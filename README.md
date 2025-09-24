# Pydantic Media Type

This package provides a [Pydantic](https://docs.pydantic.dev/) type that can be used
to validate [media types](https://en.wikipedia.org/wiki/Media_type). It uses the
media types from the [mimetypes](https://docs.python.org/3/library/mimetypes.html)
module of [The Python Standard Library](https://docs.python.org/3/library/).

## Installation
Install using uv:
```shell
uv add pydantic-media-type
```
or using pip:
```shell
pip install pydantic-media-type
```

## Example
```python
from pydantic import BaseModel

from pydantic_media_type import MediaType


class Model(BaseModel):
    media_type: MediaType

print(Model(media_type=MediaType("image/png")).media_type)  # Will print: image/png
Model(media_type=MediaType("invalid"))  # Will raise pydantic.ValidationError with code media_type_unsupported
```

## Development

Getting the project up and running can be achieved without much effort using Docker
Compose. Doing so ensures that there should be very little difference in
environment between all of us devs.

### Starting the project

```shell
docker compose build
docker compose run --rm pydantic-media-type sh
```

The last command gives you a shell within the container.

### Dependency management

We shouldn't have any other dependencies other than python and pydantic.

However, we do have some dev dependencies like:
- ruff
- mypy
- pytest

We will do our best to keep those up to date. Should you want to upgrade them
yourself, please do it from the shell inside the container using:
```shell
uv sync --upgrade
```
Similarly, installing new dependencies is possible using the command:
```shell
uv add name-of-the-dependency-to-install
```

### Dev tools
This project uses `ruff`, `mypy` and `pytest`.
The preferred way to run them is by using the container, for example:
```shell
docker compose build
docker compose run --rm pydantic-media-type sh
uv run ruff check
uv run mypy .
uv run pytest -v
```
