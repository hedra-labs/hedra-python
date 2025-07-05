# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping, Optional, cast
from typing_extensions import Self, Literal, overload, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_generations_params
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    required_args,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import assets, client, models, billing
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import HedraError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.generations_response import GenerationsResponse
from .types.generated_video_inputs_param import GeneratedVideoInputsParam

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Hedra", "AsyncHedra", "Client", "AsyncClient"]


class Hedra(SyncAPIClient):
    models: models.ModelsResource
    assets: assets.AssetsResource
    client: client.ClientResource
    billing: billing.BillingResource
    with_raw_response: HedraWithRawResponse
    with_streaming_response: HedraWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Hedra client instance.

        This automatically infers the `api_key` argument from the `HEDRA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("HEDRA_API_KEY")
        if api_key is None:
            raise HedraError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HEDRA_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("HEDRA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hedra.com/web-app/Public"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.models = models.ModelsResource(self)
        self.assets = assets.AssetsResource(self)
        self.client = client.ClientResource(self)
        self.billing = billing.BillingResource(self)
        self.with_raw_response = HedraWithRawResponse(self)
        self.with_streaming_response = HedraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @overload
    def generations(
        self,
        *,
        generated_video_inputs: GeneratedVideoInputsParam,
        ai_model_id: str | NotGiven = NOT_GIVEN,
        audio_id: Optional[str] | NotGiven = NOT_GIVEN,
        start_keyframe_id: Optional[str] | NotGiven = NOT_GIVEN,
        type: Literal["video"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          generated_video_inputs: Inputs for generating the video.

          ai_model_id: ID of the model to use for the generation.

          audio_id: The id of the Audio asset to use.

          start_keyframe_id: The id of the Image asset to use as the start keyframe.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def generations(
        self,
        *,
        text: str,
        voice_id: str,
        speed: float | NotGiven = NOT_GIVEN,
        stability: float | NotGiven = NOT_GIVEN,
        type: Literal["text_to_speech"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          text: The text to convert to speech.

          voice_id: The id of the Voice to use.

          speed: Speed should be between 0.7 and 1.2, where 0.7 is the slowest and 1.2 is the
              fastest. This varies the speed of the generated speech.

          stability: Stability should be between 0-1, where 0 is the most stable and 1 is the most
              unstable. This varies the consistency between your outputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def generations(
        self,
        *,
        ai_model_id: str,
        text_prompt: str,
        aspect_ratio: Optional[str] | NotGiven = NOT_GIVEN,
        resolution: Optional[str] | NotGiven = NOT_GIVEN,
        start_keyframe_id: Optional[str] | NotGiven = NOT_GIVEN,
        type: Literal["image"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          ai_model_id: The model to use.

          text_prompt: The text prompt for image generation or image editing.

          aspect_ratio: The aspect ratio to use.

          resolution: The resolution to use formatted like '540p', '1080p', '1440p (2K QHD)', etc.

          start_keyframe_id: The id of the Image asset to use as the start keyframe.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def generations(
        self,
        *,
        ai_model_id: str,
        audio_id: str,
        type: Literal["audio_isolation"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          ai_model_id: The id of the model to use for audio isolation.

          audio_id: The id of the audio asset requiring sound isolation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def generations(
        self,
        *,
        ai_model_id: str,
        audio_id: str,
        voice_id: str,
        type: Literal["speech_to_speech"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          ai_model_id: The id of the model to use for audio isolation.

          audio_id: The id of the audio asset requiring sound isolation.

          voice_id: The id of the Voice to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def generations(
        self,
        *,
        audio_id: str,
        name: str,
        type: Literal["voice_clone"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          audio_id: The id of the Audio asset to use as the basis for the clone.

          name: The name of the new voice. Required by ElevenLabs to create a new voice.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["generated_video_inputs"],
        ["text", "voice_id"],
        ["ai_model_id", "text_prompt"],
        ["ai_model_id", "audio_id"],
        ["ai_model_id", "audio_id", "voice_id"],
        ["audio_id", "name"],
    )
    def generations(
        self,
        *,
        generated_video_inputs: GeneratedVideoInputsParam | NotGiven = NOT_GIVEN,
        ai_model_id: str | NotGiven = NOT_GIVEN,
        audio_id: Optional[str] | NotGiven = NOT_GIVEN,
        start_keyframe_id: Optional[str] | NotGiven = NOT_GIVEN,
        type: Literal["video"]
        | Literal["text_to_speech"]
        | Literal["image"]
        | Literal["audio_isolation"]
        | Literal["speech_to_speech"]
        | Literal["voice_clone"]
        | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        voice_id: str | NotGiven = NOT_GIVEN,
        speed: float | NotGiven = NOT_GIVEN,
        stability: float | NotGiven = NOT_GIVEN,
        text_prompt: str | NotGiven = NOT_GIVEN,
        aspect_ratio: Optional[str] | NotGiven = NOT_GIVEN,
        resolution: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        return cast(
            GenerationsResponse,
            self.post(
                "/generations",
                body=maybe_transform(
                    {
                        "generated_video_inputs": generated_video_inputs,
                        "ai_model_id": ai_model_id,
                        "audio_id": audio_id,
                        "start_keyframe_id": start_keyframe_id,
                        "type": type,
                        "text": text,
                        "voice_id": voice_id,
                        "speed": speed,
                        "stability": stability,
                        "text_prompt": text_prompt,
                        "aspect_ratio": aspect_ratio,
                        "resolution": resolution,
                        "name": name,
                    },
                    client_generations_params.ClientGenerationsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, GenerationsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncHedra(AsyncAPIClient):
    models: models.AsyncModelsResource
    assets: assets.AsyncAssetsResource
    client: client.AsyncClientResource
    billing: billing.AsyncBillingResource
    with_raw_response: AsyncHedraWithRawResponse
    with_streaming_response: AsyncHedraWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncHedra client instance.

        This automatically infers the `api_key` argument from the `HEDRA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("HEDRA_API_KEY")
        if api_key is None:
            raise HedraError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HEDRA_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("HEDRA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hedra.com/web-app/Public"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.models = models.AsyncModelsResource(self)
        self.assets = assets.AsyncAssetsResource(self)
        self.client = client.AsyncClientResource(self)
        self.billing = billing.AsyncBillingResource(self)
        self.with_raw_response = AsyncHedraWithRawResponse(self)
        self.with_streaming_response = AsyncHedraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @overload
    async def generations(
        self,
        *,
        generated_video_inputs: GeneratedVideoInputsParam,
        ai_model_id: str | NotGiven = NOT_GIVEN,
        audio_id: Optional[str] | NotGiven = NOT_GIVEN,
        start_keyframe_id: Optional[str] | NotGiven = NOT_GIVEN,
        type: Literal["video"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          generated_video_inputs: Inputs for generating the video.

          ai_model_id: ID of the model to use for the generation.

          audio_id: The id of the Audio asset to use.

          start_keyframe_id: The id of the Image asset to use as the start keyframe.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def generations(
        self,
        *,
        text: str,
        voice_id: str,
        speed: float | NotGiven = NOT_GIVEN,
        stability: float | NotGiven = NOT_GIVEN,
        type: Literal["text_to_speech"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          text: The text to convert to speech.

          voice_id: The id of the Voice to use.

          speed: Speed should be between 0.7 and 1.2, where 0.7 is the slowest and 1.2 is the
              fastest. This varies the speed of the generated speech.

          stability: Stability should be between 0-1, where 0 is the most stable and 1 is the most
              unstable. This varies the consistency between your outputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def generations(
        self,
        *,
        ai_model_id: str,
        text_prompt: str,
        aspect_ratio: Optional[str] | NotGiven = NOT_GIVEN,
        resolution: Optional[str] | NotGiven = NOT_GIVEN,
        start_keyframe_id: Optional[str] | NotGiven = NOT_GIVEN,
        type: Literal["image"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          ai_model_id: The model to use.

          text_prompt: The text prompt for image generation or image editing.

          aspect_ratio: The aspect ratio to use.

          resolution: The resolution to use formatted like '540p', '1080p', '1440p (2K QHD)', etc.

          start_keyframe_id: The id of the Image asset to use as the start keyframe.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def generations(
        self,
        *,
        ai_model_id: str,
        audio_id: str,
        type: Literal["audio_isolation"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          ai_model_id: The id of the model to use for audio isolation.

          audio_id: The id of the audio asset requiring sound isolation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def generations(
        self,
        *,
        ai_model_id: str,
        audio_id: str,
        voice_id: str,
        type: Literal["speech_to_speech"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          ai_model_id: The id of the model to use for audio isolation.

          audio_id: The id of the audio asset requiring sound isolation.

          voice_id: The id of the Voice to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def generations(
        self,
        *,
        audio_id: str,
        name: str,
        type: Literal["voice_clone"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        """
        Generate Asset

        Args:
          audio_id: The id of the Audio asset to use as the basis for the clone.

          name: The name of the new voice. Required by ElevenLabs to create a new voice.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["generated_video_inputs"],
        ["text", "voice_id"],
        ["ai_model_id", "text_prompt"],
        ["ai_model_id", "audio_id"],
        ["ai_model_id", "audio_id", "voice_id"],
        ["audio_id", "name"],
    )
    async def generations(
        self,
        *,
        generated_video_inputs: GeneratedVideoInputsParam | NotGiven = NOT_GIVEN,
        ai_model_id: str | NotGiven = NOT_GIVEN,
        audio_id: Optional[str] | NotGiven = NOT_GIVEN,
        start_keyframe_id: Optional[str] | NotGiven = NOT_GIVEN,
        type: Literal["video"]
        | Literal["text_to_speech"]
        | Literal["image"]
        | Literal["audio_isolation"]
        | Literal["speech_to_speech"]
        | Literal["voice_clone"]
        | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        voice_id: str | NotGiven = NOT_GIVEN,
        speed: float | NotGiven = NOT_GIVEN,
        stability: float | NotGiven = NOT_GIVEN,
        text_prompt: str | NotGiven = NOT_GIVEN,
        aspect_ratio: Optional[str] | NotGiven = NOT_GIVEN,
        resolution: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerationsResponse:
        return cast(
            GenerationsResponse,
            await self.post(
                "/generations",
                body=await async_maybe_transform(
                    {
                        "generated_video_inputs": generated_video_inputs,
                        "ai_model_id": ai_model_id,
                        "audio_id": audio_id,
                        "start_keyframe_id": start_keyframe_id,
                        "type": type,
                        "text": text,
                        "voice_id": voice_id,
                        "speed": speed,
                        "stability": stability,
                        "text_prompt": text_prompt,
                        "aspect_ratio": aspect_ratio,
                        "resolution": resolution,
                        "name": name,
                    },
                    client_generations_params.ClientGenerationsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, GenerationsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class HedraWithRawResponse:
    def __init__(self, client: Hedra) -> None:
        self.models = models.ModelsResourceWithRawResponse(client.models)
        self.assets = assets.AssetsResourceWithRawResponse(client.assets)
        self.client = client.ClientResourceWithRawResponse(client.client)
        self.billing = billing.BillingResourceWithRawResponse(client.billing)

        self.generations = to_raw_response_wrapper(
            client.generations,
        )


class AsyncHedraWithRawResponse:
    def __init__(self, client: AsyncHedra) -> None:
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.assets = assets.AsyncAssetsResourceWithRawResponse(client.assets)
        self.client = client.AsyncClientResourceWithRawResponse(client.client)
        self.billing = billing.AsyncBillingResourceWithRawResponse(client.billing)

        self.generations = async_to_raw_response_wrapper(
            client.generations,
        )


class HedraWithStreamedResponse:
    def __init__(self, client: Hedra) -> None:
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.assets = assets.AssetsResourceWithStreamingResponse(client.assets)
        self.client = client.ClientResourceWithStreamingResponse(client.client)
        self.billing = billing.BillingResourceWithStreamingResponse(client.billing)

        self.generations = to_streamed_response_wrapper(
            client.generations,
        )


class AsyncHedraWithStreamedResponse:
    def __init__(self, client: AsyncHedra) -> None:
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.assets = assets.AsyncAssetsResourceWithStreamingResponse(client.assets)
        self.client = client.AsyncClientResourceWithStreamingResponse(client.client)
        self.billing = billing.AsyncBillingResourceWithStreamingResponse(client.billing)

        self.generations = async_to_streamed_response_wrapper(
            client.generations,
        )


Client = Hedra

AsyncClient = AsyncHedra
