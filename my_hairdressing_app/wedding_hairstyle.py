from .appointment_type import AppointmentType

class WeddingHairstyle(AppointmentType):
    """
    Objeto valor que representa el tipo de cita "Peinados de boda".

    Methods
    -------
    None
    
    """
    def __init__(self):
        """
        Constructor de la clase.
        """
        super().__init__(
            'wedding_hairstyle',
            {                
                'first_working_step'  : 10,
                'pause_step'          : 15,
                'second_working_step' : 10,
            }
        )
