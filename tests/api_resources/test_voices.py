# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hedra import Hedra, AsyncHedra
from hedra.types import VoiceListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Hedra) -> None:
        voice = client.voices.list()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Hedra) -> None:
        response = client.voices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Hedra) -> None:
        with client.voices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceListResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVoices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncHedra) -> None:
        voice = await async_client.voices.list()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHedra) -> None:
        response = await async_client.voices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHedra) -> None:
        async with async_client.voices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceListResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True
