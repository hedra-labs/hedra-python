# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .. import core
from ..core.request_options import RequestOptions
from ..types.upload_audio_response_body import UploadAudioResponseBody
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AudioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upload_audio(
        self,
        *,
        file: core.File,
        content_length: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadAudioResponseBody:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        content_length : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadAudioResponseBody
            Successful Response

        Examples
        --------
        from hedra import Hedra

        client = Hedra(
            api_key="YOUR_API_KEY",
        )
        client.audio.upload_audio()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/audio",
            method="POST",
            data={},
            files={
                "file": file,
            },
            headers={
                "content-length": str(content_length) if content_length is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    UploadAudioResponseBody,
                    parse_obj_as(
                        type_=UploadAudioResponseBody,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAudioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upload_audio(
        self,
        *,
        file: core.File,
        content_length: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadAudioResponseBody:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        content_length : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadAudioResponseBody
            Successful Response

        Examples
        --------
        import asyncio

        from hedra import AsyncHedra

        client = AsyncHedra(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.audio.upload_audio()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/audio",
            method="POST",
            data={},
            files={
                "file": file,
            },
            headers={
                "content-length": str(content_length) if content_length is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    UploadAudioResponseBody,
                    parse_obj_as(
                        type_=UploadAudioResponseBody,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
