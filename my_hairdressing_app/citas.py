from abc import abstractmethod
from cita import *

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

    @abstractmethod
    def aniadir_cita(self,fecha,turno,cita):
        """
        Función para aniadir citas a la que se pasaran los argumentos
        para formar un diccionario compuesto de citas

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
        NotImplemented