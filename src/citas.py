from datetime import datetime

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

    Methods
    -------
    muestra_cita()
        Muestra la cita
    introduce_cita()
        Añade una cita
    """

    def __init__(self,ident,fecha,turno):
        self._ident=ident
        self._fecha=fecha
        self._turno=turno

