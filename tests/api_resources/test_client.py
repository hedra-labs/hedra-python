# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hedra import Hedra, AsyncHedra
from hedra.types import GenerationsResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generations_overload_1(self, client: Hedra) -> None:
        client_ = client.generations(
            generated_video_inputs={"text_prompt": "text_prompt"},
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_method_generations_with_all_params_overload_1(self, client: Hedra) -> None:
        client_ = client.generations(
            generated_video_inputs={
                "text_prompt": "text_prompt",
                "aspect_ratio": "aspect_ratio",
                "bounding_box_target": [{}, {}],
                "duration_ms": 0,
                "resolution": "resolution",
            },
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            start_keyframe_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="video",
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_generations_overload_1(self, client: Hedra) -> None:
        response = client.with_raw_response.generations(
            generated_video_inputs={"text_prompt": "text_prompt"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_generations_overload_1(self, client: Hedra) -> None:
        with client.with_streaming_response.generations(
            generated_video_inputs={"text_prompt": "text_prompt"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GenerationsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generations_overload_2(self, client: Hedra) -> None:
        client_ = client.generations(
            text="text",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_method_generations_with_all_params_overload_2(self, client: Hedra) -> None:
        client_ = client.generations(
            text="text",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            speed=0.7,
            stability=0,
            type="text_to_speech",
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_generations_overload_2(self, client: Hedra) -> None:
        response = client.with_raw_response.generations(
            text="text",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_generations_overload_2(self, client: Hedra) -> None:
        with client.with_streaming_response.generations(
            text="text",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GenerationsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generations_overload_3(self, client: Hedra) -> None:
        client_ = client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text_prompt="text_prompt",
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_method_generations_with_all_params_overload_3(self, client: Hedra) -> None:
        client_ = client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text_prompt="text_prompt",
            aspect_ratio="aspect_ratio",
            resolution="resolution",
            start_keyframe_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="image",
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_generations_overload_3(self, client: Hedra) -> None:
        response = client.with_raw_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text_prompt="text_prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_generations_overload_3(self, client: Hedra) -> None:
        with client.with_streaming_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text_prompt="text_prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GenerationsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generations_overload_4(self, client: Hedra) -> None:
        client_ = client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_method_generations_with_all_params_overload_4(self, client: Hedra) -> None:
        client_ = client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="audio_isolation",
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_generations_overload_4(self, client: Hedra) -> None:
        response = client.with_raw_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_generations_overload_4(self, client: Hedra) -> None:
        with client.with_streaming_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GenerationsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generations_overload_5(self, client: Hedra) -> None:
        client_ = client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_method_generations_with_all_params_overload_5(self, client: Hedra) -> None:
        client_ = client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="speech_to_speech",
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_generations_overload_5(self, client: Hedra) -> None:
        response = client.with_raw_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_generations_overload_5(self, client: Hedra) -> None:
        with client.with_streaming_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GenerationsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generations_overload_6(self, client: Hedra) -> None:
        client_ = client.generations(
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_method_generations_with_all_params_overload_6(self, client: Hedra) -> None:
        client_ = client.generations(
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="voice_clone",
        )
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_generations_overload_6(self, client: Hedra) -> None:
        response = client.with_raw_response.generations(
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GenerationsResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_generations_overload_6(self, client: Hedra) -> None:
        with client.with_streaming_response.generations(
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GenerationsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_generations_overload_1(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            generated_video_inputs={"text_prompt": "text_prompt"},
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_method_generations_with_all_params_overload_1(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            generated_video_inputs={
                "text_prompt": "text_prompt",
                "aspect_ratio": "aspect_ratio",
                "bounding_box_target": [{}, {}],
                "duration_ms": 0,
                "resolution": "resolution",
            },
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            start_keyframe_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="video",
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_generations_overload_1(self, async_client: AsyncHedra) -> None:
        response = await async_client.with_raw_response.generations(
            generated_video_inputs={"text_prompt": "text_prompt"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_generations_overload_1(self, async_client: AsyncHedra) -> None:
        async with async_client.with_streaming_response.generations(
            generated_video_inputs={"text_prompt": "text_prompt"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GenerationsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generations_overload_2(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            text="text",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_method_generations_with_all_params_overload_2(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            text="text",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            speed=0.7,
            stability=0,
            type="text_to_speech",
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_generations_overload_2(self, async_client: AsyncHedra) -> None:
        response = await async_client.with_raw_response.generations(
            text="text",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_generations_overload_2(self, async_client: AsyncHedra) -> None:
        async with async_client.with_streaming_response.generations(
            text="text",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GenerationsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generations_overload_3(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text_prompt="text_prompt",
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_method_generations_with_all_params_overload_3(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text_prompt="text_prompt",
            aspect_ratio="aspect_ratio",
            resolution="resolution",
            start_keyframe_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="image",
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_generations_overload_3(self, async_client: AsyncHedra) -> None:
        response = await async_client.with_raw_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text_prompt="text_prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_generations_overload_3(self, async_client: AsyncHedra) -> None:
        async with async_client.with_streaming_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text_prompt="text_prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GenerationsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generations_overload_4(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_method_generations_with_all_params_overload_4(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="audio_isolation",
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_generations_overload_4(self, async_client: AsyncHedra) -> None:
        response = await async_client.with_raw_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_generations_overload_4(self, async_client: AsyncHedra) -> None:
        async with async_client.with_streaming_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GenerationsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generations_overload_5(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_method_generations_with_all_params_overload_5(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="speech_to_speech",
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_generations_overload_5(self, async_client: AsyncHedra) -> None:
        response = await async_client.with_raw_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_generations_overload_5(self, async_client: AsyncHedra) -> None:
        async with async_client.with_streaming_response.generations(
            ai_model_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            voice_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GenerationsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generations_overload_6(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_method_generations_with_all_params_overload_6(self, async_client: AsyncHedra) -> None:
        client = await async_client.generations(
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="voice_clone",
        )
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_generations_overload_6(self, async_client: AsyncHedra) -> None:
        response = await async_client.with_raw_response.generations(
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GenerationsResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_generations_overload_6(self, async_client: AsyncHedra) -> None:
        async with async_client.with_streaming_response.generations(
            audio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GenerationsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
