from dataclasses import dataclass
from enum import Enum
from .normal_haircut import NormalHaircut
from .hair_color import HairColor
from .wedding_hairstyle import WeddingHairstyle
from .errors import AppointmentTypeNotExistError, PhoneNumberFormatError

appointment_types = {
    'normal_haircut'    : NormalHaircut(),
    'hair_color'        : HairColor(),
    'wedding_hairstyle' : WeddingHairstyle(),
}

@dataclass(frozen=True)
class Appointment:
    """
    Objeto valor que representa una cita

    Attributes
    ----------
    phone_number : String
        Número de telefono del cliente al que pertenece la cita.
    appointment_type : AppointmentType
        Objeto valor que representa el tipo de cita.

    Methods
    -------
    get_tipo_de_cita()
        Nos devuelve el atributo tipo de cita
    
    """

    def __init__(self, phone_number: str, name_appointment_type):
        """
        Constructor del objeto valor.

        Parameters
        ----------
        phone_number : str
            Número de teléfono del cliente.
        name_appointment_type : str|int
            Nombre del tipo de cita para su elección.
        """
        if type(phone_number) != str:
            raise PhoneNumberFormatError()
        elif (name_appointment_type not in appointment_types.keys()):
            raise AppointmentTypeNotExistError()
            

        self.phone_number = phone_number
        self.appointment_type = appointment_types[name_appointment_type]
        