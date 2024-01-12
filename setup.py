#!/usr/bin/env python
# encoding=utf-8
# maintainer: Nuradic

from __future__ import absolute_import
from __future__ import unicode_literals
import setuptools

setuptools.setup(
    name="pythopia",
    version="0.0.1",
    license="GNU General Public License (GPL), Version 3",
    provides=["ethiopian_date"],
    description="Ethiopian date converter.",
    long_description=open("README.md").read(),
    url="http://github.com/nuradic/pythopia",
    packages=["ethiopian_date"],
    install_requires=[
        "six>=1.11.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or "
        "Lesser General Public License (LGPL)",
        "Programming Language :: Python",
    ],
)
