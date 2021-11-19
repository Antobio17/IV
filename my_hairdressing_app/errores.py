class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class error_cita (Error):
    
    def __inti__(self, message):
        self.message = message

#https://docs.python.org/es/3/tutorial/errors.html#user-defined-exceptions