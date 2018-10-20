"""
WSGI application for WSGI servers.

This module is loaded ois called from `.wsgi` module by the WSGI servers (e.g. gunicorn).

This module is loaded separately in each gunicorn worker (an OS process),
i.e. multiple times per a single EC2 instance / Docker container / WSGI server.
Therefore, each worker will have its own database connection pool initialised,
its own logging, and generally fully isolated from other worker processes.

No gevent monkey-patching is needed. It will be already applied before loading
of this module (if gevent workers are used at all), or not needed at all
(if other workers are used, such as threads, tornado, sync, etc).

As a rule of thumb, the WSGI server prepares the environment for our app,
and the app just uses whatever was provided.

This module MUST defined a variable named ``application``, as expected by gunicorn.
"""
from __future__ import absolute_import

from .app import create_connexion_app

application = create_connexion_app().app
