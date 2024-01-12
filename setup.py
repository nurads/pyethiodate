#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from __future__ import absolute_import
from __future__ import unicode_literals
import setuptools

setuptools.setup(
    name='ethiopian_date',
    version='1.0',
    license='GNU General Public License (GPL), Version 3',

    provides=['ethiopian_date'],

    description='Ethiopian date converter.',
    long_description=open('README.rst').read(),

    url='http://github.com/rgaudin/tools',

    packages=['ethiopian_date'],

    install_requires=[
        'six>=1.11.0',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or '
        'Lesser General Public License (LGPL)',
        'Programming Language :: Python',
    ],
)
