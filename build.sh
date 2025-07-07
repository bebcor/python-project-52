#!/usr/bin/env bash
set -e

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

uv pip install -r requirements.txt --python=3.10

python manage.py migrate
python manage.py collectstatic --noinput
