# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import portrait_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.portrait_create_response import PortraitCreateResponse

__all__ = ["PortraitsResource", "AsyncPortraitsResource"]


class PortraitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortraitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hedra-labs/hedra-python#accessing-raw-response-data-eg-headers
        """
        return PortraitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortraitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hedra-labs/hedra-python#with_streaming_response
        """
        return PortraitsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file: FileTypes,
        aspect_ratio: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortraitCreateResponse:
        """
        Upload image

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/portrait",
            body=maybe_transform(body, portrait_create_params.PortraitCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"aspect_ratio": aspect_ratio}, portrait_create_params.PortraitCreateParams),
            ),
            cast_to=PortraitCreateResponse,
        )


class AsyncPortraitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortraitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hedra-labs/hedra-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortraitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortraitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hedra-labs/hedra-python#with_streaming_response
        """
        return AsyncPortraitsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: FileTypes,
        aspect_ratio: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortraitCreateResponse:
        """
        Upload image

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/portrait",
            body=await async_maybe_transform(body, portrait_create_params.PortraitCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"aspect_ratio": aspect_ratio}, portrait_create_params.PortraitCreateParams
                ),
            ),
            cast_to=PortraitCreateResponse,
        )


class PortraitsResourceWithRawResponse:
    def __init__(self, portraits: PortraitsResource) -> None:
        self._portraits = portraits

        self.create = to_raw_response_wrapper(
            portraits.create,
        )


class AsyncPortraitsResourceWithRawResponse:
    def __init__(self, portraits: AsyncPortraitsResource) -> None:
        self._portraits = portraits

        self.create = async_to_raw_response_wrapper(
            portraits.create,
        )


class PortraitsResourceWithStreamingResponse:
    def __init__(self, portraits: PortraitsResource) -> None:
        self._portraits = portraits

        self.create = to_streamed_response_wrapper(
            portraits.create,
        )


class AsyncPortraitsResourceWithStreamingResponse:
    def __init__(self, portraits: AsyncPortraitsResource) -> None:
        self._portraits = portraits

        self.create = async_to_streamed_response_wrapper(
            portraits.create,
        )
