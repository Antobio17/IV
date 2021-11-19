class PhoneFormatError (Exception):
    def __inti__(self, message="El telefono debe ser una cadena"):
        self.message = message
class CitaNameNotExist (Exception):
    def __init__(self, message="El tipo de cita especificada no existe"):
        self.message = message

class BadDateFormatError(Exception):
    """
    Excepción lanzada para errores si la fecha introducida para la reserva de citas
    no tiene el formato adecuado.

    Attributes:
        date -- fecha que ha producido el error.
        message -- texto explicativo del error.
    """

    def __init__(self, date, message = "La fecha introducida no está en el formato correcto. Ejemplo (30-10-2021)."):
        self.date = date
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.date} >> {self.message}'


class ShiftNotExistError(Exception):
    """
    Excepción lanzada para errores si el turno de trabajo introducida para la reserva de citas
    no existe.

    Attributes:
        shift -- turno de trabajo que ha producido el error.
        message -- texto explicativo del error.
    """

    def __init__(self, shift, message = "El turno de trabajo introducido no es existe."):
        self.shift = shift
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.shift} >> {self.message}'