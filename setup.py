#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    yjd API

    :license: MIT, see LICENSE for more details

'''
from setuptools import setup


setup(
    name='yjd',
    version="0.0.1",
    url='https://github.com/dvdhinesh/python-yjd/',
    license='MIT',
    author='Dhinesh D',
    author_email='dvdhinesh.mail@gmail.com',
    description='YJD API Client',
    long_description=open('README.rst').read(),
    packages=['yjd'],
    platforms='any',
    install_requires=[
        'zeep',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
