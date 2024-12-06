# The asgi.py file is similar in purpose to the wsgi.py file but is designed for ASGI (Asynchronous Server Gateway Interface) 
# instead of WSGI. ASGI is a newer standard that supports asynchronous communication, 
# making it suitable for modern web applications that require real-time features like WebSockets, background tasks, and long-lived connections.

"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
# This docstring provides a brief overview of the file's purpose. It mentions that
# this file contains the ASGI configuration for the 'mysite' project and exposes
# the ASGI application callable as a module-level variable named 'application'.
# The URL provided directs you to the Django documentation for more details.

import os
# The 'os' module is imported to interact with the operating system. This is used to
# set environment variables.

from django.core.asgi import get_asgi_application
# The 'get_asgi_application' function is imported from 'django.core.asgi'. This function
# creates an ASGI application that can be used by any ASGI server to forward requests
# to your Django application.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# This line sets the 'DJANGO_SETTINGS_MODULE' environment variable to 'mysite.settings'.
# This tells Django which settings file to use. The 'setdefault' method is used here to
# set the environment variable only if it hasn't been set already. This ensures that
# Django uses the correct configuration for your project.

application = get_asgi_application()
# The 'get_asgi_application' function is called, and the resulting ASGI application is
# assigned to the 'application' variable. This variable is a callable that the ASGI server
# uses to forward requests to your Django application. The ASGI server invokes this callable
# for every request it receives, and it is responsible for handling the request and returning
# a response.
