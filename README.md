# Hedra Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=Hedra%2FPython)
[![pypi](https://img.shields.io/pypi/v/hedra-python)](https://pypi.python.org/pypi/hedra-python)

The Hedra Python library provides convenient access to the Hedra APIs from Python.

## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Custom base URL](#custom-base-url)
- [Pagination](#pagination)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## Installation

```sh
pip install hedra-python
```

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from hedra import Hedra

client = Hedra(
    api_key="<value>",
)

result = client.queue.submit(
    model="kling-o3-pro",
    input={
        "prompt": "a fox sprinting across fresh snow",
        "aspect_ratio": "16:9",
    },
)
print(result.request_id, result.status)

# Poll until terminal
status = client.requests.get_status(result.request_id)

# Fetch the finished result (outputs, metrics)
final = client.requests.get(result.request_id)
```

The client authenticates with `Authorization: Bearer <api key>`; an API key is the
`<key_id>:<secret>` credential from the Hedra console. The API key can also be provided via the `HEDRA_API_KEY` environment variable, in which
case `api_key` may be omitted:

```python
import os

from hedra import Hedra

# Reads HEDRA_API_KEY from the environment
client = Hedra()
```

## Custom base URL

The client targets `https://api.hedra.com/v3`. Override it with `base_url` if you
need to point elsewhere (e.g. a mock server in tests):

```python
from hedra import Hedra

client = Hedra(
    api_key="<value>",
    base_url="http://localhost:8000/v3",
)
```

## Pagination

`client.requests.list(...)` returns a pager that auto-fetches pages as you iterate:

```python
for request in client.requests.list(limit=50):
    print(request.request_id, request.status)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from hedra import AsyncHedra

client = AsyncHedra(
    api_key="<value>",
)


async def main() -> None:
    await client.queue.submit(
        model="kling-o3-pro",
        input={"prompt": "a fox sprinting across fresh snow"},
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from hedra.core.api_error import ApiError

try:
    client.queue.submit(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from hedra import Hedra

client = Hedra(...)
response = client.queue.with_raw_response.submit(...)
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
client.queue.submit(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from hedra import Hedra

client = Hedra(..., timeout=20.0)

# Override timeout for a specific method
client.queue.submit(..., request_options={
    "timeout_in_seconds": 1
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
