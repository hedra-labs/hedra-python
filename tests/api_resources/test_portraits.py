# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hedra import Hedra, AsyncHedra
from hedra.types import PortraitCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPortraits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Hedra) -> None:
        portrait = client.portraits.create(
            file=b"raw file contents",
        )
        assert_matches_type(PortraitCreateResponse, portrait, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hedra) -> None:
        portrait = client.portraits.create(
            file=b"raw file contents",
            aspect_ratio="aspect_ratio",
        )
        assert_matches_type(PortraitCreateResponse, portrait, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Hedra) -> None:
        response = client.portraits.with_raw_response.create(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portrait = response.parse()
        assert_matches_type(PortraitCreateResponse, portrait, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Hedra) -> None:
        with client.portraits.with_streaming_response.create(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portrait = response.parse()
            assert_matches_type(PortraitCreateResponse, portrait, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPortraits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncHedra) -> None:
        portrait = await async_client.portraits.create(
            file=b"raw file contents",
        )
        assert_matches_type(PortraitCreateResponse, portrait, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHedra) -> None:
        portrait = await async_client.portraits.create(
            file=b"raw file contents",
            aspect_ratio="aspect_ratio",
        )
        assert_matches_type(PortraitCreateResponse, portrait, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHedra) -> None:
        response = await async_client.portraits.with_raw_response.create(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portrait = await response.parse()
        assert_matches_type(PortraitCreateResponse, portrait, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHedra) -> None:
        async with async_client.portraits.with_streaming_response.create(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portrait = await response.parse()
            assert_matches_type(PortraitCreateResponse, portrait, path=["response"])

        assert cast(Any, response.is_closed) is True
