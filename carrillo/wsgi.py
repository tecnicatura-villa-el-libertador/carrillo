"""
WSGI config for carrillo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

# TURN ON THE VIRTUAL ENVIRONMENT FOR YOUR APPLICATION
import os
import sys

# for demo
activate_this = '/home/carrillo/.virtualenvs/carrillo/bin/activate_this.py'
if os.path.exists(activate_this):
    with open(activate_this) as f:
        code = compile(f.read(), activate_this, 'exec')
        exec(code, dict(__file__=activate_this))

path = '/home/carrillo/carrillo'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carrillo.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
