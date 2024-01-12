#!/usr/bin/env python
# encoding=utf-8
# maintainer: nuradic

""" Ethiopian Date Converter

Convert from Ethiopian date to Gregorian date (and vice-versa)

Examples:

greg_date = EthiopianDateConverter.to_gregorian(2003, 4, 11)
ethi_date = EthiopianDateConverter.date_to_ethiopian(datetime.date.today())

"""

from __future__ import absolute_import

from __future__ import unicode_literals
from .ethiopian_cal import EthDate
