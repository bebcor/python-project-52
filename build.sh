#!/usr/bin/env bash
set -e


curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env


source ~/.venvs/project52/bin/activate


uv pip install -r requirements.txt


python manage.py migrate
python manage.py collectstatic --noinput
