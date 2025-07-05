.PHONY: install collectstatic migrate

install:
	uv pip install -r requirements.txt

collectstatic:
	python manage.py collectstatic --noinput

migrate:
	python manage.py migrate