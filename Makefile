.PHONY: build render-start

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

collectstatic:
	python manage.py collectstatic --noinput