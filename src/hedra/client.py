# Hand-maintained wrapper around the Fern-generated BaseHedra/AsyncBaseHedra.
# Listed in .fernignore so it survives regeneration (base_client.py regenerates).
#
# Customizations:
#   1. The API key is read from HEDRA_API_KEY at *construction* time rather than
#      as an import-time default argument, so `load_dotenv(); Hedra()` works
#      regardless of import order.
#   2. `client.jobs.submit(model, input=...)` — a typed passthrough that submits
#      to any model id, including ones this SDK build predates. See below.

import os
import typing
from json.decoder import JSONDecodeError

import httpx
from . import errors as _errors
from .base_client import AsyncBaseHedra, BaseHedra
from .core.api_error import ApiError
from .core.jsonable_encoder import encode_path_param
from .core.logging import LogConfig, Logger
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .environment import HedraEnvironment
from .types.error_response import ErrorResponse
from .types.submit_response import SubmitResponse
from pydantic import ValidationError

if typing.TYPE_CHECKING:
    from .jobs.client import AsyncJobsClient, JobsClient
    from .jobs.raw_client import AsyncRawJobsClient, RawJobsClient

__all__ = ["AsyncHedra", "AsyncHedraJobsClient", "Hedra", "HedraJobsClient"]


def _resolve_api_key(api_key: typing.Optional[str]) -> typing.Optional[str]:
    return api_key if api_key is not None else os.environ.get("HEDRA_API_KEY")


# ---------------------------------------------------------------------------
# Typed submit passthrough
#
# Why this is exact rather than approximate: every per-model submit operation in
# the spec declares the same contract — `202 -> SubmitResponse`, errors
# `{400, 401, 402, 403, 404, 422, 429, 500} -> ErrorResponse`. So one handler
# reproduces the generated `submit_<model>()` methods byte-for-byte on the wire
# and object-for-object on the way back. Retries, backoff, `Retry-After`, auth,
# per-request overrides, logging and redaction all come along unchanged: they
# live in core.http_client.HttpClient.request, which is the same function the
# generated raw clients call.
#
# The only thing given up versus `submit_<model>()` is compile-time validation of
# `input`, which is the point of an escape hatch.
# ---------------------------------------------------------------------------

# Same sentinel the generated raw clients use: a field left as OMIT is stripped
# from the request body rather than serialized as null.
OMIT = typing.cast(typing.Any, ...)

# Every per-model submit declares exactly this error set.
_ERROR_CLASS_NAMES: typing.Dict[int, str] = {
    400: "BadRequestError",
    401: "UnauthorizedError",
    402: "PaymentRequiredError",
    403: "ForbiddenError",
    404: "NotFoundError",
    422: "UnprocessableEntityError",
    429: "TooManyRequestsError",
    500: "InternalServerError",
}


def _error_class_for(status_code: int) -> typing.Optional[typing.Any]:
    """Resolve a status code to its generated error class, if this build has one.

    Looked up by name off `hedra.errors` rather than imported directly, because the
    generated error classes track the spec: an SDK built before the API wallet
    landed has no `PaymentRequiredError`, and importing it unconditionally would
    make this module unimportable there. A status whose class is absent falls
    through to `ApiError` — the same thing the generated methods do for a status
    they do not declare — and starts mapping on its own the next time regeneration
    adds the class. No code change needed when that happens.
    """
    name = _ERROR_CLASS_NAMES.get(status_code)
    if name is None:
        return None
    return getattr(_errors, name, None)


def _parse_submit_response(response: httpx.Response) -> SubmitResponse:
    """Mirror of the generated per-model submit response handling."""
    try:
        if 200 <= response.status_code < 300:
            return typing.cast(
                SubmitResponse,
                parse_obj_as(type_=SubmitResponse, object_=response.json()),  # type: ignore
            )
        error_class = _error_class_for(response.status_code)
        if error_class is not None:
            raise error_class(
                headers=dict(response.headers),
                body=typing.cast(
                    ErrorResponse,
                    parse_obj_as(type_=ErrorResponse, object_=response.json()),  # type: ignore
                ),
            )
        _response_json = response.json()
    except JSONDecodeError:
        raise ApiError(
            status_code=response.status_code,
            headers=dict(response.headers),
            body=response.text,
        )
    except ValidationError as e:
        raise ParsingError(
            status_code=response.status_code,
            headers=dict(response.headers),
            body=response.json(),
            cause=e,
        )
    raise ApiError(
        status_code=response.status_code,
        headers=dict(response.headers),
        body=_response_json,
    )


def _submit_body(
    input: typing.Dict[str, typing.Any],
    webhook: typing.Optional[str],
    idempotency_key: typing.Optional[str],
) -> typing.Dict[str, typing.Any]:
    return {"input": input, "webhook": webhook, "idempotency_key": idempotency_key}


_SUBMIT_DOC = """Submit to any model id, including ones this SDK build predates.

Identical on the wire to `submit_<model>()` and returns the same
`SubmitResponse`; `input` is an untyped dict rather than a generated
model, so it is not validated before the request goes out. Fetch the
model's input schema at runtime with `client.models.get_openapi(model)`
when you need one.

Parameters
----------
model : str
    The model's public id (`GET /v3/models`).

input : typing.Dict[str, typing.Any]
    Model-specific inputs, exactly as `submit_<model>()` would carry them.

webhook : typing.Optional[str]
    URL to receive a signed completion webhook.

idempotency_key : typing.Optional[str]
    Replays the original ack for a retried submit instead of enqueueing a
    duplicate job.

request_options : typing.Optional[RequestOptions]
    Request-specific configuration.

Returns
-------
SubmitResponse
    Accepted. The job runs asynchronously; poll `status_url` / `result_url`
    from the ack.

Examples
--------
from hedra import Hedra

client = Hedra()
ack = client.jobs.submit("gpt-image-2", input={"prompt": "a space cat"})
"""


