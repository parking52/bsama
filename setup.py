#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
import inspect
import platform

__location__ = os.path.join(os.getcwd(), os.path.dirname(inspect.getfile(inspect.currentframe())))
py_major_version, py_minor_version = 3, 6


def get_install_requirements(path):
    content = open(os.path.join(__location__, path)).read()
    requires = [req for req in content.split('\\n') if req != '']
    if py_major_version == 2 or (py_major_version == 3 and py_minor_version < 4):
        requires.append('pathlib')
    return requires
setup(
    name='twocasas-backend-api',
    author='ASF team',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'twocasas_backend_api': ['swagger.yaml']},
    zip_safe=False,
    scripts=[
        os.path.join('bin', 'twocasas-backend-api-application.py'),
    ],
    # setup_requires=['pytest-runner'],
    install_requires=get_install_requirements('requirements.txt'),
    dependency_links=[
    ],
    # extras_require={
    #     'tests': [
    #         'pytest-flask',
    #         'pytest-mock',
    #         'pytest',
    #         'pytest-cov',
    #     ],
    # },
)
