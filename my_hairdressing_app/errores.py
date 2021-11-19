class PhoneFormatError (Exception):
    def __inti__(self, message="El telefono debe ser una cadena"):
        self.message = message
