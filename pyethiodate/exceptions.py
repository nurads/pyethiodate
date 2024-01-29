class InvalidEthiopianDateAttribute(Exception):
    def __init__(
        self, message="Invalid Attribute for Ethiopian Date", *args: object
    ) -> None:
        super().__init__(message,*args)
