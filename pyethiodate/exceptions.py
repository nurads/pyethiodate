class InvalidEthiopianDateAttribute(Exception):
    def __init__(
        self, message="Invalid Attribute for Ethiopian Date", *args: object
    ) -> None:
        self.message = message
        super().__init__(*args)
