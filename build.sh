#!/usr/bin/env bash

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env


$HOME/.local/bin/uv pip install -r requirements.txt


python -m django --version
python manage.py collectstatic --noinput
python manage.py migrate
