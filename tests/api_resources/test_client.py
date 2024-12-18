# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hedra import Hedra, AsyncHedra
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_ping(self, client: Hedra) -> None:
        client_ = client.ping()
        assert_matches_type(object, client_, path=["response"])

    @parametrize
    def test_raw_response_ping(self, client: Hedra) -> None:
        response = client.with_raw_response.ping()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(object, client_, path=["response"])

    @parametrize
    def test_streaming_response_ping(self, client: Hedra) -> None:
        with client.with_streaming_response.ping() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(object, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_ping(self, async_client: AsyncHedra) -> None:
        client = await async_client.ping()
        assert_matches_type(object, client, path=["response"])

    @parametrize
    async def test_raw_response_ping(self, async_client: AsyncHedra) -> None:
        response = await async_client.with_raw_response.ping()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(object, client, path=["response"])

    @parametrize
    async def test_streaming_response_ping(self, async_client: AsyncHedra) -> None:
        async with async_client.with_streaming_response.ping() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(object, client, path=["response"])

        assert cast(Any, response.is_closed) is True
