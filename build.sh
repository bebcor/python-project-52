#!/usr/bin/env bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env  

make install && make collectstatic && make migrate


echo "===== PATH DIAGNOSTICS ====="
echo "Current PATH: $PATH"
echo "Gunicorn path: $(which gunicorn || echo 'Not found')"
echo "===== END DIAGNOSTICS ====="
