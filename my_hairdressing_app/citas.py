import re
from enum import Enum
from .errores import BadDateFormatError, ShiftNotExistError

class work_shifts(Enum):
    MORNING = 1
    AFTERNOON = 2

SHIFT_TIME_MINUTES = 300

class citas:
    """
    Entidad que representa un conjunto de cita 

    Attributes
    ----------
    
    _citas : dict
        Diccionario que almacenara los objeto valor cita

    Methods
    -------
    aniadir_cita(fecha,turno,cita)

    """

    def __init__(self):
        """
        Constructor de la entidad que contruira un diccionario
        vacio de citas

        Parameters
        ----------
        None
        
        """
        self._citas = {}


    def book_appointment(self, date: str, shift, appointment):
        """
        Función para aniadir citas a la que se pasaran los argumentos
        para formar un diccionario compuesto de citas

        Parameters
        ----------
        date : datetime
            Tipo datetime que representa la fecha de la cita
        shift : String
            Cadena de texto que almacena el turno en el que se 
            dará la cita, siendo posible tomar los valores:
            mañana o tarde
        cita : cita
            Valor objeto de citas que viene representado por un dict
        Returns
        -------
        result : bool
            Resultado de si se puede o no reservar la cita
        """
        preg = re.compile(r'([0-9]{2})-([0-9]{2})-([0-9]{4})')
        if not preg.match(date):
            raise BadDateFormatError(date)
        elif shift not in work_shifts.__members__ and shift not in work_shifts._value2member_map_:
            raise ShiftNotExistError(shift)

        can_book = self.__can_book(date, shift, appointment)
        if can_book:
            self._citas[date][shift].append(appointment)
        
        return can_book


    def __can_book(self, date: str, shift, appointment):
        """
        Función para comprobar si una cita se puede reservar
        en una fecha y turno de trabajo determinado.

        Parameters
        ----------
        fecha : datetime
            Tipo datetime que representa la fecha de la cita
        turno : String
            Cadena de texto que almacena el turno en el que se 
            dará la cita, siendo posible tomar los valores:
            mañana o tarde
        cita : cita
            Valor objeto de citas que viene representado por un dict
        Returns
        -------
        None
        """
        result = True

        if date not in self._citas.keys():
            self._citas[date] = {}
        
        if shift not in self._citas[date].keys():
            self._citas[date][shift] = []   
        else:
            appointments_time_min = 0
            for appt in self._citas[date][shift]:
                duration = appt.getDuration()
                appointments_time_min += sum(duration.values()) - (duration['espera'] if 'espera' in duration.keys() else 0)

            total_time = appointments_time_min + sum(appointment.getDuration().values()) - (appointment.getDuration()['espera'] if 'espera' in appointment.getDuration().keys() else 0) 
            if total_time > SHIFT_TIME_MINUTES:
                result = False

        return result
