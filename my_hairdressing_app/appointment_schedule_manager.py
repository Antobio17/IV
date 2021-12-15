from my_hairdressing_app.appointment_schedule import AppointmentSchedule
from my_hairdressing_app.logging import Logging
from my_hairdressing_app.errors import BadDateFormatError, ShiftNotExistError

class AppointmentScheduleManager:
    """
    Entidad manejadora del logging en el proceso de la aplicación.

    Methods
    -------
    book_appointment(self, date: str, shift, appointment)
    """
    def __init__(self):
        """
        Constructor de la entidad.

        Parameters
        ----------
        None
        """
        self.schedule = AppointmentSchedule()
        self.logger = Logging(__name__).get_logger()


    def book_appointment(self, date: str, shift, appointment):
        """
        Fachada para manejar la función de reserva de citas de la clase AppointmentSchedule.

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
        
        try:
            can_book = self.schedule.book_appointment(date, shift, appointment)
            if can_book:
                self.logger.info("Se reservó una cita para el día %s para el turno %s." % (date, shift))
            elif not can_book:
                self.logger.info("No se pudo reservar una cita para el día %s para el turno %s." % (date, shift))
        except BadDateFormatError:
            can_book = False
            self.logger.critical("Fecha %s introducida para la reserva de cita no está en el formato correcto." % (date))
        except ShiftNotExistError:
            can_book = False
            self.logger.critical("Turno %s introducido para la reserva de cita no existe." % (shift))            
        
        return can_book