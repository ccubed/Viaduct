#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'redis', 'telnetsrv', 'greenlet', 'gevent', 'simplejson', 'cryptography'
]

setup(
    name='viaduct',
    version='0.0.1',
    description="Next Generation Mu Server",
    long_description=readme + '\n\n' + history,
    author="Charles Click",
    author_email='ccubed.techno@gmail.com',
    url='https://github.com/ccubed/viaduct',
    packages=[
        'viaduct',
    ],
    package_dir={'viaduct'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    keywords='viaduct',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
