# Reference
## Queue
<details><summary><code>client.queue.<a href="src/hedra/queue/client.py">submit</a>(...) -> SubmitResponse</code></summary>
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

client.queue.submit(
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

**webhook:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` 
    
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

