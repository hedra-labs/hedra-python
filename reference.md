# Reference
## Jobs
<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">list</a>(...) -> JobListResponse</code></summary>
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

client.jobs.list()

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

**limit:** `typing.Optional[int]` — Maximum items per page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `next_cursor`; omit for the first page.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">get</a>(...) -> ResultResponse</code></summary>
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

client.jobs.get(
    job_id="job_id",
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

**job_id:** `str` — The job's id (`job_<uuid>`).
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">get_status</a>(...) -> StatusResponse</code></summary>
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

client.jobs.get_status(
    job_id="job_id",
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

**job_id:** `str` — The job's id (`job_<uuid>`).
    
</dd>
</dl>

<dl>
<dd>

**logs_after:** `typing.Optional[str]` — Tail this job's lifecycle events incrementally: returns only events newer than this cursor, plus `logs_next_cursor` to send on the next poll. Pass `start` to begin from the job's first event. Omit it and the response carries no events at all — the default polling shape is unchanged.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">list_job_logs</a>(...) -> JobLogListResponse</code></summary>
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

client.jobs.list_job_logs(
    job_id="job_id",
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

**job_id:** `str` — The job's id (`job_<uuid>`).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum items per page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `next_cursor`; omit for the first page.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">stream</a>(...) -> typing.Iterator[bytes]</code></summary>
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

client.jobs.stream(
    job_id="job_id",
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

**job_id:** `str` — The job's id (`job_<uuid>`).
    
</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[str]` — Resume after this event id — the standard SSE reconnect header; browsers' EventSource sends it automatically.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_creatify_aurora</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create high-fidelity speaking or singing avatar videos.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputCreatifyAurora, InputCreatifyAuroraStartImage_Url, InputCreatifyAuroraAudio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_creatify_aurora(
    input=InputCreatifyAurora(
        resolution="480p",
        start_image=InputCreatifyAuroraStartImage_Url(
            url="url",
        ),
        audio=InputCreatifyAuroraAudio_Url(
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

**input:** `InputCreatifyAurora` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_dreamina31</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Polished, print-ready stills when the brief is a finished image rather than a sketch.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputDreamina31
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_dreamina31(
    input=InputDreamina31(
        prompt="prompt",
        aspect_ratio="16:9",
        resolution="540p",
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

**input:** `InputDreamina31` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_audio_isolation</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Strip background noise from a recording, keeping the speech.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputElevenlabsAudioIsolation, InputElevenlabsAudioIsolationAudio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_elevenlabs_audio_isolation(
    input=InputElevenlabsAudioIsolation(
        audio=InputElevenlabsAudioIsolationAudio_Url(
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

**input:** `InputElevenlabsAudioIsolation` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_english_sts_v2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputElevenlabsEnglishStsV2, InputElevenlabsEnglishStsV2Audio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_elevenlabs_english_sts_v2(
    input=InputElevenlabsEnglishStsV2(
        audio=InputElevenlabsEnglishStsV2Audio_Url(
            url="url",
        ),
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

**input:** `InputElevenlabsEnglishStsV2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_flash_multilingual_v2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The low-latency voice across 30+ languages, for interactive and high-volume speech.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputElevenlabsFlashMultilingualV2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_elevenlabs_flash_multilingual_v2(
    input=InputElevenlabsFlashMultilingualV2(
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

**input:** `InputElevenlabsFlashMultilingualV2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_flash_v2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The low-latency English voice, for interactive speech.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputElevenlabsFlashV2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_elevenlabs_flash_v2(
    input=InputElevenlabsFlashV2(
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

**input:** `InputElevenlabsFlashV2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_multilingual_sts_v2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputElevenlabsMultilingualStsV2, InputElevenlabsMultilingualStsV2Audio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_elevenlabs_multilingual_sts_v2(
    input=InputElevenlabsMultilingualStsV2(
        audio=InputElevenlabsMultilingualStsV2Audio_Url(
            url="url",
        ),
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

**input:** `InputElevenlabsMultilingualStsV2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_multilingual_v2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Steady, natural narration across 30+ languages, for finished voiceover.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputElevenlabsMultilingualV2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_elevenlabs_multilingual_v2(
    input=InputElevenlabsMultilingualV2(
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

**input:** `InputElevenlabsMultilingualV2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_music</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Full tracks from a written brief, with optional lyrics placed across the length you ask for.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputElevenlabsMusic
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_elevenlabs_music(
    input=InputElevenlabsMusic(
        prompt="prompt",
        duration_ms=1,
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

**input:** `InputElevenlabsMusic` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_sound_effects</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One-off sound effects from a written description, loopable on request.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputElevenlabsSoundEffects
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_elevenlabs_sound_effects(
    input=InputElevenlabsSoundEffects(
        text="text",
        duration_ms=1,
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

**input:** `InputElevenlabsSoundEffects` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_v3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The most expressive ElevenLabs voice — emotional range and delivery cues for performance, not just narration.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputElevenlabsV3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_elevenlabs_v3(
    input=InputElevenlabsV3(
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

**input:** `InputElevenlabsV3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_voice_clone</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use an audio clip to create a new Voice.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputElevenlabsVoiceClone, InputElevenlabsVoiceCloneAudio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_elevenlabs_voice_clone(
    input=InputElevenlabsVoiceClone(
        audio=InputElevenlabsVoiceCloneAudio_Url(
            url="url",
        ),
        name="name",
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

**input:** `InputElevenlabsVoiceClone` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_flux11pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Premium color depth and clarity when you want campaign-ready art that feels handcrafted.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputFlux11Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_flux11pro(
    input=InputFlux11Pro(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="540p",
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

**input:** `InputFlux11Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_flux11ultra</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The big-canvas choice for ultra-high-res images and flagship visuals.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputFlux11Ultra
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_flux11ultra(
    input=InputFlux11Ultra(
        prompt="prompt",
        aspect_ratio="16:9",
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

**input:** `InputFlux11Ultra` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_flux3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Video with native audio, straight from a prompt.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputFlux3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_flux3(
    input=InputFlux3(
        prompt="prompt",
        aspect_ratio="auto",
        resolution="720p",
        duration_ms=1,
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

**input:** `InputFlux3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_flux_dev</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fast and light for quick concepts or high-volume social posts on a budget.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputFluxDev
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_flux_dev(
    input=InputFluxDev(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="540p",
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

**input:** `InputFluxDev` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_flux_kontext_max</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Highest-fidelity reference-image support for complex, multi-element scenes and perfectly matched branded visuals.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputFluxKontextMax
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_flux_kontext_max(
    input=InputFluxKontextMax(
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

**input:** `InputFluxKontextMax` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_flux_kontext_pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reference-image support for character, brand, or style consistency.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputFluxKontextPro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_flux_kontext_pro(
    input=InputFluxKontextPro(
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

**input:** `InputFluxKontextPro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_flux2flex</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The tunable Flux.2 tier — trade denoising steps against speed per generation.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputFlux2Flex
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_flux2flex(
    input=InputFlux2Flex(
        prompt="prompt",
        aspect_ratio="16:9",
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

**input:** `InputFlux2Flex` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_flux2klein9b</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The lean Flux.2 tier — quick, inexpensive stills for concepting and high-volume work.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputFlux2Klein9B
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_flux2klein9b(
    input=InputFlux2Klein9B(
        prompt="prompt",
        aspect_ratio="16:9",
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

**input:** `InputFlux2Klein9B` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_flux2max</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The top Flux.2 tier, for realism and precision in final deliverables.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputFlux2Max
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_flux2max(
    input=InputFlux2Max(
        prompt="prompt",
        aspect_ratio="16:9",
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

**input:** `InputFlux2Max` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_flux2pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The everyday Flux.2 tier — style transfer and sequential edits that hold together across passes.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputFlux2Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_flux2pro(
    input=InputFlux2Pro(
        prompt="prompt",
        aspect_ratio="16:9",
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

**input:** `InputFlux2Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_gemini_omni_flash</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gemini's fast multimodal video model — cinematic clips with native audio from a prompt, a keyframe, or reference images.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputGeminiOmniFlash
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_gemini_omni_flash(
    input=InputGeminiOmniFlash(
        prompt="prompt",
        aspect_ratio="16:9",
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

**input:** `InputGeminiOmniFlash` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_gpt_image15</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reads a long, specific brief closely — the choice when the prompt carries the detail.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputGptImage15
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_gpt_image15(
    input=InputGptImage15(
        prompt="prompt",
        aspect_ratio="1:1",
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

**input:** `InputGptImage15` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_gpt_image2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

OpenAI's balanced tier; moderate cost and fidelity, ideal for iterative refinement and everyday generation.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputGptImage2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_gpt_image2(
    input=InputGptImage2(
        prompt="prompt",
        aspect_ratio="16:9",
        resolution="1K",
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

**input:** `InputGptImage2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_grok_imagine</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Grok's take on a prompt — punchy, irreverent stills, in everything from ultrawide to tall.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputGrokImagine
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_grok_imagine(
    input=InputGrokImagine(
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

**input:** `InputGrokImagine` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_grok_imagine20</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

xAI's current Grok Imagine — the same irreverence at higher fidelity, from a prompt or from up to three source images.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputGrokImagine20
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_grok_imagine20(
    input=InputGrokImagine20(
        prompt="prompt",
        aspect_ratio="2:1",
        resolution="1k",
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

**input:** `InputGrokImagine20` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_grok_video</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Short, punchy clips from a prompt at 480p or 720p.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputGrokVideo
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_grok_video(
    input=InputGrokVideo(
        prompt="prompt",
        aspect_ratio="auto",
        resolution="480p",
        duration_ms=1,
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

**input:** `InputGrokVideo` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_happy_horse</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Open-weight video generation from a prompt.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputHappyHorse
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_happy_horse(
    input=InputHappyHorse(
        prompt="prompt",
        aspect_ratio="21:9",
        resolution="720p",
        duration_ms=1,
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

**input:** `InputHappyHorse` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_hedra_avatar</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Hedra's latest longform avatar model, audio to video will full multi-language support. Perfect for talking and singing video with speaker selection up to 10 minutes long.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputHedraAvatar, InputHedraAvatarStartImage_Url, InputHedraAvatarAudioZero_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_hedra_avatar(
    input=InputHedraAvatar(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="540p",
        start_image=InputHedraAvatarStartImage_Url(
            url="url",
        ),
        audio=InputHedraAvatarAudioZero_Url(
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

**input:** `InputHedraAvatar` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_hedra_character3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Hedra's latest longform avatar model, audio to video will full multi-language support. Perfect for talking and singing video with speaker selection up to 10 minutes long.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputHedraCharacter3, InputHedraCharacter3StartImage_Url, InputHedraCharacter3AudioZero_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_hedra_character3(
    input=InputHedraCharacter3(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="540p",
        start_image=InputHedraCharacter3StartImage_Url(
            url="url",
        ),
        audio=InputHedraCharacter3AudioZero_Url(
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

**input:** `InputHedraCharacter3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_heygen_photo_avatar4</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Turn a clear portrait and driving audio into a talking avatar.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputHeygenPhotoAvatar4, InputHeygenPhotoAvatar4StartImage_Url, InputHeygenPhotoAvatar4Audio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_heygen_photo_avatar4(
    input=InputHeygenPhotoAvatar4(
        aspect_ratio="16:9",
        resolution="360p",
        start_image=InputHeygenPhotoAvatar4StartImage_Url(
            url="url",
        ),
        audio=InputHeygenPhotoAvatar4Audio_Url(
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

**input:** `InputHeygenPhotoAvatar4` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_hidream_o1image</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

HiDream.ai's open-weights HiDream-O1-Image (8B): one pixel-native model that generates, edits, and personalizes without a VAE or a separate text encoder.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputHidreamO1Image
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_hidream_o1image(
    input=InputHidreamO1Image(
        prompt="prompt",
        aspect_ratio="16:9",
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

**input:** `InputHidreamO1Image` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_ideogram_v2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Best in class for poster-ready images and spot-on text rendering in social graphics.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputIdeogramV2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_ideogram_v2(
    input=InputIdeogramV2(
        prompt="prompt",
        aspect_ratio="1:1",
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

**input:** `InputIdeogramV2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_ideogram_v4</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ideogram V4 renders poster-ready text and layout; the required quality parameter picks turbo, balanced or quality, which sets both the render effort and the price.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputIdeogramV4
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_ideogram_v4(
    input=InputIdeogramV4(
        prompt="prompt",
        aspect_ratio="16:9",
        resolution="720p",
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

**input:** `InputIdeogramV4` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_imagen3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Google's earlier photoreal generator, kept for parity.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputImagen3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_imagen3(
    input=InputImagen3(
        prompt="prompt",
        aspect_ratio="16:9",
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

**input:** `InputImagen3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_imagen4</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Google's photoreal model—natural lighting, lifelike skin, and pro-grade sharpness in every shot.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputImagen4
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_imagen4(
    input=InputImagen4(
        prompt="prompt",
        aspect_ratio="16:9",
        resolution="1K",
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

**input:** `InputImagen4` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling16</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKling16
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling16(
    input=InputKling16(
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

**input:** `InputKling16` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling21master</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cinema-grade video with striking textures and rich depth.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKling21Master
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling21master(
    input=InputKling21Master(
        prompt="prompt",
        aspect_ratio="16:9",
        duration_ms=1,
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

**input:** `InputKling21Master` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling25turbo</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fast, high-quality video generation.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKling25Turbo
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling25turbo(
    input=InputKling25Turbo(
        prompt="prompt",
        aspect_ratio="16:9",
        duration_ms=1,
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

**input:** `InputKling25Turbo` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling26motion_control</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transfer movements from a reference video to any character image. Cost-effective mode for motion transfer, perfect for portraits and simple animations.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKling26MotionControl, InputKling26MotionControlStartImage_Url, InputKling26MotionControlSourceVideo_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling26motion_control(
    input=InputKling26MotionControl(
        start_image=InputKling26MotionControlStartImage_Url(
            url="url",
        ),
        source_video=InputKling26MotionControlSourceVideo_Url(
            url="url",
        ),
        resolution="720p",
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

**input:** `InputKling26MotionControl` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling26pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cinematic visuals, fluid motion, and native audio generation.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKling26Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling26pro(
    input=InputKling26Pro(
        prompt="prompt",
        aspect_ratio="16:9",
        duration_ms=1,
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

**input:** `InputKling26Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling_ai_avatar_v2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create avatar videos with realistic humans, animals, cartoons, or stylized characters from an image and audio input.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKlingAiAvatarV2, InputKlingAiAvatarV2StartImage_Url, InputKlingAiAvatarV2Audio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling_ai_avatar_v2(
    input=InputKlingAiAvatarV2(
        aspect_ratio="16:9",
        start_image=InputKlingAiAvatarV2StartImage_Url(
            url="url",
        ),
        audio=InputKlingAiAvatarV2Audio_Url(
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

**input:** `InputKlingAiAvatarV2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling_o1</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate from a single image with text-driven style and scene guidance.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKlingO1
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling_o1(
    input=InputKlingO1(
        prompt="prompt",
        aspect_ratio="16:9",
        duration_ms=1,
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

**input:** `InputKlingO1` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling_o3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clips up to 15 seconds with native audio.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKlingO3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling_o3(
    input=InputKlingO3(
        aspect_ratio="16:9",
        duration_ms=1,
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

**input:** `InputKlingO3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling_o3edit</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit videos using natural language.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKlingO3Edit, InputKlingO3EditSourceVideo_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling_o3edit(
    input=InputKlingO3Edit(
        prompt="prompt",
        source_video=InputKlingO3EditSourceVideo_Url(
            url="url",
        ),
        resolution="720p",
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

**input:** `InputKlingO3Edit` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling_o3reference</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Input a reference video and preserve motion and camera style.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKlingO3Reference, InputKlingO3ReferenceSourceVideo_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling_o3reference(
    input=InputKlingO3Reference(
        prompt="prompt",
        source_video=InputKlingO3ReferenceSourceVideo_Url(
            url="url",
        ),
        resolution="720p",
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

**input:** `InputKlingO3Reference` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling_v3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ultra-high-definition storyboards with native audio.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKlingV3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling_v3(
    input=InputKlingV3(
        aspect_ratio="16:9",
        duration_ms=1,
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

**input:** `InputKlingV3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling_v3motion_control</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Animate a character image to match the motion of a reference video. Standard tier for cost-effective generation.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputKlingV3MotionControl, InputKlingV3MotionControlStartImage_Url, InputKlingV3MotionControlSourceVideo_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_kling_v3motion_control(
    input=InputKlingV3MotionControl(
        start_image=InputKlingV3MotionControlStartImage_Url(
            url="url",
        ),
        source_video=InputKlingV3MotionControlSourceVideo_Url(
            url="url",
        ),
        resolution="720p",
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

**input:** `InputKlingV3MotionControl` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_ltx23</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clips up to 4K with synchronized native audio, for final output.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputLtx23
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_ltx23(
    input=InputLtx23(
        prompt="prompt",
        resolution="1080p",
        duration_ms=1,
        aspect_ratio="auto",
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

**input:** `InputLtx23` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_luma_ray32</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cinematic motion with deliberate camera control, from a prompt.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputLumaRay32
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_luma_ray32(
    input=InputLumaRay32(
        prompt="prompt",
        aspect_ratio="3:4",
        resolution="540p",
        duration_ms=1,
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

**input:** `InputLumaRay32` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_mai_image25</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Microsoft AI's MAI-Image-2.5: photorealistic generation and editing with strong in-image typography and design-ready output.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputMaiImage25
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_mai_image25(
    input=InputMaiImage25(
        prompt="prompt",
        aspect_ratio="1:1",
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

**input:** `InputMaiImage25` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_minimax_h3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One model for every starting point — a prompt, a keyframe pair, or reference images that keep a subject consistent.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputMinimaxH3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_minimax_h3(
    input=InputMinimaxH3(
        prompt="prompt",
        resolution="480p",
        duration_ms=1,
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

**input:** `InputMinimaxH3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_minimax_hailuo02</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Everyday 1080p video with natural movement.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputMinimaxHailuo02
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_minimax_hailuo02(
    input=InputMinimaxHailuo02(
        prompt="prompt",
        duration_ms=1,
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

**input:** `InputMinimaxHailuo02` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_minimax_hailuo23</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Everyday 1080p video with natural movement.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputMinimaxHailuo23
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_minimax_hailuo23(
    input=InputMinimaxHailuo23(
        prompt="prompt",
        duration_ms=1,
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

**input:** `InputMinimaxHailuo23` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_minimax_speech25hd_preview</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The high-fidelity tier — closest voice likeness, across 40+ languages.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputMinimaxSpeech25HdPreview
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_minimax_speech25hd_preview(
    input=InputMinimaxSpeech25HdPreview(
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

**input:** `InputMinimaxSpeech25HdPreview` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_minimax_speech25turbo_preview</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The value tier — natural English delivery across 40+ languages, at a lower rate.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputMinimaxSpeech25TurboPreview
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_minimax_speech25turbo_preview(
    input=InputMinimaxSpeech25TurboPreview(
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

**input:** `InputMinimaxSpeech25TurboPreview` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_nano_banana</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reference-guided stills that hold a character or product across a set.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputNanoBanana
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_nano_banana(
    input=InputNanoBanana(
        prompt="prompt",
        aspect_ratio="16:9",
        resolution="1K",
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

**input:** `InputNanoBanana` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_nano_banana2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Multi-subject stills up to 4K — hand it several references and it keeps each one recognizable.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputNanoBanana2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_nano_banana2(
    input=InputNanoBanana2(
        prompt="prompt",
        aspect_ratio="adaptive",
        resolution="512px",
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

**input:** `InputNanoBanana2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_nano_banana_pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The reasoning-heavy tier — dense prompts, mixed references, and style transfer up to 4K.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputNanoBananaPro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_nano_banana_pro(
    input=InputNanoBananaPro(
        prompt="prompt",
        aspect_ratio="adaptive",
        resolution="1K",
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

**input:** `InputNanoBananaPro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_omnihuman15</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates vivid, emotional character videos driven entirely by your audio.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputOmnihuman15, InputOmnihuman15StartImage_Url, InputOmnihuman15Audio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_omnihuman15(
    input=InputOmnihuman15(
        resolution="720p",
        start_image=InputOmnihuman15StartImage_Url(
            url="url",
        ),
        audio=InputOmnihuman15Audio_Url(
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

**input:** `InputOmnihuman15` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_pixverse_v6</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stylized 1080p clips up to 15 seconds, with native audio.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputPixverseV6
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_pixverse_v6(
    input=InputPixverseV6(
        prompt="prompt",
        resolution="360p",
        duration_ms=1,
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

**input:** `InputPixverseV6` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_qwen_image2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Alibaba's Qwen-Image-2.0, tuned for speed. Native 2K output with professional in-image text rendering, for rapid iteration.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputQwenImage2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_qwen_image2(
    input=InputQwenImage2(
        prompt="prompt",
        aspect_ratio="16:9",
        resolution="540p",
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

**input:** `InputQwenImage2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_recraft_v3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Vector-clean graphics and crisp logos on demand.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputRecraftV3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_recraft_v3(
    input=InputRecraftV3(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="540p",
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

**input:** `InputRecraftV3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_reve21</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate images from a text prompt with strong prompt adherence, layout intelligence, and accurate text rendering

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputReve21
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_reve21(
    input=InputReve21(
        prompt="prompt",
        aspect_ratio="4:1",
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

**input:** `InputReve21` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_reve21edit</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit one source image from a natural-language instruction, keeping the rest of the image intact

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputReve21Edit, InputReve21EditImagesItem_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_reve21edit(
    input=InputReve21Edit(
        prompt="prompt",
        aspect_ratio="4:1",
        images=[
            InputReve21EditImagesItem_Url(
                url="url",
            )
        ],
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

**input:** `InputReve21Edit` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_reve21remix</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compose up to eight reference images into a new image from a text prompt

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputReve21Remix, InputReve21RemixImagesItem_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_reve21remix(
    input=InputReve21Remix(
        prompt="prompt",
        aspect_ratio="4:1",
        images=[
            InputReve21RemixImagesItem_Url(
                url="url",
            )
        ],
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

**input:** `InputReve21Remix` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_sana</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lightning-fast and cheap for simple product shots or everyday content.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputSana
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_sana(
    input=InputSana(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="540p",
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

**input:** `InputSana` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_seedance15pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Keyframe-driven video with native audio, from a start frame, an end frame, or both.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputSeedance15Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_seedance15pro(
    input=InputSeedance15Pro(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="480p",
        duration_ms=1,
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

**input:** `InputSeedance15Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_seedance20</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reference-driven video up to 4K with native audio — hold a look across shots with reference images, clips, or audio.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputSeedance20
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_seedance20(
    input=InputSeedance20(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="4K",
        duration_ms=1,
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

**input:** `InputSeedance20` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_seedance20mini</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The lightest Seedance tier — short reference-driven clips at 480p and 720p.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputSeedance20Mini
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_seedance20mini(
    input=InputSeedance20Mini(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="480p",
        duration_ms=1,
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

**input:** `InputSeedance20Mini` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_seedance25</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reference-driven video up to 30 seconds at 1080p, with native audio.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputSeedance25
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_seedance25(
    input=InputSeedance25(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="480p",
        duration_ms=1,
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

**input:** `InputSeedance25` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_seedream40</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Quick, reference-aware stills for professional work on a tight turnaround.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputSeedream40
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_seedream40(
    input=InputSeedream40(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="1080p",
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

**input:** `InputSeedream40` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_seedream45</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finer detail and steadier composition than 4.0, with support for several references at once.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputSeedream45
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_seedream45(
    input=InputSeedream45(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="1440p (2K QHD)",
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

**input:** `InputSeedream45` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_seedream50lite</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sharp 2K and 4K stills from a prompt, at the light tier's price.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputSeedream50Lite
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_seedream50lite(
    input=InputSeedream50Lite(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="1440p (2K QHD)",
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

**input:** `InputSeedream50Lite` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_seedream50pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The top Seedream tier — layer-separable output and strong multilingual in-image text, up to 2K.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputSeedream50Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_seedream50pro(
    input=InputSeedream50Pro(
        prompt="prompt",
        aspect_ratio="1:1",
        resolution="1080p",
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

**input:** `InputSeedream50Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_sora2pro</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For complex, narrative-driven videos with remarkable consistency and realistic character-world interaction.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputSora2Pro
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_sora2pro(
    input=InputSora2Pro(
        prompt="prompt",
        aspect_ratio="16:9",
        resolution="720p",
        duration_ms=1,
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

**input:** `InputSora2Pro` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_topaz_image_upscaler</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use the powerful and accurate Topaz image enhancer to upscale and enhance your images.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputTopazImageUpscaler, InputTopazImageUpscalerSourceImage_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_topaz_image_upscaler(
    input=InputTopazImageUpscaler(
        source_image=InputTopazImageUpscalerSourceImage_Url(
            url="url",
        ),
        target_resolution="1080p",
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

**input:** `InputTopazImageUpscaler` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_topaz_image_upscaler_wonder</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generative upscaling with realistic detail, precise text, and clean graphics — Topaz's highest-quality image upscaler.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputTopazImageUpscalerWonder, InputTopazImageUpscalerWonderSourceImage_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_topaz_image_upscaler_wonder(
    input=InputTopazImageUpscalerWonder(
        source_image=InputTopazImageUpscalerWonderSourceImage_Url(
            url="url",
        ),
        target_resolution="1080p",
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

**input:** `InputTopazImageUpscalerWonder` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_topaz_video_upscaler</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Precision upscaling that cleans compression and noise while staying faithful to the source.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputTopazVideoUpscaler, InputTopazVideoUpscalerSourceVideo_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_topaz_video_upscaler(
    input=InputTopazVideoUpscaler(
        source_video=InputTopazVideoUpscalerSourceVideo_Url(
            url="url",
        ),
        resolution="1080p",
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

**input:** `InputTopazVideoUpscaler` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_topaz_video_upscaler_hyperion25</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Convert SDR video to 10-bit HDR with richer highlights, color, and tonal separation. The output keeps the source resolution.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputTopazVideoUpscalerHyperion25, InputTopazVideoUpscalerHyperion25SourceVideo_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_topaz_video_upscaler_hyperion25(
    input=InputTopazVideoUpscalerHyperion25(
        source_video=InputTopazVideoUpscalerHyperion25SourceVideo_Url(
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

**input:** `InputTopazVideoUpscalerHyperion25` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_topaz_video_upscaler_starlight_fast</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Faster generative diffusion upscaling at half the cost of Starlight Precise.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputTopazVideoUpscalerStarlightFast, InputTopazVideoUpscalerStarlightFastSourceVideo_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_topaz_video_upscaler_starlight_fast(
    input=InputTopazVideoUpscalerStarlightFast(
        source_video=InputTopazVideoUpscalerStarlightFastSourceVideo_Url(
            url="url",
        ),
        resolution="1080p",
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

**input:** `InputTopazVideoUpscalerStarlightFast` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_topaz_video_upscaler_starlight_hq</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generative diffusion upscaling balancing detail and sharpness for medium-to-high quality sources.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputTopazVideoUpscalerStarlightHq, InputTopazVideoUpscalerStarlightHqSourceVideo_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_topaz_video_upscaler_starlight_hq(
    input=InputTopazVideoUpscalerStarlightHq(
        source_video=InputTopazVideoUpscalerStarlightHqSourceVideo_Url(
            url="url",
        ),
        resolution="1080p",
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

**input:** `InputTopazVideoUpscalerStarlightHq` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_topaz_video_upscaler_starlight_precise</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generative diffusion upscaling for AI-generated and archival video with realistic faces, textures, and text.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputTopazVideoUpscalerStarlightPrecise, InputTopazVideoUpscalerStarlightPreciseSourceVideo_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_topaz_video_upscaler_starlight_precise(
    input=InputTopazVideoUpscalerStarlightPrecise(
        source_video=InputTopazVideoUpscalerStarlightPreciseSourceVideo_Url(
            url="url",
        ),
        resolution="1080p",
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

**input:** `InputTopazVideoUpscalerStarlightPrecise` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_veed_fabric10</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Talking video with natural lip-sync and expressive animation.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputVeedFabric10, InputVeedFabric10StartImage_Url, InputVeedFabric10Audio_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_veed_fabric10(
    input=InputVeedFabric10(
        prompt="prompt",
        aspect_ratio="16:9",
        resolution="480p",
        start_image=InputVeedFabric10StartImage_Url(
            url="url",
        ),
        audio=InputVeedFabric10Audio_Url(
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

**input:** `InputVeedFabric10` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_veed_video_background_removal</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a video's background and return transparent WebM.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputVeedVideoBackgroundRemoval, InputVeedVideoBackgroundRemovalSourceVideo_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_veed_video_background_removal(
    input=InputVeedVideoBackgroundRemoval(
        source_video=InputVeedVideoBackgroundRemovalSourceVideo_Url(
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

**input:** `InputVeedVideoBackgroundRemoval` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_veo2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Google's earlier cinematic generator, kept for existing workflows.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputVeo2
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_veo2(
    input=InputVeo2(
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

**input:** `InputVeo2` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_veo3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Hollywood-grade, cinematic video straight from text—your go-to for hero campaigns.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputVeo3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_veo3(
    input=InputVeo3(
        prompt="prompt",
        aspect_ratio="16:9",
        resolution="720p",
        duration_ms=1,
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

**input:** `InputVeo3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_veo31</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For unparalleled detail and nuance, perfect for when your vision requires the best possible quality.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputVeo31
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_veo31(
    input=InputVeo31(
        prompt="prompt",
        aspect_ratio="16:9",
        resolution="720p",
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

**input:** `InputVeo31` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_vidu_q3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The longest clips in the catalog — up to 16 seconds with native dialogue and sound, from a text prompt, from a start frame, or between a start and end frame

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputViduQ3
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_vidu_q3(
    input=InputViduQ3(
        prompt="prompt",
        resolution="540p",
        duration_ms=1,
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

**input:** `InputViduQ3` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_vidu_q3reference</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Keep up to four subjects consistent across a clip from reference images.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputViduQ3Reference, InputViduQ3ReferenceImagesItem_Url
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_vidu_q3reference(
    input=InputViduQ3Reference(
        prompt="prompt",
        aspect_ratio="16:9",
        resolution="540p",
        duration_ms=1,
        images=[
            InputViduQ3ReferenceImagesItem_Url(
                url="url",
            )
        ],
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

**input:** `InputViduQ3Reference` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_wan27</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Wan 2.7 video with native audio — from a text prompt, from a first frame with an optional last frame, or from reference images that keep subjects consistent

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputWan27
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_wan27(
    input=InputWan27(
        prompt="prompt",
        resolution="720p",
        duration_ms=1,
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

**input:** `InputWan27` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_wan30</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Wan 3.0 video with native audio, up to 30 seconds in one shot — from a text prompt, from a first frame with an optional last frame, or from reference images that keep subjects consistent

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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
from hedra import Hedra, InputWan30
from hedra.environment import HedraEnvironment

client = Hedra(
    api_key="<token>",
    environment=HedraEnvironment.PRODUCTION,
)

client.jobs.submit_wan30(
    input=InputWan30(
        prompt="prompt",
        aspect_ratio="adaptive",
        resolution="480p",
        duration_ms=1,
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

**input:** `InputWan30` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs any model in the catalog by its public id, with `input` passed through untyped — the same call the typed operations below make, minus the compile-time schema.

Reach for it when the model is not known ahead of time: a client generated before a model shipped can still run it, and an id read from `GET /v3/models` at runtime needs no regeneration. Prefer the typed operation whenever your client already has one — `input` here is validated against the same published schema (`GET /v3/models/{model}`), so a bad field is a `400` at submit rather than an error before the call.

Submits an asynchronous job and returns `202` with a job id. Fetch the result at `GET /v3/jobs/{job_id}` — each item in its `outputs[]` follows the `OutputItem` schema — or track progress via `GET /v3/jobs/{job_id}/status` / the SSE stream at `GET /v3/jobs/{job_id}/stream`.
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

client.jobs.submit(
    model="model",
    input={
        "key": "value"
    },
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

**model:** `str` — The model's public id (`GET /v3/models`).
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Dict[str, typing.Any]` — Model-specific inputs, validated at submit against the model's published input schema (`GET /v3/models/{model}`).
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[str]` — URL to receive a signed completion webhook.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Replays the original ack for a retried submit instead of enqueueing a duplicate job.
    
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

**modality:** `typing.Optional[Modality]` — Only models with this modality, matching `modality` on each returned model.
    
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

**model:** `str` — The model's public id (`GET /v3/models`).
    
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

<details><summary><code>client.models.<a href="src/hedra/models/client.py">list_model_jobs</a>(...) -> JobListResponse</code></summary>
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

client.models.list_model_jobs(
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

**model:** `str` — The model's public id (`GET /v3/models`).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum items per page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `next_cursor`; omit for the first page.
    
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

Voices this model accepts — the shared library, plus the caller's own cloned voices when the request carries credentials.
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

**model:** `str` — The model's public id (`GET /v3/models`).
    
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

<details><summary><code>client.models.<a href="src/hedra/models/client.py">search_voices</a>(...) -> VoiceListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The voices this model accepts, ranked against a description — the whole shared library, including the voices the listing does not return.
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

client.models.search_voices(
    model="model",
    q="q",
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

**model:** `str` — The model's public id (`GET /v3/models`).
    
</dd>
</dl>

<dl>
<dd>

**q:** `str` — What the voice should sound like, in plain words — "warm british narrator", "energetic young announcer". Matched against the whole library for this model's provider, not just the voices `GET /v3/models/{model}/voices` returns.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum voices to return. Applies to the whole response.
    
</dd>
</dl>

<dl>
<dd>

**gender:** `typing.Optional[VoiceGender]` — Only voices curated with this gender.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — Only voices curated for this language, as an ISO 639-1 two-letter code (`en`, `es`, `fr`).
    
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

**model:** `str` — The model's public id (`GET /v3/models`).
    
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

**model:** `str` — The model's public id (`GET /v3/models`).
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[typing.Dict[str, typing.Any]]` — The same model-specific inputs a submit would carry; the estimate prices exactly this body.
    
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

**workspace_id:** `typing.Optional[str]` — List keys of this workspace; omitted means the authenticating key's workspace.
    
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

**name:** `typing.Optional[str]` — Human-readable label for the key.
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.List[ApiKeyScope]]` — Scopes granted to the key; omitted means full access.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[ApiKeyKind]` — `personal` (default) dies with the member; `service` is workspace-shared, OWNER/ADMIN-managed, and survives member removal.
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` — Target workspace; omitted means the authenticating key's workspace.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` — ISO-8601 instant the key stops authenticating; omitted means it never expires.
    
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

**key_id:** `str` — The key's public identifier.
    
</dd>
</dl>

<dl>
<dd>

**grace_period_seconds:** `typing.Optional[int]` — Seconds the old secret keeps authenticating after the rotation; omitted means the service default (24h).
    
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

**key_id:** `str` — The key's public identifier.
    
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

**ttl_seconds:** `typing.Optional[int]` — Seconds until the token expires; omitted means the service default.
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.List[ApiKeyScope]]` — Scopes granted to the token. Omitted means every scope of the minting key; an explicit subset narrows the grant, and requesting beyond the key's scopes is a 403.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Store a file and return a short-lived URL to pass in a model's `input`.

Free, and available on an empty API wallet — funding is enforced when you
submit a generation, not when you upload its inputs. `GET /v3/balance`
reports what the wallet holds.
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

**file:** `core.File` — The file to upload.
    
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

**start:** `typing.Optional[datetime.datetime]` — Window start (inclusive, ISO-8601); defaults to 7 days before `end`. Bounds job-creation time.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — Window end (exclusive, ISO-8601); defaults to now. The window is capped at 90 days.
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[UsageGroupBy]` — One summary row (`total`), one per UTC day (`day`), or one per model (`model`).
    
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

<details><summary><code>client.billing.<a href="src/hedra/billing/client.py">list_transactions</a>(...) -> TransactionListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Every movement of the API wallet's balance, newest first: funds added,
jobs charged, charges refunded, and corrections. Scoped to the workspace
the credential bills, the same one `GET /v3/balance` reports.
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

client.billing.list_transactions()

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

**limit:** `typing.Optional[int]` — Maximum items per page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `next_cursor`; omit for the first page.
    
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

**url:** `str` — HTTPS endpoint to receive terminal webhooks for every job that names no per-job `webhook` on submit.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the default endpoint receives deliveries; false pauses it without discarding the URL.
    
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

**limit:** `typing.Optional[int]` — Maximum items per page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `next_cursor`; omit for the first page.
    
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

The webhook id is stable across the original and every replay, because it
identifies the event. Every attempt of a replayed cycle therefore also carries
``X-Hedra-Webhook-Redelivery: true`` — without it a receiver doing exactly what
our guidance says (dedupe on the id) would silently discard the replay, which is
the one case where the duplicate is the point.
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
    job_id="job_id",
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

**job_id:** `str` — The job's id (`job_<uuid>`).
    
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

**name:** `str` — Human-readable label.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — HTTPS endpoint job-log batches are posted to.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[LogDrainFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — Signs every NDJSON post. Required when `format` is `ndjson` (the default); optional for `otlp` drains, whose receivers authenticate with `headers` instead.
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Extra headers sent with every post — typically the receiver's authentication. Stored values are never echoed back; reads expose `header_names` only.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the drain receives batches.
    
</dd>
</dl>

<dl>
<dd>

**batch_size:** `typing.Optional[int]` — Maximum log lines per post.
    
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

**drain_id:** `str` — The drain's id (`drain_<uuid>`).
    
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

**drain_id:** `str` — The drain's id (`drain_<uuid>`).
    
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

**drain_id:** `str` — The drain's id (`drain_<uuid>`).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New label; omitted means unchanged.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — New destination; omitted means unchanged.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[LogDrainFormat]` — New wire format; omitted means unchanged.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — Rotates the signing secret. No conditional applies here: the drain may already hold one. Switching `format` to `ndjson` on a drain with no stored secret requires supplying one in the same request.
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Replaces the full header set; `{}` clears it. Omitted means unchanged.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Pause (false) or resume (true) the drain; omitted means unchanged. Re-enabling clears the auto-disable failure count.
    
</dd>
</dl>

<dl>
<dd>

**batch_size:** `typing.Optional[int]` — New maximum log lines per post; omitted means unchanged.
    
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

**drain_id:** `str` — The drain's id (`drain_<uuid>`).
    
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

