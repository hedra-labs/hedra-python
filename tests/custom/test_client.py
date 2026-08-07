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
from hedra.types import InputFluxDev


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


def test_job_submit_posts_to_model_path() -> None:
    captured: dict = {}
    client = _client_with_capture(
        captured,
        {
            "job_id": "job_123",
            "model": "flux-dev",
            "status": "IN_QUEUE",
            "status_url": "https://api.hedra.com/v3/jobs/job_123/status",
            "result_url": "https://api.hedra.com/v3/jobs/job_123",
        },
    )

    client.jobs.submit_flux_dev(
        input=InputFluxDev(prompt="a fox", aspect_ratio="1:1", resolution="1080p")
    )

    request = captured["request"]
    assert request.method == "POST"
    assert str(request.url) == "https://api.hedra.com/v3/models/flux-dev"


def test_jobs_list_sends_cursor_pagination_params() -> None:
    captured: dict = {}
    client = _client_with_capture(captured, {"data": [], "next_cursor": None})

    pager = client.jobs.list(limit=5)
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


def test_parse_retry_after_header() -> None:
    # Only the `retry-after` header is asserted here. `retry-after-ms` is knowingly
    # broken upstream in fern-python-sdk: it compares the header string to an int,
    # and the resulting TypeError is swallowed by a bare `except`, so the header is
    # ignored and parsing falls through to `retry-after` below. We used to carry a
    # one-line fix for that by freezing http_client.py in .fernignore, but the freeze
    # cost a hand-port on every generator bump and the Hedra API does not send
    # `retry-after-ms`. If that changes, fix it upstream rather than re-freezing.
    from hedra.core.http_client import _parse_retry_after

    assert _parse_retry_after(httpx.Headers({"retry-after": "3"})) == 3
    assert _parse_retry_after(httpx.Headers({})) is None


def _client_capturing_timeout(captured: dict, **client_kwargs: object) -> Hedra:
    def handler(request: httpx.Request) -> httpx.Response:
        # httpx records the timeout it resolved for the request here.
        captured["timeout"] = request.extensions.get("timeout")
        return httpx.Response(200, json={"data": [], "next_cursor": None})

    transport = httpx.MockTransport(handler)
    return Hedra(api_key="test-key", httpx_client=httpx.Client(transport=transport, **client_kwargs))  # type: ignore[arg-type]


def test_request_options_timeout_is_honoured() -> None:
    # Regression: `request_options={"timeout": N}` is the documented, preferred
    # option. src/hedra/core/http_client.py is .fernignore'd, and the frozen
    # 5.15.0 copy never read this key -- it type-checked, was documented, and was
    # silently dropped at runtime (the request went out on httpx's own default).
    captured: dict = {}
    client = _client_capturing_timeout(captured)

    client.models.list(request_options={"timeout": 30})

    assert captured["timeout"]["read"] == 30


def test_request_options_timeout_takes_precedence_over_timeout_in_seconds() -> None:
    # Both are in seconds; `timeout` wins. Mirrors the generated
    # tests/utils/test_http_client.py assertions so this stays pinned on main
    # even before the tree regenerates.
    captured: dict = {}
    client = _client_capturing_timeout(captured)

    client.models.list(request_options={"timeout": 30, "timeout_in_seconds": 45})

    assert captured["timeout"]["read"] == 30


def test_deprecated_timeout_in_seconds_still_works() -> None:
    captured: dict = {}
    client = _client_capturing_timeout(captured)

    client.models.list(request_options={"timeout_in_seconds": 45})

    assert captured["timeout"]["read"] == 45


def test_caller_supplied_httpx_client_timeout_is_not_discarded() -> None:
    # Cross-generator invariant. When the caller brings their own httpx_client and
    # sets no explicit timeout, their configured timeout must reach httpx.
    # base_client.py reaches this result two different ways depending on the
    # generator -- 5.15.0 passes httpx_client.timeout.read through, while 5.26.0+
    # passes None and relies on http_client.py mapping it to
    # httpx.USE_CLIENT_DEFAULT. Pin the observable behaviour so the regeneration
    # cannot silently turn this into "no timeout at all".
    captured: dict = {}
    client = _client_capturing_timeout(captured, timeout=12.5)

    client.models.list()

    assert captured["timeout"]["read"] == 12.5
