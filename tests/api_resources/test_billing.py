# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hedra import Hedra, AsyncHedra
from hedra.types import BillingListCreditsResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_credits(self, client: Hedra) -> None:
        billing = client.billing.list_credits()
        assert_matches_type(BillingListCreditsResponse, billing, path=["response"])

    @parametrize
    def test_raw_response_list_credits(self, client: Hedra) -> None:
        response = client.billing.with_raw_response.list_credits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingListCreditsResponse, billing, path=["response"])

    @parametrize
    def test_streaming_response_list_credits(self, client: Hedra) -> None:
        with client.billing.with_streaming_response.list_credits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingListCreditsResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_credits(self, async_client: AsyncHedra) -> None:
        billing = await async_client.billing.list_credits()
        assert_matches_type(BillingListCreditsResponse, billing, path=["response"])

    @parametrize
    async def test_raw_response_list_credits(self, async_client: AsyncHedra) -> None:
        response = await async_client.billing.with_raw_response.list_credits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingListCreditsResponse, billing, path=["response"])

    @parametrize
    async def test_streaming_response_list_credits(self, async_client: AsyncHedra) -> None:
        async with async_client.billing.with_streaming_response.list_credits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingListCreditsResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True
