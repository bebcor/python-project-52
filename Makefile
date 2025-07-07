.PHONY: build render-start

build:
	./build.sh

render-start:
	/opt/render/project/python/Python-3.10.12/bin/gunicorn task_manager.wsgi

collectstatic:
	python manage.py collectstatic --noinput