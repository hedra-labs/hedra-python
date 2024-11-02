# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import character_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
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
from ..types.character_create_response import CharacterCreateResponse

__all__ = ["CharactersResource", "AsyncCharactersResource"]


class CharactersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CharactersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hedra-labs/hedra-python#accessing-raw-response-data-eg-headers
        """
        return CharactersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CharactersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hedra-labs/hedra-python#with_streaming_response
        """
        return CharactersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        aspect_ratio: Literal["1:1", "16:9", "9:16"] | NotGiven = NOT_GIVEN,
        audio_source: Literal["tts", "audio"] | NotGiven = NOT_GIVEN,
        avatar_image: Optional[str] | NotGiven = NOT_GIVEN,
        avatar_image_input: Optional[character_create_params.AvatarImageInput] | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        voice_id: Optional[str] | NotGiven = NOT_GIVEN,
        voice_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CharacterCreateResponse:
        """
        Initialize character generation

        Args:
          aspect_ratio: URL of audio uploaded using the /v1/audio endpoint

          audio_source: `tts` for text to speech or `audio`

          avatar_image: URL of image uploaded via /v1/portrait

          avatar_image_input: Image metadata

          text: text to convert to audio. Ignored if audio_source is not tts

          voice_id: Voice ID

          voice_url: URL of audio uploaded using the /v1/audio endpoint

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/characters",
            body=maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "audio_source": audio_source,
                    "avatar_image": avatar_image,
                    "avatar_image_input": avatar_image_input,
                    "text": text,
                    "voice_id": voice_id,
                    "voice_url": voice_url,
                },
                character_create_params.CharacterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CharacterCreateResponse,
        )


class AsyncCharactersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCharactersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hedra-labs/hedra-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCharactersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCharactersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hedra-labs/hedra-python#with_streaming_response
        """
        return AsyncCharactersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        aspect_ratio: Literal["1:1", "16:9", "9:16"] | NotGiven = NOT_GIVEN,
        audio_source: Literal["tts", "audio"] | NotGiven = NOT_GIVEN,
        avatar_image: Optional[str] | NotGiven = NOT_GIVEN,
        avatar_image_input: Optional[character_create_params.AvatarImageInput] | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        voice_id: Optional[str] | NotGiven = NOT_GIVEN,
        voice_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CharacterCreateResponse:
        """
        Initialize character generation

        Args:
          aspect_ratio: URL of audio uploaded using the /v1/audio endpoint

          audio_source: `tts` for text to speech or `audio`

          avatar_image: URL of image uploaded via /v1/portrait

          avatar_image_input: Image metadata

          text: text to convert to audio. Ignored if audio_source is not tts

          voice_id: Voice ID

          voice_url: URL of audio uploaded using the /v1/audio endpoint

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/characters",
            body=await async_maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "audio_source": audio_source,
                    "avatar_image": avatar_image,
                    "avatar_image_input": avatar_image_input,
                    "text": text,
                    "voice_id": voice_id,
                    "voice_url": voice_url,
                },
                character_create_params.CharacterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CharacterCreateResponse,
        )


class CharactersResourceWithRawResponse:
    def __init__(self, characters: CharactersResource) -> None:
        self._characters = characters

        self.create = to_raw_response_wrapper(
            characters.create,
        )


class AsyncCharactersResourceWithRawResponse:
    def __init__(self, characters: AsyncCharactersResource) -> None:
        self._characters = characters

        self.create = async_to_raw_response_wrapper(
            characters.create,
        )


class CharactersResourceWithStreamingResponse:
    def __init__(self, characters: CharactersResource) -> None:
        self._characters = characters

        self.create = to_streamed_response_wrapper(
            characters.create,
        )


class AsyncCharactersResourceWithStreamingResponse:
    def __init__(self, characters: AsyncCharactersResource) -> None:
        self._characters = characters

        self.create = async_to_streamed_response_wrapper(
            characters.create,
        )
