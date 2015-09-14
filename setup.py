#!/usr/bin/env python

from os.path import exists
from version import get_git_version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = "1.0.0"

setup(
    name='django-tenant-schemas',
    version=get_git_version(),
    author='Hovhannes Nurijanyan',
    author_email='hovikn@gmail.com',
    packages=[
        'tenant_schemas',
        'tenant_schemas.postgresql_backend',
        'tenant_schemas.management',
        'tenant_schemas.management.commands',
        'tenant_schemas.management.commands.legacy',
        'tenant_schemas.templatetags',
        'tenant_schemas.test',
        'tenant_schemas.tests',
    ],
    scripts=[],
    url='https://github.com/honur/django-tenants-1.5',
    license='MIT',
    description='Tenant support for Django 1.5 using PostgreSQL schemas.',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Programming Language :: Python',
    ],
    install_requires=[
        'Django == 1.5',
        'psycopg2',
    ],
    zip_safe=False,
)
