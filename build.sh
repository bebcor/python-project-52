#!/usr/bin/env bash
set -e

# Установка Python зависимостей через стандартный pip
python -m pip install --upgrade pip
pip install -r requirements.txt

# Выполнение команд Django
python manage.py collectstatic --noinput
python manage.py migrate

# Явная установка gunicorn
pip install gunicorn==21.2.0
