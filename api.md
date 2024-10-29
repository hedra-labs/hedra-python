# Hedra

Types:

```python
from hedra.types import PingResponse
```

Methods:

- <code title="get /ping">client.<a href="./src/hedra/_client.py">ping</a>() -> <a href="./src/hedra/types/ping_response.py">object</a></code>

# Voices

Types:

```python
from hedra.types import VoiceListResponse
```

Methods:

- <code title="get /v1/voices">client.voices.<a href="./src/hedra/resources/voices.py">list</a>() -> <a href="./src/hedra/types/voice_list_response.py">VoiceListResponse</a></code>

# Audio

Types:

```python
from hedra.types import AudioCreateResponse
```

Methods:

- <code title="post /v1/audio">client.audio.<a href="./src/hedra/resources/audio.py">create</a>(\*\*<a href="src/hedra/types/audio_create_params.py">params</a>) -> <a href="./src/hedra/types/audio_create_response.py">AudioCreateResponse</a></code>

# Portraits

Types:

```python
from hedra.types import PortraitCreateResponse
```

Methods:

- <code title="post /v1/portrait">client.portraits.<a href="./src/hedra/resources/portraits.py">create</a>(\*\*<a href="src/hedra/types/portrait_create_params.py">params</a>) -> <a href="./src/hedra/types/portrait_create_response.py">PortraitCreateResponse</a></code>

# Characters

Types:

```python
from hedra.types import CharacterCreateResponse
```

Methods:

- <code title="post /v1/characters">client.characters.<a href="./src/hedra/resources/characters.py">create</a>(\*\*<a href="src/hedra/types/character_create_params.py">params</a>) -> <a href="./src/hedra/types/character_create_response.py">CharacterCreateResponse</a></code>

# Projects

Types:

```python
from hedra.types import (
    AvatarProjectItem,
    ProjectListResponse,
    ProjectDeleteResponse,
    ProjectSharingResponse,
)
```

Methods:

- <code title="get /v1/projects/{project_id}">client.projects.<a href="./src/hedra/resources/projects.py">retrieve</a>(project_id) -> <a href="./src/hedra/types/avatar_project_item.py">AvatarProjectItem</a></code>
- <code title="get /v1/projects">client.projects.<a href="./src/hedra/resources/projects.py">list</a>() -> <a href="./src/hedra/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /v1/projects/{project_id}">client.projects.<a href="./src/hedra/resources/projects.py">delete</a>(project_id) -> <a href="./src/hedra/types/project_delete_response.py">object</a></code>
- <code title="post /v1/projects/{project_id}/sharing">client.projects.<a href="./src/hedra/resources/projects.py">sharing</a>(project_id, \*\*<a href="src/hedra/types/project_sharing_params.py">params</a>) -> <a href="./src/hedra/types/project_sharing_response.py">object</a></code>
