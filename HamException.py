class HamCodeException(BaseException):
    """
    Custom exceptions for handling errors in HemCode class

    :param Exception: python Exception
    """

    def __init__(self, *args):
        super().__init__(*args)
