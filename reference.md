# Reference
<details><summary><code>client.<a href="src/hedra/client.py">list_models</a>(...) -> typing.List[AiModel]</code></summary>
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
    api_key="<value>",
    environment=HedraEnvironment.DEFAULT,
)

client.list_models()

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

**types:** `typing.Optional[typing.List[str]]` 
    
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

<details><summary><code>client.<a href="src/hedra/client.py">list_voices</a>() -> typing.List[Asset]</code></summary>
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
    api_key="<value>",
    environment=HedraEnvironment.DEFAULT,
)

client.list_voices()

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

<details><summary><code>client.<a href="src/hedra/client.py">list_assets</a>(...) -> typing.List[Asset]</code></summary>
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
    api_key="<value>",
    environment=HedraEnvironment.DEFAULT,
)

client.list_assets(
    type="text",
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

**type:** `AssetType` 
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/hedra/client.py">create_asset</a>(...) -> CreateAssetResponse</code></summary>
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
    api_key="<value>",
    environment=HedraEnvironment.DEFAULT,
)

client.create_asset(
    name="name",
    type="text",
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

**name:** `str` — Name of the asset. Default to user-provided file name.
    
</dd>
</dl>

<dl>
<dd>

**type:** `AssetType` — The type of the asset.
    
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

<details><summary><code>client.<a href="src/hedra/client.py">upload_asset</a>(...) -> Asset</code></summary>
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
    api_key="<value>",
    environment=HedraEnvironment.DEFAULT,
)

client.upload_asset(
    id="id",
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

**id:** `str` 
    
</dd>
</dl>

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

<details><summary><code>client.<a href="src/hedra/client.py">list_generations</a>(...) -> PagedResponseGeneration</code></summary>
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
    api_key="<value>",
    environment=HedraEnvironment.DEFAULT,
)

client.list_generations()

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

**type:** `typing.Optional[ListGenerationsRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_query:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**agent_thread_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items returned in the page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of records skipped.
    
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

<details><summary><code>client.<a href="src/hedra/client.py">generate_asset</a>(...) -> GenerateAssetResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra, GenerateAssetRequest_Video, GeneratedVideoInputs
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<value>",
    environment=HedraEnvironment.DEFAULT,
)

client.generate_asset(
    request=GenerateAssetRequest_Video(
        generated_video_inputs=GeneratedVideoInputs(
            text_prompt="text_prompt",
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

**request:** `GenerateAssetRequest` 
    
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

<details><summary><code>client.<a href="src/hedra/client.py">get_status</a>(...) -> GenerationStatusResponse</code></summary>
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
    api_key="<value>",
    environment=HedraEnvironment.DEFAULT,
)

client.get_status(
    generation_id="generation_id",
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

**generation_id:** `str` 
    
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

<details><summary><code>client.<a href="src/hedra/client.py">get_credits</a>() -> CreditBalance</code></summary>
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
    api_key="<value>",
    environment=HedraEnvironment.DEFAULT,
)

client.get_credits()

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

