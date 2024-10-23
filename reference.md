# Reference
## Voice
<details><summary><code>client.voice.<a href="src/hedra/voice/client.py">get</a>()</code></summary>
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
client.voice.get()

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
<details><summary><code>client.audio.<a href="src/hedra/audio/client.py">upload_audio</a>(...)</code></summary>
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
client.audio.upload_audio()

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
<details><summary><code>client.portait.<a href="src/hedra/portait/client.py">upload_image</a>(...)</code></summary>
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
client.portait.upload_image()

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
<details><summary><code>client.characters.<a href="src/hedra/characters/client.py">initialize_talking_head_avatar</a>(...)</code></summary>
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
client.characters.initialize_talking_head_avatar()

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
<details><summary><code>client.projects.<a href="src/hedra/projects/client.py">get_all</a>()</code></summary>
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
client.projects.get_all()

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

<details><summary><code>client.projects.<a href="src/hedra/projects/client.py">get</a>(...)</code></summary>
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
client.projects.get(
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

<details><summary><code>client.projects.<a href="src/hedra/projects/client.py">delete</a>(...)</code></summary>
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
client.projects.delete(
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

<details><summary><code>client.projects.<a href="src/hedra/projects/client.py">share</a>(...)</code></summary>
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
client.projects.share(
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

