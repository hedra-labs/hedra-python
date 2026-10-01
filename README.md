# Hedra Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=Hedra%2FPython)
[![pypi](https://img.shields.io/pypi/v/hedra-sdk)](https://pypi.python.org/pypi/hedra-sdk)

The Hedra Python library provides convenient access to the Hedra APIs from Python.

## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Custom base URL](#custom-base-url)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Streaming](#streaming)
- [Pagination](#pagination)
- [Media Inputs and File Uploads](#media-inputs-and-file-uploads)
  - [Untyped input](#untyped-input-clientjobssubmit--clientmodelsestimate)
  - [Which fields go together](#which-fields-go-together)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## Installation

```sh
pip install hedra-sdk
```

## Reference

A full reference for this library is available [here](https://github.com/hedra-labs/hedra-python/blob/main/reference.md).

## Usage

Instantiate and use the client with the following:

```python
import time

from hedra import Hedra, InputMinimaxH3

client = Hedra(
    api_key="<value>",
)

submitted = client.jobs.submit_minimax_h3(
    input=InputMinimaxH3(
        prompt="a fox sprinting across fresh snow",
        aspect_ratio="16:9",
        resolution="768p",
        duration_ms=6000,
    ),
)

# Poll until the job reaches a terminal state, then fetch the result envelope.
status = client.jobs.get_status(submitted.job_id)
while status.status in ("IN_QUEUE", "IN_PROGRESS"):
    time.sleep(2)
    status = client.jobs.get_status(submitted.job_id)

result = client.jobs.get(submitted.job_id)
for output in result.outputs or []:
    print(output.url)
```

Every model has its own submit method — `submit_minimax_h3`, `submit_kling_o3`, `submit_veo3`
and so on — each taking the typed input model for that model (`InputMinimaxH3`, `InputKlingO3`, …).
The [reference](https://github.com/hedra-labs/hedra-python/blob/main/reference.md) lists all of them.
To run a model by its public id instead, with an untyped `input` dict that the API validates at
submit time, use `client.jobs.submit(model, input={...})`. Prefer the typed methods when one exists:
the untyped path sends whatever dict you give it, so a malformed field only fails once it reaches the
server. See [Media Inputs and File Uploads](#media-inputs-and-file-uploads) for the shape a media
reference must have there.

Instead of polling you can follow the job over server-sent events; see [Streaming](#streaming).

The client authenticates with `Authorization: Bearer <api key>`; an API key is the
`<key_id>:<secret>` credential from the Hedra console. The API key can also be provided via the
`HEDRA_API_KEY` environment variable, in which case `api_key` may be omitted:

```python
from hedra import Hedra

# Reads HEDRA_API_KEY from the environment
client = Hedra()
```

## Custom base URL

The client targets `https://api.hedra.com/v3` (`HedraEnvironment.PRODUCTION`). Override it with
`base_url` if you need to point elsewhere (e.g. a mock server in tests):

```python
from hedra import Hedra

client = Hedra(
    api_key="<value>",
    base_url="http://localhost:8000/v3",
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from hedra import AsyncHedra, InputMinimaxH3

client = AsyncHedra(
    api_key="<value>",
)


async def main() -> None:
    await client.jobs.submit_minimax_h3(
        input=InputMinimaxH3(
            prompt="a fox sprinting across fresh snow",
            aspect_ratio="16:9",
            resolution="768p",
            duration_ms=6000,
        ),
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from hedra.core.api_error import ApiError

try:
    client.jobs.submit_minimax_h3(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Streaming

`client.jobs.stream(job_id)` follows a job over server-sent events instead of polling. It returns a
generator that yields a `StatusResponse` for every `status` frame and a `JobLogItem` for every `log`
frame, and it returns once the job reaches a terminal state:

```python
from hedra import Hedra, StatusResponse

client = Hedra(
    api_key="<value>",
)

# submitted is the SubmitResponse returned by any submit call
for event in client.jobs.stream(submitted.job_id):
    if isinstance(event, StatusResponse):
        print(event.status, event.progress)
    else:
        print(event.level, event.message)
```

A dropped connection is resumed automatically from the last event id. Tune that with the
`stream_reconnection_enabled` and `max_stream_reconnection_attempts` options, on the client or per
request via `request_options`.

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from hedra import Hedra

client = Hedra(
    api_key="<value>",
)

for job in client.jobs.list(limit=50):
    print(job.job_id, job.status)
```

```python
# You can also iterate through pages and access the typed response per page
pager = client.jobs.list(...)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)
```

## Media Inputs and File Uploads

Media inputs (`start_image`, `end_image`, `images`, `audios`, `videos`, …) accept exactly two kinds of
reference:

- **an uploaded file**: the `url` that `client.files.upload` returned to you, or
- **an earlier output**: the `asset_id` of an output from one of your own completed jobs
  (`outputs[].asset_id` on `client.jobs.get`).

**A public URL is not accepted.** It rejects any URL that `POST /v3/files` did not issue to you
with a `400` (`reason: "external_url_rejected"`), even a public link, a CDN URL or a presigned URL from
your own bucket. To use a remote file, download it and upload it with `client.files.upload`.

The upload URL is the file's handle. Pass it back exactly as returned, query string included: if you
change it, the API treats it as an external URL. It stops being accepted about an hour after upload
(`upload.expires_at`), and after that a submit fails with `400` (`reason: "expired"`). Upload right
before you submit, and upload again rather than reusing an old URL.

```python
from hedra import Hedra, InputMinimaxH3, InputMinimaxH3StartImage_Url

client = Hedra(
    api_key="<value>",
)

with open("frame.png", "rb") as f:
    upload = client.files.upload(file=f)

client.jobs.submit_minimax_h3(
    input=InputMinimaxH3(
        prompt="the fox turns toward the camera",
        resolution="768p",
        duration_ms=6000,
        start_image=InputMinimaxH3StartImage_Url(url=upload.url),
    ),
)
```

`file` accepts an open binary file, raw `bytes`, or a `(filename, content, content_type)` tuple. A file
that lives at a remote URL is downloaded first and then uploaded:

```python
import httpx

remote = httpx.get("https://example.com/frame.png", follow_redirects=True)
remote.raise_for_status()
upload = client.files.upload(file=("frame.png", remote.content, remote.headers["content-type"]))
```

To reuse an output of an earlier job, reference it by asset id. You don't need to upload it again:

```python
from hedra import InputMinimaxH3, InputMinimaxH3StartImage_Asset

previous = client.jobs.get("<job_id of an image job>")

client.jobs.submit_minimax_h3(
    input=InputMinimaxH3(
        prompt="the fox turns toward the camera",
        resolution="768p",
        duration_ms=6000,
        start_image=InputMinimaxH3StartImage_Asset(asset_id=previous.outputs[0].asset_id),
    ),
)
```

Every media field has its own pair of classes, named `Input<Model><Field>_Url` and
`Input<Model><Field>_Asset`, for example `InputKlingO3StartImage_Url` or `InputMinimaxH3ImagesItem_Asset`
for one item of an `images` list. Use these underscore classes. `InputMinimaxH3StartImageUrl` (no
underscore) also exists, but it is only the body of the `url` variant. It has no `source` field, so
passing it as `start_image` fails with `Unable to extract tag using discriminator 'source'`.

### Untyped input (`client.jobs.submit` / `client.models.estimate`)

`client.jobs.submit(model, input={...})` and `client.models.estimate(model, input={...})` take a plain dict
and send it unchanged. The SDK does no checking on that path. There, a media reference is an object whose
`source` field says which kind it is:

```python
client.jobs.submit(
    "minimax-h3",
    input={
        "prompt": "the fox turns toward the camera",
        "resolution": "768p",
        "duration_ms": 6000,
        "start_image": {"source": "url", "url": upload.url},
        # or, for an earlier output: {"source": "asset", "asset_id": "asset_<uuid>"}
    },
)
```

These are the mistakes we see most. The first two can only happen on the untyped path, because the typed
`submit_<model>` methods raise a `pydantic.ValidationError` before sending the request:

| You send | The API answers `400` with |
| --- | --- |
| a bare string: `"start_image": upload.url` | `Input should be a valid dictionary or object to extract fields from` |
| an object without `source`: `"start_image": {"url": upload.url}` | `Unable to extract tag using discriminator 'source'` |
| any URL that `client.files.upload` did not return | `reason: "external_url_rejected"` |
| an upload URL more than about an hour old | `reason: "expired"` |

**Prefer the typed `client.jobs.submit_<model>(...)` methods** whenever your client has one for the model.
They build the right `source`-tagged object for you and catch a malformed reference before it costs a
round trip. Keep the untyped `submit` for model ids that are only known at runtime.

### Which fields go together

Each model accepts a fixed set of field combinations, one per input mode. They are listed under "Accepted
field combinations" in the docstring of its `Input<Model>` class. The SDK does not enforce them: an
`Input<Model>` object will hold any combination, and only the server rejects a wrong one. The combination
most often gotten wrong is `aspect_ratio` together with `start_image`, and the rule differs from model to
model:

- **must not be sent** for the MiniMax H3 and Hailuo video models (`minimax-h3`, `minimax-hailuo-23`, …),
  `pixverse-v6`, `vidu-q3` and `wan-2-7`. The image-to-video mode uses the start frame's aspect ratio.
- **required** for the Kling models, `veo-3`, `sora-2-pro`, `wan-3-0` and others.

`client.models.estimate(model, input={...})` validates `input` against these rules without creating a job
or charging anything. Use it to check a new combination before you submit.

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from hedra import Hedra

client = Hedra(...)
response = client.jobs.with_raw_response.submit_minimax_h3(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.jobs.submit_minimax_h3(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from hedra import Hedra

client = Hedra(..., timeout=20.0)

# Override timeout for a specific method
client.jobs.submit_minimax_h3(..., request_options={
    "timeout": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from hedra import Hedra

client = Hedra(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
