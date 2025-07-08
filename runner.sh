#!/bin/bash
set -e

export PYTHONPATH=/project:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=task_manager.settings

cd /project

uv run pytest -vv tests