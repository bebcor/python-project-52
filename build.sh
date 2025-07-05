#!/usr/bin/env bash

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env


python3 -m venv venv
source venv/bin/activate


$HOME/.local/bin/uv pip install -r requirements.txt


python manage.py collectstatic --noinput
python manage.py migrate
