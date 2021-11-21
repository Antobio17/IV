from .appointment_type import AppointmentType

class HairColor(AppointmentType):
    """
    Objeto valor que representa el tipo de cita "Tinte".

    Methods
    -------
    None 
    """
    def __init__(self):
        """
        Constructor de la clase.
        """
        super().__init__(
            'hair_color',
            {                
                'first_working_step'  : 15,
                'pause_step'          : 30,
                'second_working_step' : 10,
            }
        )

        


