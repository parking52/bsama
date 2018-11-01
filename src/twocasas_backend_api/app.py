from __future__ import absolute_import

import connexion
from flask_compress import Compress
from pkg_resources import resource_filename
from werkzeug.contrib.fixers import ProxyFix

SWAGGER_FILE = 'swagger.yaml'


def create_connexion_app():
    """
    Create a `connexion` app with the swagger API loaded.

    The execution environment is not touched, and assumed to be initialised
    separately. This method is used both in the creation of a WSGI run-time app,
    and in the tests/fixtures without the databases/logging.
    """

    app = connexion.App(__name__, port=8080, debug=False)
    app.add_api(resource_filename('twocasas_backend_api', SWAGGER_FILE))
    app.app.wsgi_app = ProxyFix(app.app.wsgi_app)
    Compress().init_app(app.app)
    return app
