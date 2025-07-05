# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hedra import Hedra, AsyncHedra
from hedra.types import (
    ClientListGenerationsResponse,
    ClientRetrieveGenerationStatusResponse,
)
from tests.utils import assert_matches_type
from hedra._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_generations(self, client: Hedra) -> None:
        client_ = client.client.list_generations()
        assert_matches_type(ClientListGenerationsResponse, client_, path=["response"])

    @parametrize
    def test_method_list_generations_with_all_params(self, client: Hedra) -> None:
        client_ = client.client.list_generations(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            ids="ids",
            paging_params={
                "limit": 0,
                "offset": 0,
            },
            type="image",
        )
        assert_matches_type(ClientListGenerationsResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_list_generations(self, client: Hedra) -> None:
        response = client.client.with_raw_response.list_generations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ClientListGenerationsResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_list_generations(self, client: Hedra) -> None:
        with client.client.with_streaming_response.list_generations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ClientListGenerationsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_generation_status(self, client: Hedra) -> None:
        client_ = client.client.retrieve_generation_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ClientRetrieveGenerationStatusResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_retrieve_generation_status(self, client: Hedra) -> None:
        response = client.client.with_raw_response.retrieve_generation_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ClientRetrieveGenerationStatusResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_generation_status(self, client: Hedra) -> None:
        with client.client.with_streaming_response.retrieve_generation_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ClientRetrieveGenerationStatusResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_generation_status(self, client: Hedra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            client.client.with_raw_response.retrieve_generation_status(
                "",
            )


class TestAsyncClient:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_generations(self, async_client: AsyncHedra) -> None:
        client = await async_client.client.list_generations()
        assert_matches_type(ClientListGenerationsResponse, client, path=["response"])

    @parametrize
    async def test_method_list_generations_with_all_params(self, async_client: AsyncHedra) -> None:
        client = await async_client.client.list_generations(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            ids="ids",
            paging_params={
                "limit": 0,
                "offset": 0,
            },
            type="image",
        )
        assert_matches_type(ClientListGenerationsResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_list_generations(self, async_client: AsyncHedra) -> None:
        response = await async_client.client.with_raw_response.list_generations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ClientListGenerationsResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_list_generations(self, async_client: AsyncHedra) -> None:
        async with async_client.client.with_streaming_response.list_generations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ClientListGenerationsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_generation_status(self, async_client: AsyncHedra) -> None:
        client = await async_client.client.retrieve_generation_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ClientRetrieveGenerationStatusResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_generation_status(self, async_client: AsyncHedra) -> None:
        response = await async_client.client.with_raw_response.retrieve_generation_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ClientRetrieveGenerationStatusResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_generation_status(self, async_client: AsyncHedra) -> None:
        async with async_client.client.with_streaming_response.retrieve_generation_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ClientRetrieveGenerationStatusResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_generation_status(self, async_client: AsyncHedra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            await async_client.client.with_raw_response.retrieve_generation_status(
                "",
            )
