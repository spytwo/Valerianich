up:
    docker compose up -d

down:
    docker compose down

fix:
    docker compose exec app uv run ruff format
    docker compose exec app uv run ruff check --fix