# The `submit` implementations live on mixins so that importing this module does
# not pull in hedra.jobs.client, which transitively loads every generated input
# type (~0.9s). The generated `jobs` property defers that import to first access;
# the concrete subclasses below are built at the same moment, preserving it.
class _SubmitPassthroughMixin:
    if typing.TYPE_CHECKING:
        _raw_client: "RawJobsClient"

    def submit(
        self,
        model: str,
        *,
        input: typing.Dict[str, typing.Any],
        webhook: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubmitResponse:
        _response = self._raw_client._client_wrapper.httpx_client.request(
            f"models/{encode_path_param(model)}",
            method="POST",
            json=_submit_body(input, webhook, idempotency_key),
            headers={"content-type": "application/json"},
            request_options=request_options,
            omit=OMIT,
        )
        return _parse_submit_response(_response)

    submit.__doc__ = _SUBMIT_DOC


class _AsyncSubmitPassthroughMixin:
    if typing.TYPE_CHECKING:
        _raw_client: "AsyncRawJobsClient"

    async def submit(
        self,
        model: str,
        *,
        input: typing.Dict[str, typing.Any],
        webhook: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubmitResponse:
        _response = await self._raw_client._client_wrapper.httpx_client.request(
            f"models/{encode_path_param(model)}",
            method="POST",
            json=_submit_body(input, webhook, idempotency_key),
            headers={"content-type": "application/json"},
            request_options=request_options,
            omit=OMIT,
        )
        return _parse_submit_response(_response)

    submit.__doc__ = _SUBMIT_DOC


if typing.TYPE_CHECKING:
    # Statically these are ordinary subclasses, so `client.jobs.submit(...)` type
    # checks and IDEs complete it alongside every generated `submit_<model>`. At
    # runtime they are built on first use by the factories below — that is what
    # keeps the generated jobs module off the import path.
    class HedraJobsClient(_SubmitPassthroughMixin, JobsClient):
        """The generated jobs client plus an untyped `submit` for any model id."""

    class AsyncHedraJobsClient(_AsyncSubmitPassthroughMixin, AsyncJobsClient):
        """Async counterpart of :class:`HedraJobsClient`."""


_jobs_client_cls: typing.Optional[typing.Any] = None
_async_jobs_client_cls: typing.Optional[typing.Any] = None


def _hedra_jobs_client_cls() -> typing.Any:
    global _jobs_client_cls
    if _jobs_client_cls is None:
        from .jobs.client import JobsClient  # noqa: E402

        class HedraJobsClient(_SubmitPassthroughMixin, JobsClient):  # type: ignore[no-redef]
            """The generated jobs client plus an untyped `submit` for any model id."""

        _jobs_client_cls = HedraJobsClient
    return _jobs_client_cls


def _async_hedra_jobs_client_cls() -> typing.Any:
    global _async_jobs_client_cls
    if _async_jobs_client_cls is None:
        from .jobs.client import AsyncJobsClient  # noqa: E402

        class AsyncHedraJobsClient(_AsyncSubmitPassthroughMixin, AsyncJobsClient):  # type: ignore[no-redef]
            """Async counterpart of :class:`HedraJobsClient`."""

        _async_jobs_client_cls = AsyncHedraJobsClient
    return _async_jobs_client_cls


def __getattr__(attr_name: str) -> typing.Any:
    # `hedra.client.HedraJobsClient` / `AsyncHedraJobsClient` resolve on demand,
    # so neither `import hedra` nor `from hedra import Hedra` pays for the
    # generated jobs module. Mirrors the lazy attribute access the generated
    # packages use.
    if attr_name == "HedraJobsClient":
        return _hedra_jobs_client_cls()
    if attr_name == "AsyncHedraJobsClient":
        return _async_hedra_jobs_client_cls()
    raise AttributeError(f"module {__name__!r} has no attribute {attr_name!r}")


def __dir__() -> typing.List[str]:
    return sorted(set(globals()) | {"AsyncHedraJobsClient", "HedraJobsClient"})


class Hedra(BaseHedra):
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: HedraEnvironment = HedraEnvironment.PRODUCTION,
        api_key: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        super().__init__(
            base_url=base_url,
            environment=environment,
            api_key=_resolve_api_key(api_key),
            headers=headers,
            timeout=timeout,
            max_retries=max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
        )

    @property
    def jobs(self) -> "HedraJobsClient":
        # Overrides BaseHedra.jobs to hand back the passthrough subclass. Same
        # lazy-construct-and-cache contract as the generated property, so every
        # generated method stays exactly where it was and `submit` joins them.
        if self._jobs is None:
            self._jobs = _hedra_jobs_client_cls()(client_wrapper=self._client_wrapper)
        return typing.cast("HedraJobsClient", self._jobs)


class AsyncHedra(AsyncBaseHedra):
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: HedraEnvironment = HedraEnvironment.PRODUCTION,
        api_key: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        super().__init__(
            base_url=base_url,
            environment=environment,
            api_key=_resolve_api_key(api_key),
            headers=headers,
            timeout=timeout,
            max_retries=max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
        )

    @property
    def jobs(self) -> "AsyncHedraJobsClient":
        if self._jobs is None:
            self._jobs = _async_hedra_jobs_client_cls()(client_wrapper=self._client_wrapper)
        return typing.cast("AsyncHedraJobsClient", self._jobs)
