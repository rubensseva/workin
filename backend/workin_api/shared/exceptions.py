class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class TokenAuthError(Error):
    """Exception raised for errors on token auth

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class ResourceNotFoundError(Error):
    """Exception raised for errors on token auth

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class MissingURLParamError(Error):
    """Exception raised for errors on token auth

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
