#!/usr/bin/env bash
set -e


curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
export PATH="$HOME/.cargo/bin:$PATH"


uv pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
