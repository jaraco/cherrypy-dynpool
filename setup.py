#!/usr/bin/env python

from setuptools import setup


setup_args = dict(
    name='cherrypy-dynpool',
    version='2.2.3',
    url='https://github.com/tabo/cherrypy-dynpool/',
    author='Gustavo Picon',
    author_email='tabo@tabo.pe',
    license='Apache License 2.0',
    py_modules=['cherrypy_dynpool'],
    description='A dynamic thread pool tool for CherryPy.',
    install_requires=[
        "CherryPy>=3.2",
        "dynpool>=2.0,<3.0"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries'])

if __name__ == '__main__':
    setup(**setup_args)
