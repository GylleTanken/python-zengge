#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages
import sys
import warnings

dynamic_requires = []

version = 0.2

setup(
    name='zengge',
    version=0.2,
    author='Matthew Garrett',
    author_email='mjg59@srcf.ucam.org',
    url='http://github.com/mjg59/python-zengge',
    packages=find_packages(),
    scripts=[],
    description='Python API for controlling Zengge LED bulbs',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
)
