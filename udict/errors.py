
class PageStatusError(Exception):
    """Raise when page status code is not 200 or 202."""
    def __init__(self, status_code):
        self.status_code = status_code
        self.message = f"Page status code is {status_code}!"

    def __str__(self):
        return self.message

