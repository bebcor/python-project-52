#!/usr/bin/env bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

python -m venv venv
source venv/bin/activate

uv pip install -r requirements.txt

make install && make collectstatic && make migrate


echo "===== PATH DIAGNOSTICS ====="
echo "Current PATH: $PATH"
echo "Python path: $(which python)"
echo "Django version: $(python -c 'import django; print(django.__version__)' || echo 'Django not found')"
echo "Gunicorn path: $(which gunicorn)"
echo "===== END DIAGNOSTICS ====="
