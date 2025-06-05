FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /ticket_mgmt

COPY ./pyproject.toml /ticket_mgmt/pyproject.toml
COPY ticket_mgmt.env /ticket_mgmt/ticket_mgmt.env

RUN uv sync

COPY ./app /ticket_mgmt/app

# Expose port
EXPOSE 8000

CMD ["uv", "run", "app/main.py"]
