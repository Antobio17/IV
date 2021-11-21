from .appointment_type import AppointmentType

class NormalHaircut(AppointmentType):
    """
    Objeto valor que representa el tipo de cita "Corte normal".

    Methods
    -------
    None
    """
    def __init__(self):
        """
        Constructor de la clase.
        """
        super().__init__(
            'normal_haircut',
            {                
                'first_working_step'  : 20,
            }
        )
