"""Verify the typed `client.jobs.submit()` passthrough matches the generated per-model submit.

The passthrough (in `src/hedra/client.py`) exists so callers can submit to a model
id this SDK build predates. It is exact rather than approximate: every per-model
submit in the spec declares the same contract — `202 -> SubmitResponse`, errors
`{400, 401, 402, 403, 404, 422, 429, 500} -> ErrorResponse` — so one handler
reproduces them on the wire and on the way back. These tests pin that down.

Lives under tests/custom/ so Fern preserves it across regeneration.
"""

import json
import typing

import httpx
import pytest

import hedra.errors
from hedra import AsyncHedra, Hedra
from hedra.client import AsyncHedraJobsClient, HedraJobsClient
from hedra.core.api_error import ApiError
from hedra.core.parse_error import ParsingError
from hedra.core.request_options import RequestOptions
from hedra.errors import (
    BadRequestError,
    ForbiddenError,
    InternalServerError,
    NotFoundError,
    TooManyRequestsError,
    UnauthorizedError,
    UnprocessableEntityError,
)
from hedra.types import InputGptImage2
from hedra.types.error_response import ErrorResponse
from hedra.types.submit_response import SubmitResponse

ACK = {
    "job_id": "job_abc",
    "model": "some-new-model",
    "status": "IN_QUEUE",
    "status_url": "/v3/jobs/job_abc/status",
    "result_url": "/v3/jobs/job_abc",
    "estimated_completion_at": "2026-08-05T20:00:00Z",
}

ERROR_BODY = {"error": {"code": "SOME_CODE", "message": "boom", "retryable": False}}

# Error responses must not be retried away before the assertion sees them.
NO_RETRY = RequestOptions(max_retries=0)

# 402 postdates the spec this SDK build was generated from, so the generated
# `PaymentRequiredError` may not exist yet. The passthrough resolves its error map
# by class name, so it starts mapping 402 the moment regeneration adds the class
# and falls through to ApiError (like any undeclared status) until then. Resolving
# it the same way here keeps this file green on both sides of that boundary.
PaymentRequiredError = getattr(hedra.errors, "PaymentRequiredError", None)

DECLARED_ERRORS: typing.List[typing.Tuple[int, typing.Type[ApiError]]] = [
    (400, BadRequestError),
    (401, UnauthorizedError),
    (403, ForbiddenError),
    (404, NotFoundError),
    (422, UnprocessableEntityError),
    (429, TooManyRequestsError),
    (500, InternalServerError),
]
if PaymentRequiredError is not None:
    DECLARED_ERRORS.insert(2, (402, PaymentRequiredError))


class Responder:
    """Mock transport handler that records the request it served."""

    def __init__(
        self,
        status: int,
        body: typing.Optional[typing.Any] = None,
        *,
        text: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
    ) -> None:
        self._status = status
        self._body = body
        self._text = text
        self._headers = headers or {}
        self.request: typing.Optional[httpx.Request] = None

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.request = request
        if self._text is not None:
            return httpx.Response(self._status, text=self._text, headers=self._headers)
        return httpx.Response(self._status, json=self._body, headers=self._headers)

    def sent_body(self) -> typing.Any:
        assert self.request is not None, "no request was served"
        return json.loads(self.request.content)


def _client(responder: Responder) -> Hedra:
    return Hedra(api_key="test-key", httpx_client=httpx.Client(transport=httpx.MockTransport(responder)))


def _async_client(responder: Responder) -> AsyncHedra:
    return AsyncHedra(api_key="test-key", httpx_client=httpx.AsyncClient(transport=httpx.MockTransport(responder)))


# --- the passthrough is wired onto the exported clients ---------------------


def test_jobs_property_exposes_the_passthrough_client() -> None:
    client = _client(Responder(202, ACK))
    assert isinstance(client.jobs, HedraJobsClient)
    assert client.jobs is client.jobs  # the generated lazy-cache behavior is preserved


def test_async_jobs_property_exposes_the_passthrough_client() -> None:
    client = _async_client(Responder(202, ACK))
    assert isinstance(client.jobs, AsyncHedraJobsClient)
    assert client.jobs is client.jobs


def test_generated_methods_are_untouched() -> None:
    client = _client(Responder(202, ACK))
    assert hasattr(client.jobs, "submit_gpt_image2")
    assert hasattr(client.jobs, "get_status")
    assert hasattr(client.jobs, "stream")
    assert hasattr(client.models, "estimate")


# --- 202 parses into a real SubmitResponse ----------------------------------


def test_accepted_response_parses_into_submit_response() -> None:
    ack = _client(Responder(202, ACK)).jobs.submit("some-new-model", input={"prompt": "a space cat"})

    assert isinstance(ack, SubmitResponse)
    assert ack.job_id == "job_abc"
    assert ack.status == "IN_QUEUE"
    # pydantic coerces the ISO-8601 string, exactly as the generated method does
    assert type(ack.estimated_completion_at).__name__ == "datetime"


# --- error mapping ----------------------------------------------------------


@pytest.mark.parametrize("status,exc", DECLARED_ERRORS, ids=[str(s) for s, _ in DECLARED_ERRORS])
def test_declared_error_status_raises_its_generated_class(status: int, exc: typing.Type[ApiError]) -> None:
    client = _client(Responder(status, ERROR_BODY))

    with pytest.raises(exc) as excinfo:
        client.jobs.submit("m", input={}, request_options=NO_RETRY)

    # the ErrorResponse body is parsed, not left as a raw dict
    assert excinfo.value.body.error.message == "boom"
    assert excinfo.value.body.error.code == "SOME_CODE"


