#!/usr/bin/env bash

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env


$HOME/.local/bin/uv pip install -r requirements.txt


$HOME/.local/bin/uv python manage.py collectstatic --noinput
$HOME/.local/bin/uv python manage.py migrate
