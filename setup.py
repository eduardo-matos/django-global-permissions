#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import global_permissions

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = global_permissions.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='django-global-permissions',
    version=version,
    description="""Implementation of permissions not related to models""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Eduardo Matos',
    author_email='eduardo.matos.silva@gmail.com',
    url='https://github.com/eduardo-matos/django-global-permissions',
    packages=[
        'global_permissions',
    ],
    include_package_data=True,
    install_requires=[
        'django>=1.4'
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-global-permissions',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
