#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

# NB: Monkey-patch ASAP, before any other imports. But once per script!
import gevent.monkey
gevent.monkey.patch_all()

import os
from twocasas_backend_api.app import create_connexion_app


def main():
    app = create_connexion_app()
    port = os.environ.get('PORT', '8080')
    app.run(port=int(port))


if __name__ == '__main__':
    main()
