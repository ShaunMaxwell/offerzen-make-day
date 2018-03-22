#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re


requirements = [
    'flask'
]

version = open('version').read()

setup_args = {
    'name': 'phonealot',
    'version': '0.0.1',
    'description': "insurance chatbot backend webserver",
    'long_description': "backend for a google assistant chatbot for buying and insuring phones",
    'author': "Shaun and Nicky",
    'author_email': 'shaunmaxwell930@gmail.com',
    'url': 'https://github.com/ShaunMaxwell/offerzen-make-day',
    'packages': find_packages(),
    'package_dir': {'webserver': 'webserver'},
    'package_data': {},
    'install_requires': requirements,
    'keywords': '',
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Literally no one',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    'entry_points': {
        'console_scripts': [
            'phonealot=webserver.server:serve',
        ],
    }
}

setup(**setup_args)
