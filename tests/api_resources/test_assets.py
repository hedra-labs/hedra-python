# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hedra import Hedra, AsyncHedra
from hedra.types import (
    Asset,
    AssetListResponse,
    AssetCreateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Hedra) -> None:
        asset = client.assets.create(
            name="name",
            type="image",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Hedra) -> None:
        response = client.assets.with_raw_response.create(
            name="name",
            type="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Hedra) -> None:
        with client.assets.with_streaming_response.create(
            name="name",
            type="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetCreateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Hedra) -> None:
        asset = client.assets.list(
            type="image",
        )
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hedra) -> None:
        asset = client.assets.list(
            type="image",
            ids="ids",
        )
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Hedra) -> None:
        response = client.assets.with_raw_response.list(
            type="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Hedra) -> None:
        with client.assets.with_streaming_response.list(
            type="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetListResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload(self, client: Hedra) -> None:
        asset = client.assets.upload(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )
        assert_matches_type(Asset, asset, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Hedra) -> None:
        response = client.assets.with_raw_response.upload(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(Asset, asset, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Hedra) -> None:
        with client.assets.with_streaming_response.upload(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(Asset, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upload(self, client: Hedra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.assets.with_raw_response.upload(
                id="",
                file=b"raw file contents",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncHedra) -> None:
        asset = await async_client.assets.create(
            name="name",
            type="image",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHedra) -> None:
        response = await async_client.assets.with_raw_response.create(
            name="name",
            type="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHedra) -> None:
        async with async_client.assets.with_streaming_response.create(
            name="name",
            type="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetCreateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncHedra) -> None:
        asset = await async_client.assets.list(
            type="image",
        )
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHedra) -> None:
        asset = await async_client.assets.list(
            type="image",
            ids="ids",
        )
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHedra) -> None:
        response = await async_client.assets.with_raw_response.list(
            type="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHedra) -> None:
        async with async_client.assets.with_streaming_response.list(
            type="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetListResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload(self, async_client: AsyncHedra) -> None:
        asset = await async_client.assets.upload(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )
        assert_matches_type(Asset, asset, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncHedra) -> None:
        response = await async_client.assets.with_raw_response.upload(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(Asset, asset, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncHedra) -> None:
        async with async_client.assets.with_streaming_response.upload(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(Asset, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upload(self, async_client: AsyncHedra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.assets.with_raw_response.upload(
                id="",
                file=b"raw file contents",
            )
