# Reference
## Requests
<details><summary><code>client.requests.<a href="src/hedra/requests/client.py">list</a>(...) -> RequestListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.requests.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.requests.<a href="src/hedra/requests/client.py">get</a>(...) -> ResultResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.requests.get(
    request_id="request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.requests.<a href="src/hedra/requests/client.py">get_status</a>(...) -> StatusResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.requests.get_status(
    request_id="request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.requests.<a href="src/hedra/requests/client.py">list_request_logs</a>(...) -> RequestLogListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.requests.list_request_logs(
    request_id="request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.requests.<a href="src/hedra/requests/client.py">stream</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.requests.stream(
    request_id="request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Models
<details><summary><code>client.models.<a href="src/hedra/models/client.py">list</a>(...) -> ModelListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.models.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/hedra/models/client.py">get</a>(...) -> ModelDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.models.get(
    model="model",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/hedra/models/client.py">list_model_requests</a>(...) -> RequestListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.models.list_model_requests(
    model="model",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/hedra/models/client.py">list_voices</a>(...) -> VoiceListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Voices this model accepts — scoped to the model's voice provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.models.list_voices(
    model="model",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/hedra/models/client.py">get_openapi</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A standalone one-operation OpenAPI spec for this model's submit call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.models.get_openapi(
    model="model",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/hedra/models/client.py">estimate</a>(...) -> EstimateResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.models.estimate(
    model="model",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Keys
<details><summary><code>client.keys.<a href="src/hedra/keys/client.py">list</a>(...) -> KeyListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.keys.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.<a href="src/hedra/keys/client.py">create</a>(...) -> KeyCreateResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.keys.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.List[ApiKeyScope]]` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[ApiKeyKind]` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.<a href="src/hedra/keys/client.py">rotate</a>(...) -> KeyRotateResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.keys.rotate(
    key_id="key_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**grace_period_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.<a href="src/hedra/keys/client.py">revoke</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.keys.revoke(
    key_id="key_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tokens
<details><summary><code>client.tokens.<a href="src/hedra/tokens/client.py">create</a>(...) -> TokenCreateResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.tokens.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ttl_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.List[ApiKeyScope]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/hedra/files/client.py">upload</a>(...) -> FileUploadResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.files.upload(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Billing
<details><summary><code>client.billing.<a href="src/hedra/billing/client.py">get_balance</a>() -> BalanceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.billing.get_balance()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing.<a href="src/hedra/billing/client.py">get_usage</a>(...) -> UsageResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.billing.get_usage()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[UsageGroupBy]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/hedra/webhooks/client.py">get_public_key</a>() -> WebhookPublicKey</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.webhooks.get_public_key()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/hedra/webhooks/client.py">get_default</a>() -> WebhookDefaultConfig</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.webhooks.get_default()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/hedra/webhooks/client.py">put_default</a>(...) -> WebhookDefaultConfig</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.webhooks.put_default(
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/hedra/webhooks/client.py">delete_default</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.webhooks.delete_default()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/hedra/webhooks/client.py">test_default</a>() -> WebhookTestResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.webhooks.test_default()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/hedra/webhooks/client.py">list_deliveries</a>(...) -> WebhookDeliveryListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.webhooks.list_deliveries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/hedra/webhooks/client.py">redeliver</a>(...) -> WebhookDeliverySummary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replay a finished delivery: reset it to PENDING and re-fire the signed POST.

404 if the delivery isn't visible to the caller; 409 if a delivery for the
request is still in flight (a replay must not stack on it). The delivery is
re-validated (SSRF) and re-signed at send time, and the receiver dedupes on
``X-Hedra-Webhook-Id``, so a replay is safe.

The webhook id is stable across the original and every replay, so a receiver
that dedupes on it will ignore a replay of an event it already recorded —
redeliver only helps events the receiver never successfully processed (e.g. it
was down when the original fired).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.webhooks.redeliver(
    request_id="request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Log drains
<details><summary><code>client.log_drains.<a href="src/hedra/log_drains/client.py">list_log_drains</a>() -> LogDrainListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.log_drains.list_log_drains()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.log_drains.<a href="src/hedra/log_drains/client.py">create_log_drain</a>(...) -> LogDrainConfig</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.log_drains.create_log_drain(
    name="name",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[LogDrainFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**batch_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.log_drains.<a href="src/hedra/log_drains/client.py">get_log_drain</a>(...) -> LogDrainConfig</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.log_drains.get_log_drain(
    drain_id="drain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**drain_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.log_drains.<a href="src/hedra/log_drains/client.py">delete_log_drain</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.log_drains.delete_log_drain(
    drain_id="drain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**drain_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.log_drains.<a href="src/hedra/log_drains/client.py">update_log_drain</a>(...) -> LogDrainConfig</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.log_drains.update_log_drain(
    drain_id="drain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**drain_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[LogDrainFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**batch_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.log_drains.<a href="src/hedra/log_drains/client.py">test_log_drain</a>(...) -> LogDrainTestResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.log_drains.test_log_drain(
    drain_id="drain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**drain_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Queue
<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_dreamina31</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputDreamina31
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_dreamina31(
    input=GenerationInputDreamina31(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputDreamina31` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_elevenlabs_flash_multilingual_v2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputElevenlabsFlashMultilingualV2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_elevenlabs_flash_multilingual_v2(
    input=GenerationInputElevenlabsFlashMultilingualV2(
        text="text",
        voice_id="voice_id",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputElevenlabsFlashMultilingualV2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_elevenlabs_flash_v2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputElevenlabsFlashV2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_elevenlabs_flash_v2(
    input=GenerationInputElevenlabsFlashV2(
        text="text",
        voice_id="voice_id",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputElevenlabsFlashV2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_elevenlabs_multilingual_v2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputElevenlabsMultilingualV2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_elevenlabs_multilingual_v2(
    input=GenerationInputElevenlabsMultilingualV2(
        text="text",
        voice_id="voice_id",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputElevenlabsMultilingualV2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_elevenlabs_v3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputElevenlabsV3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_elevenlabs_v3(
    input=GenerationInputElevenlabsV3(
        text="text",
        voice_id="voice_id",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputElevenlabsV3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_elevenlabs_v3331</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputElevenlabsV3331
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_elevenlabs_v3331(
    input=GenerationInputElevenlabsV3331(
        text="text",
        voice_id="voice_id",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputElevenlabsV3331` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_flux11pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputFlux11Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_flux11pro(
    input=GenerationInputFlux11Pro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputFlux11Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_flux11ultra</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputFlux11Ultra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_flux11ultra(
    input=GenerationInputFlux11Ultra(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputFlux11Ultra` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_flux_dev</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputFluxDev
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_flux_dev(
    input=GenerationInputFluxDev(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputFluxDev` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_flux_kontext_max</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`flux-kontext-max` is a model family; the inputs present select the variant:
- prompt + image -> `flux-kontext-max-i2i`
- prompt only -> `flux-kontext-max-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputFluxKontextMax
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_flux_kontext_max(
    input=GenerationInputFluxKontextMax(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputFluxKontextMax` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_flux_kontext_pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`flux-kontext-pro` is a model family; the inputs present select the variant:
- prompt + image -> `flux-kontext-pro-i2i`
- prompt only -> `flux-kontext-pro-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputFluxKontextPro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_flux_kontext_pro(
    input=GenerationInputFluxKontextPro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputFluxKontextPro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_flux2flex</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`flux2-flex` is a model family; the inputs present select the variant:
- prompt + image -> `flux2-flex-i2i`
- prompt only -> `flux2-flex-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputFlux2Flex
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_flux2flex(
    input=GenerationInputFlux2Flex(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputFlux2Flex` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_flux2klein9b</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`flux2-klein-9b` is a model family; the inputs present select the variant:
- prompt + image -> `flux2-klein-9b-i2i`
- prompt only -> `flux2-klein-9b-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputFlux2Klein9B
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_flux2klein9b(
    input=GenerationInputFlux2Klein9B(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputFlux2Klein9B` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_flux2max</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`flux2-max` is a model family; the inputs present select the variant:
- prompt + image -> `flux2-max-i2i`
- prompt only -> `flux2-max-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputFlux2Max
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_flux2max(
    input=GenerationInputFlux2Max(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputFlux2Max` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_flux2pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`flux2-pro` is a model family; the inputs present select the variant:
- prompt + image -> `flux2-pro-i2i`
- prompt only -> `flux2-pro-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputFlux2Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_flux2pro(
    input=GenerationInputFlux2Pro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputFlux2Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_gpt_image15</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`gpt-image-15` is a model family; the inputs present select the variant:
- prompt + image -> `gpt-image-15-i2i`
- prompt only -> `gpt-image-15-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputGptImage15
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_gpt_image15(
    input=GenerationInputGptImage15(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputGptImage15` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_gpt_image2high</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`gpt-image-2-high` is a model family; the inputs present select the variant:
- prompt + image -> `gpt-image-2-high-i2i`
- prompt only -> `gpt-image-2-high-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputGptImage2High
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_gpt_image2high(
    input=GenerationInputGptImage2High(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputGptImage2High` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_gpt_image2low</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`gpt-image-2-low` is a model family; the inputs present select the variant:
- prompt + image -> `gpt-image-2-low-i2i`
- prompt only -> `gpt-image-2-low-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputGptImage2Low
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_gpt_image2low(
    input=GenerationInputGptImage2Low(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputGptImage2Low` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_gpt_image2medium</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`gpt-image-2-medium` is a model family; the inputs present select the variant:
- prompt + image -> `gpt-image-2-medium-i2i`
- prompt only -> `gpt-image-2-medium-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputGptImage2Medium
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_gpt_image2medium(
    input=GenerationInputGptImage2Medium(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputGptImage2Medium` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_grok_imagine</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`grok-imagine` is a model family; the inputs present select the variant:
- prompt + image -> `grok-imagine-i2i`
- prompt only -> `grok-imagine-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputGrokImagine
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_grok_imagine(
    input=GenerationInputGrokImagine(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputGrokImagine` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_grok_video</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`grok-video` is a model family; the inputs present select the variant:
- prompt + image -> `grok-video-i2v`
- prompt only -> `grok-video-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputGrokVideo
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_grok_video(
    input=GenerationInputGrokVideo(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputGrokVideo` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_happy_horse</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`happy-horse` is a model family; the inputs present select the variant:
- prompt + image -> `happy-horse-i2v`
- prompt only -> `happy-horse-ir2v`
- prompt only -> `happy-horse-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputHappyHorse
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_happy_horse(
    input=GenerationInputHappyHorse(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputHappyHorse` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_hedra_avatar</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputHedraAvatar, GenerationInputHedraAvatarImage_Url, GenerationInputHedraAvatarAudio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_hedra_avatar(
    input=GenerationInputHedraAvatar(
        prompt="prompt",
        image=GenerationInputHedraAvatarImage_Url(
            url="url",
        ),
        audio=GenerationInputHedraAvatarAudio_Url(
            url="url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputHedraAvatar` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_hedra_avatar_staging</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputHedraAvatarStaging, GenerationInputHedraAvatarStagingImage_Url, GenerationInputHedraAvatarStagingAudio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_hedra_avatar_staging(
    input=GenerationInputHedraAvatarStaging(
        prompt="prompt",
        image=GenerationInputHedraAvatarStagingImage_Url(
            url="url",
        ),
        audio=GenerationInputHedraAvatarStagingAudio_Url(
            url="url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputHedraAvatarStaging` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_hedra_character3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputHedraCharacter3, GenerationInputHedraCharacter3Image_Url, GenerationInputHedraCharacter3Audio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_hedra_character3(
    input=GenerationInputHedraCharacter3(
        prompt="prompt",
        image=GenerationInputHedraCharacter3Image_Url(
            url="url",
        ),
        audio=GenerationInputHedraCharacter3Audio_Url(
            url="url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputHedraCharacter3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_hedra_omnia</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputHedraOmnia, GenerationInputHedraOmniaImage_Url, GenerationInputHedraOmniaAudio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_hedra_omnia(
    input=GenerationInputHedraOmnia(
        prompt="prompt",
        image=GenerationInputHedraOmniaImage_Url(
            url="url",
        ),
        audio=GenerationInputHedraOmniaAudio_Url(
            url="url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputHedraOmnia` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_ideogram_v2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputIdeogramV2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_ideogram_v2(
    input=GenerationInputIdeogramV2(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputIdeogramV2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_imagen3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputImagen3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_imagen3(
    input=GenerationInputImagen3(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputImagen3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_imagen4</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputImagen4
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_imagen4(
    input=GenerationInputImagen4(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputImagen4` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling16</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`kling-16` is a model family; the inputs present select the variant:
- prompt + image -> `kling-16-i2v`
- prompt only -> `kling-16-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKling16
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling16(
    input=GenerationInputKling16(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKling16` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling21master</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`kling-21-master` is a model family; the inputs present select the variant:
- prompt + image -> `kling-21-master-i2v`
- prompt only -> `kling-21-master-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKling21Master
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling21master(
    input=GenerationInputKling21Master(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKling21Master` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling21pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`kling-21-pro` is a model family; the inputs present select the variant:
- prompt + image -> `kling-21-pro-i2v`
- prompt only -> `kling-21-pro-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKling21Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling21pro(
    input=GenerationInputKling21Pro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKling21Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling25turbo</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`kling-25-turbo` is a model family; the inputs present select the variant:
- prompt + image -> `kling-25-turbo-i2v`
- prompt only -> `kling-25-turbo-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKling25Turbo
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling25turbo(
    input=GenerationInputKling25Turbo(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKling25Turbo` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling26pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`kling-26-pro` is a model family; the inputs present select the variant:
- prompt + image -> `kling-26-pro-i2v`
- prompt only -> `kling-26-pro-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKling26Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling26pro(
    input=GenerationInputKling26Pro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKling26Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling_ai_avatar_v2pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKlingAiAvatarV2Pro, GenerationInputKlingAiAvatarV2ProImage_Url, GenerationInputKlingAiAvatarV2ProAudio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling_ai_avatar_v2pro(
    input=GenerationInputKlingAiAvatarV2Pro(
        prompt="prompt",
        image=GenerationInputKlingAiAvatarV2ProImage_Url(
            url="url",
        ),
        audio=GenerationInputKlingAiAvatarV2ProAudio_Url(
            url="url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKlingAiAvatarV2Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling_ai_avatar_v2standard</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKlingAiAvatarV2Standard, GenerationInputKlingAiAvatarV2StandardImage_Url, GenerationInputKlingAiAvatarV2StandardAudio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling_ai_avatar_v2standard(
    input=GenerationInputKlingAiAvatarV2Standard(
        prompt="prompt",
        image=GenerationInputKlingAiAvatarV2StandardImage_Url(
            url="url",
        ),
        audio=GenerationInputKlingAiAvatarV2StandardAudio_Url(
            url="url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKlingAiAvatarV2Standard` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling_o1</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`kling-o1` is a model family; the inputs present select the variant:
- prompt + image -> `kling-o1-i2v`
- prompt + image + end_image -> `kling-o1-ie2v`
- prompt + images -> `kling-o1-ir2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKlingO1
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling_o1(
    input=GenerationInputKlingO1(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKlingO1` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling_o3pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`kling-o3-pro` is a model family; the inputs present select the variant:
- prompt + image -> `kling-o3-pro-i2v`
- prompt + image + end_image -> `kling-o3-pro-ie2v`
- prompt + images -> `kling-o3-pro-ir2v`
- prompt only -> `kling-o3-pro-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKlingO3Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling_o3pro(
    input=GenerationInputKlingO3Pro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKlingO3Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling_o3standard</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`kling-o3-standard` is a model family; the inputs present select the variant:
- prompt + image -> `kling-o3-standard-i2v`
- prompt + image + end_image -> `kling-o3-standard-ie2v`
- prompt + images -> `kling-o3-standard-ir2v`
- prompt only -> `kling-o3-standard-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKlingO3Standard
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling_o3standard(
    input=GenerationInputKlingO3Standard(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKlingO3Standard` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling_v3pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`kling-v3-pro` is a model family; the inputs present select the variant:
- prompt + image -> `kling-v3-pro-i2v`
- prompt + image + end_image -> `kling-v3-pro-ie2v`
- prompt only -> `kling-v3-pro-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKlingV3Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling_v3pro(
    input=GenerationInputKlingV3Pro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKlingV3Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_kling_v3standard</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`kling-v3-standard` is a model family; the inputs present select the variant:
- prompt + image -> `kling-v3-standard-i2v`
- prompt + image + end_image -> `kling-v3-standard-ie2v`
- prompt only -> `kling-v3-standard-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputKlingV3Standard
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_kling_v3standard(
    input=GenerationInputKlingV3Standard(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputKlingV3Standard` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_minimax_hailuo02pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`minimax-hailuo-02-pro` is a model family; the inputs present select the variant:
- prompt + image -> `minimax-hailuo-02-pro-i2v`
- prompt only -> `minimax-hailuo-02-pro-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputMinimaxHailuo02Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_minimax_hailuo02pro(
    input=GenerationInputMinimaxHailuo02Pro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputMinimaxHailuo02Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_minimax_hailuo02standard</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`minimax-hailuo-02-standard` is a model family; the inputs present select the variant:
- prompt + image -> `minimax-hailuo-02-standard-i2v`
- prompt only -> `minimax-hailuo-02-standard-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputMinimaxHailuo02Standard
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_minimax_hailuo02standard(
    input=GenerationInputMinimaxHailuo02Standard(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputMinimaxHailuo02Standard` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_minimax_hailuo23fast_pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputMinimaxHailuo23FastPro, GenerationInputMinimaxHailuo23FastProImage_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_minimax_hailuo23fast_pro(
    input=GenerationInputMinimaxHailuo23FastPro(
        prompt="prompt",
        image=GenerationInputMinimaxHailuo23FastProImage_Url(
            url="url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputMinimaxHailuo23FastPro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_minimax_hailuo23fast_standard</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputMinimaxHailuo23FastStandard, GenerationInputMinimaxHailuo23FastStandardImage_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_minimax_hailuo23fast_standard(
    input=GenerationInputMinimaxHailuo23FastStandard(
        prompt="prompt",
        image=GenerationInputMinimaxHailuo23FastStandardImage_Url(
            url="url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputMinimaxHailuo23FastStandard` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_minimax_hailuo23pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`minimax-hailuo-23-pro` is a model family; the inputs present select the variant:
- prompt + image -> `minimax-hailuo-23-pro-i2v`
- prompt only -> `minimax-hailuo-23-pro-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputMinimaxHailuo23Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_minimax_hailuo23pro(
    input=GenerationInputMinimaxHailuo23Pro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputMinimaxHailuo23Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_minimax_hailuo23standard</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`minimax-hailuo-23-standard` is a model family; the inputs present select the variant:
- prompt + image -> `minimax-hailuo-23-standard-i2v`
- prompt only -> `minimax-hailuo-23-standard-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputMinimaxHailuo23Standard
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_minimax_hailuo23standard(
    input=GenerationInputMinimaxHailuo23Standard(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputMinimaxHailuo23Standard` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_minimax_speech25hd_preview</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputMinimaxSpeech25HdPreview
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_minimax_speech25hd_preview(
    input=GenerationInputMinimaxSpeech25HdPreview(
        text="text",
        voice_id="voice_id",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputMinimaxSpeech25HdPreview` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_minimax_speech25turbo_preview</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputMinimaxSpeech25TurboPreview
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_minimax_speech25turbo_preview(
    input=GenerationInputMinimaxSpeech25TurboPreview(
        text="text",
        voice_id="voice_id",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputMinimaxSpeech25TurboPreview` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_nano_banana</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`nano-banana` is a model family; the inputs present select the variant:
- prompt only -> `nano-banana`
- prompt + image -> `nano-banana-i2i`
- prompt only -> `nano-banana-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputNanoBanana
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_nano_banana(
    input=GenerationInputNanoBanana(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputNanoBanana` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_nano_banana2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputNanoBanana2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_nano_banana2(
    input=GenerationInputNanoBanana2(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputNanoBanana2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_nano_banana_pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`nano-banana-pro` is a model family; the inputs present select the variant:
- prompt only -> `nano-banana-pro`
- prompt + image -> `nano-banana-pro-i2i`
- prompt only -> `nano-banana-pro-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputNanoBananaPro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_nano_banana_pro(
    input=GenerationInputNanoBananaPro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputNanoBananaPro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_omnihuman15</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputOmnihuman15, GenerationInputOmnihuman15Image_Url, GenerationInputOmnihuman15Audio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_omnihuman15(
    input=GenerationInputOmnihuman15(
        prompt="prompt",
        image=GenerationInputOmnihuman15Image_Url(
            url="url",
        ),
        audio=GenerationInputOmnihuman15Audio_Url(
            url="url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputOmnihuman15` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_recraft_v3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputRecraftV3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_recraft_v3(
    input=GenerationInputRecraftV3(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputRecraftV3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_sana</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputSana
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_sana(
    input=GenerationInputSana(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputSana` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_seedance15pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputSeedance15Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_seedance15pro(
    input=GenerationInputSeedance15Pro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputSeedance15Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_seedance20</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputSeedance20
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_seedance20(
    input=GenerationInputSeedance20(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputSeedance20` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_seedance20fast</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputSeedance20Fast
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_seedance20fast(
    input=GenerationInputSeedance20Fast(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputSeedance20Fast` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_seedance20mini</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputSeedance20Mini
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_seedance20mini(
    input=GenerationInputSeedance20Mini(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputSeedance20Mini` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_seedream40</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`seedream-40` is a model family; the inputs present select the variant:
- prompt + image -> `seedream-40-i2i`
- prompt only -> `seedream-40-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputSeedream40
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_seedream40(
    input=GenerationInputSeedream40(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputSeedream40` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_seedream45</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`seedream-45` is a model family; the inputs present select the variant:
- prompt + image -> `seedream-45-i2i`
- prompt only -> `seedream-45-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputSeedream45
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_seedream45(
    input=GenerationInputSeedream45(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputSeedream45` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_seedream50lite</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`seedream-50-lite` is a model family; the inputs present select the variant:
- prompt + image -> `seedream-50-lite-i2i`
- prompt only -> `seedream-50-lite-t2i`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputSeedream50Lite
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_seedream50lite(
    input=GenerationInputSeedream50Lite(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputSeedream50Lite` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_sonic</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputSonic
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_sonic(
    input=GenerationInputSonic(
        text="text",
        voice_id="voice_id",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputSonic` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_sora2pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`sora-2-pro` is a model family; the inputs present select the variant:
- prompt + image -> `sora-2-pro-i2v`
- prompt only -> `sora-2-pro-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputSora2Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_sora2pro(
    input=GenerationInputSora2Pro(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputSora2Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_veed_fabric10</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputVeedFabric10, GenerationInputVeedFabric10Image_Url, GenerationInputVeedFabric10Audio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_veed_fabric10(
    input=GenerationInputVeedFabric10(
        prompt="prompt",
        image=GenerationInputVeedFabric10Image_Url(
            url="url",
        ),
        audio=GenerationInputVeedFabric10Audio_Url(
            url="url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputVeedFabric10` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_veed_fabric10fast</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputVeedFabric10Fast, GenerationInputVeedFabric10FastImage_Url, GenerationInputVeedFabric10FastAudio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_veed_fabric10fast(
    input=GenerationInputVeedFabric10Fast(
        prompt="prompt",
        image=GenerationInputVeedFabric10FastImage_Url(
            url="url",
        ),
        audio=GenerationInputVeedFabric10FastAudio_Url(
            url="url",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputVeedFabric10Fast` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_veo2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`veo-2` is a model family; the inputs present select the variant:
- prompt + image -> `veo-2-i2v`
- prompt only -> `veo-2-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputVeo2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_veo2(
    input=GenerationInputVeo2(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputVeo2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_veo3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`veo-3` is a model family; the inputs present select the variant:
- prompt + image -> `veo-3-i2v`
- prompt only -> `veo-3-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputVeo3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_veo3(
    input=GenerationInputVeo3(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputVeo3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_veo3fast</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.

`veo-3-fast` is a model family; the inputs present select the variant:
- prompt + image -> `veo-3-fast-i2v`
- prompt only -> `veo-3-fast-t2v`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputVeo3Fast
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_veo3fast(
    input=GenerationInputVeo3Fast(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputVeo3Fast` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_veo31</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputVeo31
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_veo31(
    input=GenerationInputVeo31(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputVeo31` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit_veo31fast</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous generation and returns `202` with a request id. Fetch the result at `GET /v3/requests/{request_id}` — each item in its `outputs[]` follows the `GenerationOutput` schema — or track progress via `GET /v3/requests/{request_id}/status` / the SSE stream at `GET /v3/requests/{request_id}/stream`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerationInputVeo31Fast
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.queue.submit_veo31fast(
    input=GenerationInputVeo31Fast(
        prompt="prompt",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `GenerationInputVeo31Fast` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate generation.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Requested queue priority (per-tier priority is planned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

