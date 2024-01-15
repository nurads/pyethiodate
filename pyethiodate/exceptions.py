class InvalidYearException(Exception):
    def __init__(self, message="Invalid year input") -> None:
        self.message


class InvalidEthiopianDateAttribute(Exception):
    def __init__(
        self, message="Invalid Attribute for Ethiopian Date", *args: object
    ) -> None:
        self.message = message
        super().__init__(*args)


class InValidDayOfTheMonthException:
    def __init__(
        self, message="Invalid day of the month ethiopian date range 1...30"
    ) -> None:
        self.message = message


class InValidMonthOfTheYearException:
    def __init__(
        self, message="Invalid Month Input: the input should be 1...12"
    ) -> None:
        self.message = message


class InvalidHourException:
    def __init__(self, message="Invalid Hour input") -> None:
        pass


class InvalidMinuteException:
    def __init__(self, message="Invalid Minute input") -> None:
        pass


class InvalidDateException:
    def __init__(self, message="Invalid Date Input") -> None:
        self.message = message
