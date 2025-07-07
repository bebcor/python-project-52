.PHONY: build render-start

build:
	./build.sh

render-start:
	gunicorn hexlet_code.wsgi

collectstatic:
	python manage.py collectstatic --noinput