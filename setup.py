#!/usr/bin/env python

import io
import os

from setuptools import find_packages, setup

NAME = 'dns-record-updater'
DESCRIPTION = 'Application for updating DNS records in automatic mode.'
URL = 'https://github.com/opavlov24/dns-record-updater'
EMAIL = 'oleg.pavlov@aol.com'
AUTHOR = 'Oleg Pavlov'
REQUIRES_PYTHON = '>=3.8.0'
VERSION = '0.1.0'

REQUIRED = [
    'requests', 'schedule'
]

EXTRAS = {}

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
)
