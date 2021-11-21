import re
from enum import Enum
from .errors import BadDateFormatError, ShiftNotExistError

class work_shifts(Enum):
    MORNING = 1
    AFTERNOON = 2

SHIFT_TIME_MINUTES = 300

class AppointmentSchedule:
    """
    Entidad que representa una agenda de citas.

    Attributes
    ----------
    
    appointments : dict
        Diccionario que almacenará las citas en un día y turno especifico.

    Methods
    -------
    book_appointment(self, date: str, shift, appointment)

    _can_book(self, date: str, shift, appointment)
    """

    def __init__(self):
        """
        Constructor de la entidad.

        Parameters
        ----------
        None
        """
        self.appointments = {}


    def book_appointment(self, date: str, shift, appointment):
        """
        Función para aniadir citas a la que se pasaran los argumentos para formar un diccionario compuesto de citas.

        Parameters
        ----------
        date : datetime
            Tipo datetime que representa la fecha de la cita.
        shift : String
            Cadena de texto que almacena el turno en el que se dará la cita, siendo posible tomar los valores: mañana o tarde.
        appointment : Appointment
            Objeto valor Appointment que define una cita.

        Returns
        -------
        result : bool
            Resultado de si se puede o no reservar la cita.
        """
        preg = re.compile(r'([0-9]{2})-([0-9]{2})-([0-9]{4})')
        if not preg.match(date):
            raise BadDateFormatError(date)
        elif shift not in work_shifts.__members__ and shift not in work_shifts._value2member_map_:
            raise ShiftNotExistError(shift)

        can_book = self._can_book(date, shift, appointment)
        if can_book:
            self.appointments[date][shift].append(appointment)
        
        return can_book


    def _can_book(self, date: str, shift, appointment):
        """
        Función para comprobar si una cita se puede reservar en una fecha y turno de trabajo determinado.

        Parameters
        ----------
        fecha : datetime
            Tipo datetime que representa la fecha de la cita.
        turno : String
            Cadena de texto que almacena el turno en el que se dará la cita, siendo posible tomar los valores: mañana o tarde.
        appointment : Appointment
            Objeto valor Appointment que define una cita.

        Returns
        -------
        None
        """
        result = True

        if date not in self.appointments.keys():
            self.appointments[date] = {}
        
        if shift not in self.appointments[date].keys():
            self.appointments[date][shift] = []   
        else:
            appointments_time_min = 0
            for appt in self.appointments[date][shift]:
                duration = appt.getDuration()
                appointments_time_min += sum(duration.values()) - (duration['pause_step'] if 'pause_step' in duration.keys() else 0)

            total_time = appointments_time_min + sum(appointment.getDuration().values()) - (appointment.getDuration()['pause_step'] if 'pause_step' in appointment.getDuration().keys() else 0) 
            if total_time > SHIFT_TIME_MINUTES:
                result = False

        return result
