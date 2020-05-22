#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

from publications_bootstrap import __version__

REPO_URL = "https://github.com/mbourqui/django-publications-bootstrap/"

README = ''
for ext in ['md','rst']:
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.' + ext)) as readme:
            README = readme.read()
    except FileNotFoundError as fnfe:
        pass


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-publications-bootstrap',
    version=__version__,
    author='Marc Bourqui',
    author_email='pypi.kemar@bourqui.org',
    license='MIT',
    description='A Django app for managing scientific publications with a Bootstrap-powered UI.',
    long_description=README,
    url=REPO_URL,
    download_url=REPO_URL + 'releases/tag/v' + __version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.11.29',
        'Pillow>=6.0.0',
        'bibtexparser>=1.1.0',
        'django-countries>=6.0',
        'django-ordered-model>=2.1.0',
        'django-echoices>=2.6',
    ],
    zip_safe=False,
    keywords='django scientific publications citations references bibliography',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
