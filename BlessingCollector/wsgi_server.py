"""
WSGI config for BlessingCollector project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from os.path import dirname, abspath
from django.core.wsgi import get_wsgi_application
from utility.functions import init

PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys
sys.path.insert(0,PROJECT_DIR)

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BlessingCollector.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "BlessingCollector.settings"

init()

application = get_wsgi_application()
