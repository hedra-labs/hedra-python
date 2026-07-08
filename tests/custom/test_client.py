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


def test_bearer_auth_header_and_base_url() -> None:
    captured: dict = {}
    client = _client_with_capture(captured, {"data": [], "next_cursor": None})

    client.models.list()

    request = captured["request"]
    assert request.headers["Authorization"] == "Bearer test-key"
    assert str(request.url) == "https://api.hedra.com/v3/models"


def test_queue_submit_posts_to_model_path() -> None:
    captured: dict = {}
    client = _client_with_capture(
        captured,
        {
            "request_id": "req_123",
            "model": "kling-o3-pro-i2v",
            "status": "IN_QUEUE",
            "status_url": "https://api.hedra.com/v3/requests/req_123/status",
            "response_url": "https://api.hedra.com/v3/requests/req_123",
        },
    )

    client.queue.submit(model="kling-o3-pro", input={"prompt": "a fox"})

    request = captured["request"]
    assert request.method == "POST"
    assert str(request.url) == "https://api.hedra.com/v3/queue/kling-o3-pro"


def test_requests_list_sends_cursor_pagination_params() -> None:
    captured: dict = {}
    client = _client_with_capture(captured, {"data": [], "next_cursor": None})

    pager = client.requests.list(limit=5)
    list(pager)  # drain the pager so the first page request fires

    url = captured["request"].url
    assert url.params.get("limit") == "5"


def test_missing_api_key_sends_no_authorization_header() -> None:
    # The v3 catalog endpoints are public; constructing without a key is valid
    # and simply sends unauthenticated requests.
    os.environ.pop("HEDRA_API_KEY", None)
    captured: dict = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(200, json={"data": [], "next_cursor": None})

    client = Hedra(api_key=None, httpx_client=httpx.Client(transport=httpx.MockTransport(handler)))
    client.models.list()

    assert "Authorization" not in captured["request"].headers


def test_hedra_api_key_env_fallback() -> None:
    script = (
        "from hedra import Hedra\n"
        "c = Hedra()\n"
        "assert c._client_wrapper._get_api_key() == 'env-key'\n"
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
    assert client._client_wrapper._get_api_key() == "set-after-import"


def test_parse_retry_after_ms_header() -> None:
    # Regression: retry-after-ms is a string; it must not be compared to int 0.
    from hedra.core.http_client import _parse_retry_after

    assert _parse_retry_after(httpx.Headers({"retry-after-ms": "2500"})) == 2.5
    assert _parse_retry_after(httpx.Headers({"retry-after-ms": "0"})) == 0
    assert _parse_retry_after(httpx.Headers({"retry-after": "3"})) == 3
