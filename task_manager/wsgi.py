"""
WSGI config for task_manager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import rollbar 
from django.core.wsgi import get_wsgi_application
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

application = get_wsgi_application()


if hasattr(settings, 'ROLLBAR') and settings.ROLLBAR.get('access_token'):
    rollbar.init(**settings.ROLLBAR)
