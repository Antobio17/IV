class PhoneFormatError (Exception):
    def __inti__(self, message="El telefono debe ser una cadena"):
        self.message = message
class CitaNameNotExist (Exception):
    def __init__(self, message="El tipo de cita especificada no existe"):
        self.message = message