#!/usr/bin/env bash
set -e

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env


uv pip install -r requirements.txt --python /opt/render/project/python/Python-3.10.12/bin/python3.10


/opt/render/project/python/Python-3.10.12/bin/python3.10 manage.py migrate
/opt/render/project/python/Python-3.10.12/bin/python3.10 manage.py collectstatic --noinput
