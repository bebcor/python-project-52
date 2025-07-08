#!/usr/bin/env bash
set -e

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env


export PYTHONPATH=$(pwd):$PYTHONPATH
export DJANGO_SETTINGS_MODULE=task_manager.settings

uv pip install -r requirements.txt --python /opt/render/project/python/Python-3.10.12/bin/python3.10

ln -s /project /project/code

/opt/render/project/python/Python-3.10.12/bin/python3.10 manage.py migrate
/opt/render/project/python/Python-3.10.12/bin/python3.10 manage.py collectstatic --noinput

chmod +x /project/runner.sh
