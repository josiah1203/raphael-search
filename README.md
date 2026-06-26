# raphael-search

Global and scoped search, semantic search

## API

- Prefix: `/v1/search`
- Port: `8092`
- Health: `GET /health`

## Events

_Published and consumed events documented in `openapi.yaml` and raphael-contracts._

## Development

```bash
uv sync
uv run uvicorn raphael_search.app:app --reload --port 8092
```

Part of the [Raphael Platform](https://github.com/hummingbird-labs) by HummingBird Labs.
