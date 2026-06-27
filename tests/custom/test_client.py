"""Generated-client request tests using a mock httpx transport.

These exercise the real Hedra client end-to-end (auth, base URL, query encoding)
without hitting the network. They live under tests/custom/ so Fern preserves them.
"""

import os
import subprocess
import sys

import httpx
import pytest

from hedra import Hedra


def _client_with_capture(captured: dict, body: dict, *, api_key: str = "test-key") -> Hedra:
    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(200, json=body)

    return Hedra(api_key=api_key, httpx_client=httpx.Client(transport=httpx.MockTransport(handler)))


def test_api_key_header_and_base_url() -> None:
    captured: dict = {}
    client = _client_with_capture(captured, {"remaining": 1, "expiring": 0, "used": 0})

    client.get_credits()

    request = captured["request"]
    assert request.headers["X-API-Key"] == "test-key"
    assert str(request.url) == "https://api.hedra.com/web-app/public/billing/credits"


def test_list_generations_flattens_limit_and_offset_into_query() -> None:
    captured: dict = {}
    client = _client_with_capture(captured, {"page_info": {"limit": 5, "offset": 10}, "data": []})

    client.list_generations(limit=5, offset=10)

    url = captured["request"].url
    # Flattened scalar query params — NOT a nested paging_params object.
    assert url.params.get("limit") == "5"
    assert url.params.get("offset") == "10"
    assert "paging_params" not in str(url)


def test_missing_api_key_raises() -> None:
    # No api_key passed and HEDRA_API_KEY not set in this process.
    os.environ.pop("HEDRA_API_KEY", None)
    with pytest.raises(Exception) as exc_info:
        Hedra(api_key=None)
    assert "HEDRA_API_KEY" in str(exc_info.value)


def test_hedra_api_key_env_fallback() -> None:
    script = (
        "from hedra import Hedra\n"
        "c = Hedra()\n"
        "assert c._client_wrapper.api_key == 'env-key'\n"
        "print('ok')\n"
    )
    env = {**os.environ, "HEDRA_API_KEY": "env-key"}
    result = subprocess.run([sys.executable, "-c", script], env=env, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert "ok" in result.stdout


def test_hedra_api_key_env_read_at_construction_not_import(monkeypatch: pytest.MonkeyPatch) -> None:
    # Regression: the env var must be read when the client is constructed, not
    # captured as an import-time default. Mirrors `import Hedra; load_dotenv(); Hedra()`.
    monkeypatch.setenv("HEDRA_API_KEY", "set-after-import")
    client = Hedra()
    assert client._client_wrapper.api_key == "set-after-import"


def test_parse_retry_after_ms_header() -> None:
    # Regression: retry-after-ms is a string; it must not be compared to int 0.
    from hedra.core.http_client import _parse_retry_after

    assert _parse_retry_after(httpx.Headers({"retry-after-ms": "2500"})) == 2.5
    assert _parse_retry_after(httpx.Headers({"retry-after-ms": "0"})) == 0
    assert _parse_retry_after(httpx.Headers({"retry-after": "3"})) == 3
