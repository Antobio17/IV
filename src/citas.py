from cita import *

class citas:
    """
    Entidad que representa una cita 

    Attributes
    ----------
    ident : int
        Identificador de cita
    fecha : datetime
        Tipo datetime que representa la fecha de la cita
    turno : String
        Cadena de texto que almacena el turno en el que se 
        dará la cita, siendo posible tomar los valores:
        mañana o tarde
    cita : cita
        Valor objeto de citas

    Methods
    -------
    set_cita(fecha,turno,cita)

    """

    def __init__(self):
        self._citas = {}

    def set_cita(self,ident,fecha,turno,cita): 
        None

