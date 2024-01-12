#!/usr/bin/env python
# encoding=utf-8
# maintainer: Nuradic

from __future__ import absolute_import
from __future__ import unicode_literals
import setuptools

decs = """
calendar and vice-versa.
It is a fork from ethiopian_date package to insure better maintainance
Installation
------------

    pip install pyethiodate
"""
setuptools.setup(
    name="pyethiodate",
    version="1.0.0",
    license="GNU General Public License (GPL), Version 3",
    provides=["pythopia"],
    description="Ethiopian date converter.",
    long_description=decs,
    url="http://github.com/nuradic/pyethiodate",
    author="Murad",
    author_email="nuradhussen082@gmail.com",
    packages=["pyethiodate"],
    install_requires=[
        "six>=1.16.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or "
        "Lesser General Public License (LGPL)",
        "Programming Language :: Python",
    ],
)
