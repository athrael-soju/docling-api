# Docling API server

## Getting Started

```
docker compose up
docker compose up -f docker-compose.gpu.yml up  # for GPU
```

## Request

```
curl -X POST http://localhost:8000/parse -H "Content-Type: multipart/form-data" -F "file=@path/to/file"
```

Or access the API docs at http://localhost:8000/docs
