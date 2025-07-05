#!/usr/bin/env bash
set -e


curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/activate


echo "Installing dependencies..."
uv pip install -r requirements.txt


echo "===== DIAGNOSTICS START ====="
echo "Current user: $(whoami)"
echo "Home directory: $HOME"
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"
echo "Gunicorn version: $(gunicorn --version || echo 'Gunicorn not found')"
echo "Gunicorn path: $(which gunicorn || echo 'Not in PATH')"
echo "Contents of $HOME/.local/bin:"
ls -la $HOME/.local/bin || echo "Directory not found"
echo "===== DIAGNOSTICS END ====="


echo "Running collectstatic..."
python manage.py collectstatic --noinput
echo "Running migrations..."
python manage.py migrate
