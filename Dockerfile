FROM python:3.12-alpine

WORKDIR /opt/pydantic-media-type

RUN set -eux; \
    apk update; \
    apk add curl

# Install Poetry
RUN set eux; \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python; \
    cd /usr/local/bin; \
    ln -s /opt/poetry/bin/poetry; \
    poetry config virtualenvs.create false; \
    poetry self add poetry-plugin-sort

COPY ./pyproject.toml ./poetry.lock /opt/pydantic-media-type/

RUN poetry install --no-root

COPY . /opt/pydantic-media-type
ENV PYTHONPATH=/opt/pydantic-media-type
