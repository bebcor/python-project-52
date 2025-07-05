install:
    uv pip install -r requirements.txt

collectstatic:
    python manage.py collectstatic --noinput

migrate:
    python manage.py migrate

render-start:
    $HOME/.local/bin/gunicorn task_manager.wsgi

.PHONY: install collectstatic migrate render-start
