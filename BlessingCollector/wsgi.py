"""
WSGI config for BlessingCollector project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from os.path import dirname, abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys
sys.path.append(PROJECT_DIR)

from django.core.wsgi import get_wsgi_application
from utility.functions import init

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BlessingCollector.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "BlessingCollector.settings"

init()

application = get_wsgi_application()
