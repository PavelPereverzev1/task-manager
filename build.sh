#!/usr/bin/env bash
set -o errexit

pip install uv

uv pip install --system -r pyproject.toml

uv run python manage.py collectstatic --no-input
uv run python manage.py migrate