@pytest.mark.skipif(
    PaymentRequiredError is not None,
    reason="this build declares PaymentRequiredError; covered by the parametrized case",
)
def test_402_falls_through_to_api_error_until_regeneration_adds_the_class() -> None:
    # Documents the pre-regeneration behavior: a status whose generated class is
    # absent behaves exactly like an undeclared status on a generated method.
    client = _client(Responder(402, ERROR_BODY))

    with pytest.raises(ApiError) as excinfo:
        client.jobs.submit("m", input={}, request_options=NO_RETRY)

    assert excinfo.value.status_code == 402


def test_error_map_picks_up_a_class_a_later_regeneration_adds(monkeypatch: pytest.MonkeyPatch) -> None:
    # The claim the 402 skip above rests on: the passthrough resolves error classes
    # by name at response time, so a status starts mapping the moment regeneration
    # adds its class — no change needed here. Plant one the way regeneration would.
    class PlantedError(ApiError):
        def __init__(self, body: ErrorResponse, headers: typing.Optional[typing.Dict[str, str]] = None) -> None:
            super().__init__(status_code=402, headers=headers, body=body)

    monkeypatch.setattr(hedra.errors, "PaymentRequiredError", PlantedError, raising=False)
    client = _client(Responder(402, ERROR_BODY))

    with pytest.raises(PlantedError) as excinfo:
        client.jobs.submit("m", input={}, request_options=NO_RETRY)

    assert excinfo.value.body.error.message == "boom"


def test_undeclared_status_raises_api_error() -> None:
    client = _client(Responder(418, {"weird": True}))

    with pytest.raises(ApiError) as excinfo:
        client.jobs.submit("m", input={}, request_options=NO_RETRY)

    assert excinfo.value.status_code == 418
    assert excinfo.value.body == {"weird": True}


def test_non_json_body_raises_api_error_carrying_the_raw_text() -> None:
    client = _client(Responder(502, text="<html>bad gateway</html>"))

    with pytest.raises(ApiError) as excinfo:
        client.jobs.submit("m", input={}, request_options=NO_RETRY)

    assert "bad gateway" in str(excinfo.value.body)


def test_schema_violating_accepted_response_raises_parsing_error() -> None:
    client = _client(Responder(202, {"job_id": "j"}))  # missing every other required field

    with pytest.raises(ParsingError) as excinfo:
        client.jobs.submit("m", input={})

    assert excinfo.value.status_code == 202


# --- OMIT semantics: unset / supplied / explicit null are three states -------


def test_unset_optionals_are_stripped_from_the_body() -> None:
    responder = Responder(202, ACK)
    _client(responder).jobs.submit("m", input={"prompt": "x"})

    assert responder.sent_body() == {"input": {"prompt": "x"}}


def test_supplied_optionals_are_sent() -> None:
    responder = Responder(202, ACK)
    _client(responder).jobs.submit("m", input={"prompt": "x"}, webhook="https://cb", idempotency_key="idem-1")

    assert responder.sent_body() == {
        "input": {"prompt": "x"},
        "webhook": "https://cb",
        "idempotency_key": "idem-1",
    }


def test_explicit_none_is_sent_as_null_and_is_distinct_from_unset() -> None:
    responder = Responder(202, ACK)
    _client(responder).jobs.submit("m", input={"prompt": "x"}, webhook=None)

    assert responder.sent_body() == {"input": {"prompt": "x"}, "webhook": None}


# --- wire parity with the generated per-model method ------------------------


def test_wire_matches_the_generated_per_model_submit() -> None:
    generated = Responder(202, ACK)
    _client(generated).jobs.submit_gpt_image2(
        input=InputGptImage2(prompt="a space cat", quality="medium", aspect_ratio="1:1", resolution="1K")
    )

    passthrough = Responder(202, ACK)
    _client(passthrough).jobs.submit(
        "gpt-image-2",
        input={"prompt": "a space cat", "quality": "medium", "aspect_ratio": "1:1", "resolution": "1K"},
    )

    gen_req, pt_req = generated.request, passthrough.request
    assert gen_req is not None and pt_req is not None
    assert str(pt_req.url) == str(gen_req.url) == "https://api.hedra.com/v3/models/gpt-image-2"
    assert pt_req.method == gen_req.method == "POST"
    assert pt_req.headers.get("content-type") == gen_req.headers.get("content-type")
    assert pt_req.headers.get("authorization") == gen_req.headers.get("authorization")
    # JSON objects are unordered: the generated method serializes in pydantic
    # field-declaration order, the passthrough in caller dict order. Compare parsed.
    assert passthrough.sent_body() == generated.sent_body()


def test_model_slug_is_path_encoded() -> None:
    responder = Responder(202, ACK)
    _client(responder).jobs.submit("weird/../slug", input={})

    assert responder.request is not None
    assert ".." not in str(responder.request.url)


# --- async variant ----------------------------------------------------------


async def test_async_accepted_response_parses_into_submit_response() -> None:
    responder = Responder(202, ACK)
    ack = await _async_client(responder).jobs.submit("some-new-model", input={"prompt": "x"})

    assert isinstance(ack, SubmitResponse)
    assert ack.job_id == "job_abc"
    assert responder.sent_body() == {"input": {"prompt": "x"}}


async def test_async_declared_error_status_raises_its_generated_class() -> None:
    responder = Responder(429, ERROR_BODY)

    with pytest.raises(TooManyRequestsError) as excinfo:
        await _async_client(responder).jobs.submit("m", input={}, request_options=NO_RETRY)

    assert excinfo.value.body.error.message == "boom"


async def test_async_undeclared_status_raises_api_error() -> None:
    responder = Responder(418, {"weird": True})

    with pytest.raises(ApiError) as excinfo:
        await _async_client(responder).jobs.submit("m", input={}, request_options=NO_RETRY)

    assert excinfo.value.status_code == 418
