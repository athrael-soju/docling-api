FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-cache

COPY download_models.py test.pdf ./
RUN /app/.venv/bin/python download_models.py && rm download_models.py test.pdf

COPY app.py ./
CMD ["/app/.venv/bin/fastapi", "run", "app.py", "--port", "8000", "--host", "0.0.0.0"]
