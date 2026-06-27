# Hand-maintained wrapper around the Fern-generated BaseHedra/AsyncBaseHedra.
# Listed in .fernignore so it survives regeneration (base_client.py regenerates).
#
# Customization: the API key is read from HEDRA_API_KEY at *construction* time
# rather than as an import-time default argument, so `load_dotenv(); Hedra()`
# works regardless of import order.

import os
import typing

import httpx

from .base_client import AsyncBaseHedra, BaseHedra
from .core.logging import LogConfig, Logger
from .environment import HedraEnvironment

__all__ = ["AsyncHedra", "Hedra"]


def _resolve_api_key(api_key: typing.Optional[str]) -> typing.Optional[str]:
    return api_key if api_key is not None else os.environ.get("HEDRA_API_KEY")


class Hedra(BaseHedra):
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: HedraEnvironment = HedraEnvironment.DEFAULT,
        api_key: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        super().__init__(
            base_url=base_url,
            environment=environment,
            api_key=_resolve_api_key(api_key),
            headers=headers,
            timeout=timeout,
            max_retries=max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
        )


class AsyncHedra(AsyncBaseHedra):
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: HedraEnvironment = HedraEnvironment.DEFAULT,
        api_key: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        super().__init__(
            base_url=base_url,
            environment=environment,
            api_key=_resolve_api_key(api_key),
            headers=headers,
            timeout=timeout,
            max_retries=max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
        )
