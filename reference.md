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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_dreamina31</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ultra high quality generations for professional grade images.

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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_flash_multilingual_v2</a>(...) -> SubmitResponse</code></summary>
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_multilingual_v2</a>(...) -> SubmitResponse</code></summary>
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_elevenlabs_v3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

ElevenLabs V3

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

Black Forest Labs FLUX.3 text-to-video with native audio.

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

Image creation and editing with FLUX.2 [flex] from Black Forest Labs.

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

Flux.2 [klein] 9B model from Black Forest Labs.

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

FLUX.2 [max] delivers state-of-the-art image generation and advanced image editing with exceptional realism, precision, and consistency.

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

Image creation and editing with FLUX.2 [pro] from Black Forest Labs. Ideal for high-quality image manipulation, style transfer, and sequential editing workflows

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

OpenAI-powered image generation with exceptional prompt understanding and versatile editing capabilities.

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
        quality="low",
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

xAI's Grok Imagine image generation model

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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_grok_video</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

xAI's text-to-video generation model.

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

Generate video from text with Alibaba Happy Horse 1.0.

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
        quality="standard",
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
        quality="turbo",
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

The latest text to image model from Google

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
        quality="standard",
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

Text-to-video model with up to 15-second generations and native audio.

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
        prompt="prompt",
        aspect_ratio="16:9",
        duration_ms=1,
        quality="standard",
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_kling_v3</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Text-to-video with ultra-high-definition storyboards and native audio.

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
        prompt="prompt",
        aspect_ratio="16:9",
        duration_ms=1,
        quality="standard",
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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_ltx23</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lightricks LTX-2.3 text-to-video at up to 4K, with synchronized native audio

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
        aspect_ratio="16:9",
        quality="fast",
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

Luma Ray 3.2 text-to-video with cinematic motion and camera control

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
        aspect_ratio="1:1",
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
        quality="standard",
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

MiniMax H3 video generation from text, frames, or references.

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
        resolution="768p",
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
        quality="standard",
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
        quality="standard",
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

The brand new HD model. Ultimate Similarity, Ultra-High Quality. Supports 40+ languages including Tamil, Hebrew, Swedish, etc.

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

The brand new Turbo model. Ultimate Value, 40 Languages. Major improvements to natural English expression.

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

Best in class image model with reference image support and ultra high quality generations for professional grade images.

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

Gemini 3.1 Flash native image generation with improved quality and advanced features including multi-subject reference and high-fidelity style transfer

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

Gemini 3 Pro native image generation with advanced multimodal understanding and richer visuals

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

PixVerse V6 text-to-video with native audio and 1080p output up to 15 seconds

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
        quality="standard",
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

ByteDance Seedance 1.5 Pro video generation model

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

ByteDance Seedance 2.0 video generation model

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
        resolution="480p",
        duration_ms=1,
        quality="standard",
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

ByteDance Seedance 2.0 Mini video generation model

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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_seedream40</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ultra-fast pro grade image model, pairing reference image support with high quality output for professional visuals

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

Latest Seedream with enhanced detail, refined composition, and multi-reference image support for professional visuals.

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

ByteDance Seedream 5.0 Lite Text-to-Image

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

ByteDance Seedream 5.0 Pro Text-to-Image

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

<details><summary><code>client.jobs.<a href="src/hedra/jobs/client.py">submit_veo2</a>(...) -> SubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The current state of the art in video generation

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
        quality="standard",
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
        quality="standard",
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

Vidu Q3 video with native dialogue and sound, up to 16 seconds — from a text prompt, from a start frame, or between a start and end frame

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
        quality="standard",
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

Vidu Q3 reference-to-video keeping up to four subjects consistent

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

Voices this model accepts — scoped to the model's voice provider. fern-config end-to-end regeneration probe 20260810-011748.
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

