#!/usr/bin/env python
# encoding=utf-8
# maintainer: nuradic

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import datetime
from datetime import timedelta
from six.moves import range
from exceptions import *


class EthDate:
    eth_months = [
        "Meskerem",
        "Tikimt",
        "Hidar",
        "Tahsas",
        "Tir",
        "Yekatit",
        "Megabit",
        "Miazia",
        "Ginbot",
        "Sene",
        "Hamle",
        "Nehase",
        "Pagume",
    ]

    @property
    def month_name(self):
        return EthDate.eth_months[self.month - 1]

    @property
    def weekDay(
        self,
    ):
        return 1

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}.{}".format(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second,
            self.microsecond,
        )

    def __init__(
        self,
        year: int = None,
        month: int = None,
        day: int = None,
        hour: int = None,
        minute: int = None,
        second: int = None,
        microsecond: int = None,
        date: datetime.datetime = None,
    ) -> None:
        if date:
            date = EthDate.date_to_ethiopian(date)
            self.year = date.year
            self.month = date.month
            self.day = date.day
            self.hour = date.hour
            self.minute = date.minute
            self.second = date.second
            self.microsecond = date.microsecond
            return
        date = datetime.datetime.now()
        date = EthDate.to_ethiopian(
            date.year,
            date.month,
            date.day,
            date.hour,
            date.minute,
            date.second,
            date.microsecond,
        )
        if not year:
            year = date["year"]
        if not month:
            month = date["month"]
        if not day:
            day = date["day"]
        if not hour:
            hour = date["hour"]
        if not minute:
            minute = date["minute"]
        if not second:
            second = date["second"]
        if not microsecond:
            microsecond = date["microsecond"]
        if year > datetime.MAXYEAR or year < datetime.MINYEAR:
            raise InvalidYearException()
        self.year = year
        if month < 1 or month > 12:
            raise InValidMonthOfTheYearException()
        self.month = month

        if day < 1 or day > 30:
            raise InValidDayOfTheMonthException()
        if day > 6 and month == 13:
            raise InValidDayOfTheMonthException()
        self.day = day
        if hour < 0 or hour > 23:
            raise InvalidEthiopianDateAttribute(
                message="Invalid hour : valid only 0...23"
            )
        self.hour = hour

        if minute < 0 or minute > 59:
            raise InvalidEthiopianDateAttribute(
                message="Invalid minute : valid only 0...59"
            )
        self.minute = minute
        if day < 0 or day > 59:
            raise InvalidEthiopianDateAttribute(
                message="Invalid second : valid only 0...59"
            )
        self.second = second

        if microsecond < 0 or microsecond > 999999:
            raise InvalidEthiopianDateAttribute(
                message="Invalid microsecond : valid only 0...999999"
            )
        self.microsecond = microsecond

    # Define EthDate Operators
    def __le__(self, __value):
        pass

    def __sub__(self, __value: timedelta):
        date = EthDate.date_to_ethiopian(EthDate.date_to_gregorian(self) - __value)
        return date

    def __add__(self, __value: timedelta):
        date = EthDate.date_to_ethiopian(EthDate.date_to_gregorian(self) + __value)
        return date
        total_sec = __value.total_seconds()
        days, left_sec = total_sec // (24 * 60 * 60), total_sec % (24 * 60 * 60)
        hours, left_sec = left_sec // (60 * 60), left_sec % (60 * 60)
        minutes, left_sec = left_sec // 60, left_sec % 60
        seconds = int(left_sec)

        total_day = self.day + days
        day, add_month = total_day % 30, total_day // 30

        # Handle month 13 5 or 6 days
        total_month = self.month + add_month
        month, add_year = total_month % 12, total_month // 12

        total_year = self.year + add_year
        return EthDate(
            year=int(total_year),
            month=int(month),
            day=int(day),
            hour=int(hours),
            minute=int(minutes),
            second=int(seconds),
            microsecond=__value.microseconds,
        )

    def __lt__(self, __value):
        return (
            self.year < __value.year
            or self.month < __value.month
            or self.day < __value.day
        )

    def __lte__(self, __value):
        pass

    def __eq__(self, __value: object) -> bool:
        return (
            __value.year == self.year
            and __value.month == self.month
            and __value.day == self.day
        )

    @staticmethod
    def _start_day_of_ethiopian(year):
        """returns first day of that Ethiopian year

        Params:
        * year: an int"""

        # magic formula gives start of year
        new_year_day = (year // 100) - (year // 400) - 4

        # if the prev ethiopian year is a leap year, new-year occrus on 12th
        if (year - 1) % 4 == 3:
            new_year_day += 1

        return new_year_day

    @staticmethod
    def date_to_ethiopian(date: datetime.datetime):
        """Ethiopian date object representation of provided Gregorian date

        Shortcut to to_ethiopian() classmethod using a date parameter

        Params:
        * adate: date object"""
        return EthDate.to_ethiopian_date(
            date.year,
            date.month,
            date.day,
            date.hour,
            date.minute,
            date.second,
            date.microsecond,
        )

    @staticmethod
    def to_ethiopian(
        year,
        month,
        date,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    ):
        """Ethiopian date string representation of provided Gregorian date

        Params:
        * year: an int
        * month: an int
        * date: an int"""

        # prevent incorect input
        inputs = (year, month, date)
        if 0 in inputs or [data.__class__ for data in inputs].count(int) != 3:
            raise ValueError("Malformed input can't be converted.")

        # date between 5 and 14 of May 1582 are invalid
        if month == 10 and date >= 5 and date <= 14 and year == 1582:
            raise ValueError("Invalid Date between 5-14 May 1582.")

        # Number of days in gregorian months
        # starting with January (index 1)
        # Index 0 is reserved for leap years switches.
        gregorian_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Number of days in ethiopian months
        # starting with January (index 1)
        # Index 0 is reserved for leap years switches.
        ethiopian_months = [0, 30, 30, 30, 30, 30, 30, 30, 30, 30, 5, 30, 30, 30, 30]

        # if gregorian leap year, February has 29 days.
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            gregorian_months[2] = 29

        # September sees 8y difference
        ethiopian_year = year - 8

        # if ethiopian leap year pagumain has 6 days
        if ethiopian_year % 4 == 3:
            ethiopian_months[10] = 6
        else:
            ethiopian_months[10] = 5

        # Ethiopian new year in Gregorian calendar
        new_year_day = EthDate._start_day_of_ethiopian(year - 8)

        # calculate number of days up to that date
        until = 0
        for i in range(1, month):
            until += gregorian_months[i]
        until += date

        # update tahissas (december) to match january 1st
        if ethiopian_year % 4 == 0:
            tahissas = 26
        else:
            tahissas = 25

        # take into account the 1582 change
        if year < 1582:
            ethiopian_months[1] = 0
            ethiopian_months[2] = tahissas
        elif until <= 277 and year == 1582:
            ethiopian_months[1] = 0
            ethiopian_months[2] = tahissas
        else:
            tahissas = new_year_day - 3
            ethiopian_months[1] = tahissas

        # calculate month and date incremently
        m = 0
        for m in range(1, ethiopian_months.__len__()):
            if until <= ethiopian_months[m]:
                if m == 1 or ethiopian_months[m] == 0:
                    ethiopian_date = until + (30 - tahissas)
                else:
                    ethiopian_date = until
                break
            else:
                until -= ethiopian_months[m]

        # if m > 4, we're already on next Ethiopian year
        if m > 10:
            ethiopian_year += 1

        # Ethiopian months ordered according to Gregorian
        order = [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4]
        ethiopian_month = order[m]

        return {
            "year": ethiopian_year,
            "month": ethiopian_month,
            "day": ethiopian_date,
            "hour": hour,
            "minute": minute,
            "second": second,
            "microsecond": microsecond,
        }

    @staticmethod
    def to_ethiopian_date(
        year,
        month,
        date,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    ):
        kwargs = EthDate.to_ethiopian(
            year,
            month,
            date,
            hour,
            minute,
            second,
            microsecond,
        )

        return EthDate(**kwargs)

    @staticmethod
    def to_gregorian(year, month, date, hour=0, minute=0, second=0, microsecond=0):
        """Gregorian date object representation of provided Ethiopian date

        Params:
        * year: an int
        * month: an int
        * date: an int"""

        # prevent incorect input
        inputs = (year, month, date)
        if 0 in inputs or [data.__class__ for data in inputs].count(int) != 3:
            raise ValueError("Malformed input can't be converted.")

        # Ethiopian new year in Gregorian calendar
        new_year_day = EthDate._start_day_of_ethiopian(year)

        # September (Ethiopian) sees 7y difference
        gregorian_year = year + 7

        # Number of days in gregorian months
        # starting with September (index 1)
        # Index 0 is reserved for leap years switches.
        gregorian_months = [0, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30]

        # if next gregorian year is leap year, February has 29 days.
        next_year = gregorian_year + 1
        if (next_year % 4 == 0 and next_year % 100 != 0) or next_year % 400 == 0:
            gregorian_months[6] = 29

        # calculate number of days up to that date
        until = ((month - 1) * 30) + date
        if until <= 37 and year <= 1575:  # mysterious rule
            until += 28
            gregorian_months[0] = 31
        else:
            until += new_year_day - 1

        # if ethiopian year is leap year, paguemain has six days
        if year - 1 % 4 == 3:
            until += 1

        # calculate month and date incremently
        m = 0
        for i in range(0, gregorian_months.__len__()):
            if until <= gregorian_months[i]:
                m = i
                gregorian_date = until
                break
            else:
                m = i
                until -= gregorian_months[i]

        # if m > 4, we're already on next Gregorian year
        if m > 4:
            gregorian_year += 1

        # Gregorian months ordered according to Ethiopian
        order = [8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        gregorian_month = order[m]

        return datetime.datetime(
            gregorian_year,
            gregorian_month,
            gregorian_date,
            hour,
            minute,
            second,
            microsecond,
        )

    @staticmethod
    def date_to_gregorian(adate):
        """Gregorian date object representation of provided Ethiopian date

        Shortcut to to_gregorian() classmethod using a date parameter

        Params:
        * adate: date object"""

        return EthDate.to_gregorian(
            adate.year,
            adate.month,
            adate.day,
            adate.hour,
            adate.minute,
            adate.second,
            adate.microsecond,
        )


n = EthDate()

# print(n.hour)
n2 = n + datetime.timedelta(days=30 * 12)
# # n < n2
print(n)
print(n2)

# diff = timedelta(days=2, hours=2 * 1)
# print(diff.days, diff.seconds)
