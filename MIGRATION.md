# Migration guide

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
