#!/usr/bin/env bash
set -o errexit

pip install uv

uv pip install --system .

python manage.py collectstatic --no-input
python manage.py migrate