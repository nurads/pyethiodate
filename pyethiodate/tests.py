#!/usr/bin/env python
# encoding=utf-8
# maintainer: nuradic

from __future__ import absolute_import
from __future__ import unicode_literals
import unittest
import datetime

from ethiopian_cal import EthDate


class TestEthiopianCalendar(unittest.TestCase):
    def test_gregorian_to_ethiopian(self):
        conv = EthDate.to_ethiopian
        self.assertEqual(conv(1982, 11, 21), EthDate(1975, 3, 12))
        self.assertEqual(conv(1941, 12, 7), EthDate(1934, 3, 28))
        self.assertEqual(conv(2010, 12, 22), EthDate(2003, 4, 13))

    def test_date_gregorian_to_ethiopian(self):
        self.assertEqual(
            EthDate.date_to_ethiopian(datetime.date(1982, 11, 21)),
            EthDate(1975, 3, 12),
        )
        self.assertEqual(
            EthDate.date_to_ethiopian(datetime.date(1941, 12, 7)),
            EthDate(1934, 3, 28),
        )
        self.assertEqual(
            EthDate.date_to_ethiopian(datetime.date(2010, 12, 22)),
            EthDate(2003, 4, 13),
        )

    def test_ethiopian_to_gregorian(self):
        conv = EthDate.to_gregorian
        self.assertEqual(conv(2003, 4, 11).strftime("%F"), "2010-12-20")
        self.assertEqual(conv(1975, 3, 12).strftime("%F"), "1982-11-21")

    def test_date_ethiopian_to_gregorian(self):
        self.assertEqual(
            EthDate.date_to_gregorian(datetime.date(2003, 4, 11)),
            datetime.date(2010, 12, 20),
        )
        self.assertEqual(
            EthDate.date_to_gregorian(datetime.date(1975, 3, 12)),
            datetime.date(1982, 11, 21),
        )


if __name__ == "__main__":
    unittest.main()
