# Reference
<details><summary><code>client.<a href="src/hedra/client.py">ping_ping_get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra

client = Hedra(
    api_key="YOUR_API_KEY",
)
client.ping_ping_get()

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

## Voice
<details><summary><code>client.voice.<a href="src/hedra/voice/client.py">api_access_get_voices</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra

client = Hedra(
    api_key="YOUR_API_KEY",
)
client.voice.api_access_get_voices()

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

## Audio
<details><summary><code>client.audio.<a href="src/hedra/audio/client.py">api_access_upload_audio</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra

client = Hedra(
    api_key="YOUR_API_KEY",
)
client.audio.api_access_upload_audio()

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

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**content_length:** `typing.Optional[int]` 
    
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

## Portait
<details><summary><code>client.portait.<a href="src/hedra/portait/client.py">api_access_upload_image</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra

client = Hedra(
    api_key="YOUR_API_KEY",
)
client.portait.api_access_upload_image()

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

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**aspect_ratio:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**content_length:** `typing.Optional[int]` 
    
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

## Characters
<details><summary><code>client.characters.<a href="src/hedra/characters/client.py">api_access_initialize_talking_head_avatar</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra

client = Hedra(
    api_key="YOUR_API_KEY",
)
client.characters.api_access_initialize_talking_head_avatar()

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

**content_length:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — text to convert to audio. Ignored if audio_source is not tts
    
</dd>
</dl>

<dl>
<dd>

**voice_id:** `typing.Optional[str]` — Voice ID
    
</dd>
</dl>

<dl>
<dd>

**voice_url:** `typing.Optional[str]` — URL of audio uploaded using the /v1/audio endpoint
    
</dd>
</dl>

<dl>
<dd>

**avatar_image:** `typing.Optional[str]` — URL of image uploaded via /v1/portrait
    
</dd>
</dl>

<dl>
<dd>

**aspect_ratio:** `typing.Optional[ApiGenerateTalkingAvatarRequestBodyAspectRatio]` — URL of audio uploaded using the /v1/audio endpoint
    
</dd>
</dl>

<dl>
<dd>

**audio_source:** `typing.Optional[ApiGenerateTalkingAvatarRequestBodyAudioSource]` — `tts` for text to speech or `audio`
    
</dd>
</dl>

<dl>
<dd>

**avatar_image_input:** `typing.Optional[AvatarImageInput]` — Image metadata
    
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

## Projects
<details><summary><code>client.projects.<a href="src/hedra/projects/client.py">api_access_get_all_user_projects</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra

client = Hedra(
    api_key="YOUR_API_KEY",
)
client.projects.api_access_get_all_user_projects()

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

<details><summary><code>client.projects.<a href="src/hedra/projects/client.py">api_access_get_project</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra

client = Hedra(
    api_key="YOUR_API_KEY",
)
client.projects.api_access_get_project(
    project_id="project_id",
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

**project_id:** `str` 
    
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

<details><summary><code>client.projects.<a href="src/hedra/projects/client.py">api_access_delete_project</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra

client = Hedra(
    api_key="YOUR_API_KEY",
)
client.projects.api_access_delete_project(
    project_id="project_id",
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

**project_id:** `str` 
    
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

<details><summary><code>client.projects.<a href="src/hedra/projects/client.py">api_access_share_project</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hedra import Hedra

client = Hedra(
    api_key="YOUR_API_KEY",
)
client.projects.api_access_share_project(
    project_id="project_id",
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

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**shared:** `typing.Optional[bool]` 
    
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

