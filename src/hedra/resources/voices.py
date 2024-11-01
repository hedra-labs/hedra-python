# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.voice_list_response import VoiceListResponse

__all__ = ["VoicesResource", "AsyncVoicesResource"]


class VoicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hedra-python#accessing-raw-response-data-eg-headers
        """
        return VoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hedra-python#with_streaming_response
        """
        return VoicesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoiceListResponse:
        """Retrieve available voices"""
        return self._get(
            "/v1/voices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceListResponse,
        )


class AsyncVoicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hedra-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hedra-python#with_streaming_response
        """
        return AsyncVoicesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoiceListResponse:
        """Retrieve available voices"""
        return await self._get(
            "/v1/voices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceListResponse,
        )


class VoicesResourceWithRawResponse:
    def __init__(self, voices: VoicesResource) -> None:
        self._voices = voices

        self.list = to_raw_response_wrapper(
            voices.list,
        )


class AsyncVoicesResourceWithRawResponse:
    def __init__(self, voices: AsyncVoicesResource) -> None:
        self._voices = voices

        self.list = async_to_raw_response_wrapper(
            voices.list,
        )


class VoicesResourceWithStreamingResponse:
    def __init__(self, voices: VoicesResource) -> None:
        self._voices = voices

        self.list = to_streamed_response_wrapper(
            voices.list,
        )


class AsyncVoicesResourceWithStreamingResponse:
    def __init__(self, voices: AsyncVoicesResource) -> None:
        self._voices = voices

        self.list = async_to_streamed_response_wrapper(
            voices.list,
        )