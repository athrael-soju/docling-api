# Docling API server

## Getting Started

### Local development

```
uvicorn app:app --reload --port 8000 --host 127.0.0.1
```

### Docker

```
docker compose up
docker compose up -f docker-compose.gpu.yml up  # for GPU
```

## Request

```
curl -X POST http://localhost:8000/convert -H "Content-Type: multipart/form-data" -F "file=@path/to/file"
```

Or access the API docs at http://localhost:8000/docs

## Demo (x2 speed)

![demo](./demo.gif)
