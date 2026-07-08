# Migration guide

## 0.2.x → 0.3.0 (API v3)

`hedra-python` 0.3.0 retargets the SDK at **Hedra API v3** (`https://api.hedra.com/v3`),
the queue-based generation API. This is a breaking release. The PyPI package name
(`hedra-python`) and import name (`hedra`) are unchanged.

### What changed

**API surface.** The flat 0.2.x methods are replaced by resource groups:

| 0.2.x | 0.3.0 | Endpoint |
| --- | --- | --- |
| `client.generate_asset(...)` | `client.queue.submit(model=..., input={...})` | `POST /v3/queue/{model}` |
| `client.get_status(...)` | `client.requests.get_status(request_id)` | `GET /v3/requests/{id}/status` |
| `client.list_generations(...)` | `client.requests.list(...)` (cursor pager) | `GET /v3/requests` |
| — | `client.requests.get(request_id)` | `GET /v3/requests/{id}` |
| — | `client.requests.stream(request_id)` (SSE) | `GET /v3/requests/{id}/stream` |
| `client.list_models()` | `client.models.list(...)` | `GET /v3/models` |
| — | `client.models.get(model)` | `GET /v3/models/{model}` |
| `client.list_voices()` | `client.models.list_voices(model)` | `GET /v3/models/{model}/voices` |
| — | `client.models.estimate(model, input={...})` | `POST /v3/models/{model}/estimate` |
| — | `client.models.get_openapi(model)` | `GET /v3/models/{model}/openapi.json` |
| `client.create_asset(...)` + `client.upload_asset(...)` | `client.files.upload(file=...)` | `POST /v3/files` |
| `client.get_credits()` | — (v3 balance/usage endpoints are not live yet) | |
| — | `client.keys.create/list/rotate/revoke` | `/v3/keys*` |
| — | `client.tokens.create()` | `POST /v3/tokens` |
| — | `client.webhooks.get_public_key()` | `GET /v3/webhooks/public-key` |

Generation submits take the model id in the path and a schema-validated `input`
dict (per-model schemas: `client.models.get(model).input_schema` or
`GET /v3/models/{model}/openapi.json`). Statuses are `IN_QUEUE` → `IN_PROGRESS` →
`COMPLETED` | `FAILED`; a request's `outputs` is always an array.

**Auth.** `X-API-Key: sk_hedra_…` is replaced by standard
`Authorization: Bearer <key_id>:<secret>` (v3 API keys from the console).
`api_key=` and the `HEDRA_API_KEY` env fallback work as before — pass the
`<key_id>:<secret>` string.

**Environments.** `HedraEnvironment.PRODUCTION` (`https://api.hedra.com/v3`)
replaces `HedraEnvironment.DEFAULT`; use `base_url=` to point anywhere else.

**Pagination.** `client.requests.list()` returns a `SyncPager` /
`AsyncPager` that fetches cursor pages lazily as you iterate.


## 0.1.x (Stainless) → 0.2.0 (Fern)

`hedra-python` 0.2.0 is a ground-up regeneration of the SDK. It switches the code
generator from Stainless to [Fern](https://buildwithfern.com) **and** retargets the
library at Hedra's current public API. This is a breaking release.

The PyPI package name (`hedra-python`) and the import name (`hedra`) are unchanged:

```python
from hedra import Hedra, AsyncHedra
```

### What changed

**API surface.** The 0.1.x SDK targeted the legacy `mercury.dev.dream-ai.com` API,
which is no longer available. 0.2.0 targets `https://api.hedra.com/web-app/public`
(the spec published at <https://hedra.com/docs/openapi.json>). The old methods
(`client.characters.create`, `client.audio.create`, `client.portraits.create`,
`client.projects.*`, `client.voices.list`, `client.ping`) no longer exist.

**New methods** are flat on the client (no resource namespace):

| Method | Endpoint |
| --- | --- |
| `client.list_models()` | `GET /models` |
| `client.list_voices()` | `GET /voices` |
| `client.list_assets()` | `GET /assets` |
| `client.create_asset(...)` | `POST /assets` |
| `client.upload_asset(...)` | `POST /assets/{id}/upload` |
| `client.list_generations(...)` | `GET /generations` |
| `client.generate_asset(...)` | `POST /generations` |
| `client.get_status(...)` | `GET /generations/{generation_id}/status` |
| `client.get_credits()` | `GET /billing/credits` |

`async` equivalents are available on `AsyncHedra`.

**Auth** is unchanged in spirit — an `X-API-Key` header — and still reads the
`HEDRA_API_KEY` environment variable when `api_key` is not passed explicitly:

```python
from hedra import Hedra

client = Hedra(api_key="...")   # or set HEDRA_API_KEY and call Hedra()
```

**Paging.** `list_generations` takes flat `limit` / `offset` keyword arguments rather
than a nested paging object.

**Responses** are still Pydantic models. Errors raise subclasses of `hedra.core.ApiError`.

### Regenerating

The SDK is generated from `fern/` (OpenAPI spec + `fern/openapi/overrides.yml`).
Run the `fern` GitHub workflow (`workflow_dispatch`) to regenerate and open a PR, or
locally `fern generate --local --group local`. Hand-maintained files are protected by
`.fernignore`.
