# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import client_list_generations_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.client_list_generations_response import ClientListGenerationsResponse
from ..types.client_retrieve_generation_status_response import ClientRetrieveGenerationStatusResponse

__all__ = ["ClientResource", "AsyncClientResource"]


class ClientResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hedra-labs/hedra-python#accessing-raw-response-data-eg-headers
        """
        return ClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hedra-labs/hedra-python#with_streaming_response
        """
        return ClientResourceWithStreamingResponse(self)

    def list_generations(
        self,
        *,
        created_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        ids: Optional[str] | NotGiven = NOT_GIVEN,
        paging_params: client_list_generations_params.PagingParams | NotGiven = NOT_GIVEN,
        type: Optional[
            Literal[
                "image",
                "audio",
                "video",
                "text_to_speech",
                "speech_to_speech",
                "voice_clone",
                "audio_isolation",
                "video_stitching",
                "agent_response",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientListGenerationsResponse:
        """
        List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/generations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "ids": ids,
                        "paging_params": paging_params,
                        "type": type,
                    },
                    client_list_generations_params.ClientListGenerationsParams,
                ),
            ),
            cast_to=ClientListGenerationsResponse,
        )

    def retrieve_generation_status(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientRetrieveGenerationStatusResponse:
        """
        Get Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return self._get(
            f"/generations/{generation_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientRetrieveGenerationStatusResponse,
        )


class AsyncClientResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hedra-labs/hedra-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hedra-labs/hedra-python#with_streaming_response
        """
        return AsyncClientResourceWithStreamingResponse(self)

    async def list_generations(
        self,
        *,
        created_after: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        ids: Optional[str] | NotGiven = NOT_GIVEN,
        paging_params: client_list_generations_params.PagingParams | NotGiven = NOT_GIVEN,
        type: Optional[
            Literal[
                "image",
                "audio",
                "video",
                "text_to_speech",
                "speech_to_speech",
                "voice_clone",
                "audio_isolation",
                "video_stitching",
                "agent_response",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientListGenerationsResponse:
        """
        List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/generations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "ids": ids,
                        "paging_params": paging_params,
                        "type": type,
                    },
                    client_list_generations_params.ClientListGenerationsParams,
                ),
            ),
            cast_to=ClientListGenerationsResponse,
        )

    async def retrieve_generation_status(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientRetrieveGenerationStatusResponse:
        """
        Get Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return await self._get(
            f"/generations/{generation_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientRetrieveGenerationStatusResponse,
        )


class ClientResourceWithRawResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

        self.list_generations = to_raw_response_wrapper(
            client.list_generations,
        )
        self.retrieve_generation_status = to_raw_response_wrapper(
            client.retrieve_generation_status,
        )


class AsyncClientResourceWithRawResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

        self.list_generations = async_to_raw_response_wrapper(
            client.list_generations,
        )
        self.retrieve_generation_status = async_to_raw_response_wrapper(
            client.retrieve_generation_status,
        )


class ClientResourceWithStreamingResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

        self.list_generations = to_streamed_response_wrapper(
            client.list_generations,
        )
        self.retrieve_generation_status = to_streamed_response_wrapper(
            client.retrieve_generation_status,
        )


class AsyncClientResourceWithStreamingResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

        self.list_generations = async_to_streamed_response_wrapper(
            client.list_generations,
        )
        self.retrieve_generation_status = async_to_streamed_response_wrapper(
            client.retrieve_generation_status,
        )
