# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hedra import Hedra, AsyncHedra
from hedra.types import AudioCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudio:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Hedra) -> None:
        audio = client.audio.create(
            file=b"raw file contents",
        )
        assert_matches_type(AudioCreateResponse, audio, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Hedra) -> None:
        response = client.audio.with_raw_response.create(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = response.parse()
        assert_matches_type(AudioCreateResponse, audio, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Hedra) -> None:
        with client.audio.with_streaming_response.create(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = response.parse()
            assert_matches_type(AudioCreateResponse, audio, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAudio:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncHedra) -> None:
        audio = await async_client.audio.create(
            file=b"raw file contents",
        )
        assert_matches_type(AudioCreateResponse, audio, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHedra) -> None:
        response = await async_client.audio.with_raw_response.create(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = await response.parse()
        assert_matches_type(AudioCreateResponse, audio, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHedra) -> None:
        async with async_client.audio.with_streaming_response.create(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = await response.parse()
            assert_matches_type(AudioCreateResponse, audio, path=["response"])

        assert cast(Any, response.is_closed) is True
