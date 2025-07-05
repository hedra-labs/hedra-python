# Hedra

Types:

```python
from hedra.types import (
    GenerateImageRequest,
    GenerateIsolatedAudioRequest,
    GenerateSpeechToSpeechRequest,
    GenerateTextToSpeechRequest,
    GenerateVoiceCloneRequest,
    GeneratedVideoInputs,
    GenerationsResponse,
)
```

Methods:

- <code title="post /generations">client.<a href="./src/hedra/_client.py">generations</a>(\*\*<a href="src/hedra/types/client_generations_params.py">params</a>) -> <a href="./src/hedra/types/generations_response.py">GenerationsResponse</a></code>

# Models

Types:

```python
from hedra.types import ModelListResponse
```

Methods:

- <code title="get /models">client.models.<a href="./src/hedra/resources/models.py">list</a>() -> <a href="./src/hedra/types/model_list_response.py">ModelListResponse</a></code>

# Assets

Types:

```python
from hedra.types import Asset, AssetType, GeneratedVideo, AssetCreateResponse, AssetListResponse
```

Methods:

- <code title="post /assets">client.assets.<a href="./src/hedra/resources/assets.py">create</a>(\*\*<a href="src/hedra/types/asset_create_params.py">params</a>) -> <a href="./src/hedra/types/asset_create_response.py">AssetCreateResponse</a></code>
- <code title="get /assets">client.assets.<a href="./src/hedra/resources/assets.py">list</a>(\*\*<a href="src/hedra/types/asset_list_params.py">params</a>) -> <a href="./src/hedra/types/asset_list_response.py">AssetListResponse</a></code>
- <code title="post /assets/{id}/upload">client.assets.<a href="./src/hedra/resources/assets.py">upload</a>(id, \*\*<a href="src/hedra/types/asset_upload_params.py">params</a>) -> <a href="./src/hedra/types/asset.py">Asset</a></code>

# Client

Types:

```python
from hedra.types import (
    GenerationStatus,
    ClientListGenerationsResponse,
    ClientRetrieveGenerationStatusResponse,
)
```

Methods:

- <code title="get /generations">client.client.<a href="./src/hedra/resources/client.py">list_generations</a>(\*\*<a href="src/hedra/types/client_list_generations_params.py">params</a>) -> <a href="./src/hedra/types/client_list_generations_response.py">ClientListGenerationsResponse</a></code>
- <code title="get /generations/{generation_id}/status">client.client.<a href="./src/hedra/resources/client.py">retrieve_generation_status</a>(generation_id) -> <a href="./src/hedra/types/client_retrieve_generation_status_response.py">ClientRetrieveGenerationStatusResponse</a></code>

# Billing

Types:

```python
from hedra.types import BillingListCreditsResponse
```

Methods:

- <code title="get /billing/credits">client.billing.<a href="./src/hedra/resources/billing.py">list_credits</a>() -> <a href="./src/hedra/types/billing_list_credits_response.py">BillingListCreditsResponse</a></code>
