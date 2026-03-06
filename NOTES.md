## Create a project

```sh
uv init --package [name]
```

## Install

```sh
uv sync
```

## Run current

```sh
uv run [name]
```

## Intall

```sh
uv tool install [name]
```

## Build

```sh
uv build
```


## GitHub Workflow

```yml .github/workflows/publish.yml
name: "Publish"

on:
  push:
    tags:
      # Publish on any tag starting with a `v`, e.g., v0.1.0
      - v*

jobs:
  run:
    runs-on: ubuntu-latest
    environment:
      name: pypi
    permissions:
      id-token: write
      contents: read
    steps:
      - name: Checkout
        uses: actions/checkout@v6
      - name: Install uv
        uses: astral-sh/setup-uv@v7
        with:
          enable-cache: true
      - name: Install Python
        run: uv python install
      - name: Build
        run: uv build
      - name: Publish
        run: uv publish

```

## Publish

Guide [publishing-to-pypi](https://docs.astral.sh/uv/guides/integration/github/#publishing-to-pypi)

```sh
uv version --bump
git tag -a v1.1.0 -m "Release v1.1.0"
git push origin v1.1.0
```
