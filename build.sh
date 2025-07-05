#!/usr/bin/env bash
set -e  


curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/activate


uv pip install --upgrade pip
uv pip install -r requirements.txt


python manage.py collectstatic --noinput
python manage.py migrate
