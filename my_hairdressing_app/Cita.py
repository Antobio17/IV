from dataclasses import dataclass
from enum import Enum
from .corte_normal import CorteNormal
from .tinte import Tinte
from .peinados_para_boda import PeinadosParaBoda


class tipo_cita(Enum):
    CORTE_NORMAL = 1
    TINTE = 2
    PEINADOS_PARA_BODA = 3

@dataclass(frozen=True)
class cita:
    """
    Entidad que representa un objeto valor cita 

    Attributes
    ----------
    telefono : String
        Número de telefono
    tipo_de_cita : dict
        Diccionario que almacenará el tipo de tratamiento, 
        así como el tiempo que se da entre que se comienza, 
        se pausa y se termina el tipo de tratamiento en la 
        peluqueria

    Methods
    -------
    get_tipo_de_cita()
        Nos devuelve el atributo tipo de cita
    
    """

    def __init__(self,telefono,nombre_tipo_cita):
        """
        Constructor del objeto valor que inicializaremos el numero
        de telefono, así como el nombre del tipo de cita, pues
        con este parametro se puede contruir el diccionario ya que
        los demás valores son contantes en funcion del nombre

        Parameters
        ----------
        telefono : str
        nombre_tipo_cita : str
        
        """
        if type(telefono)!=str:
            raise AttributeError("El teléfono debe ser una cadena")

        if (nombre_tipo_cita in tipo_cita.members):
            raise AttributeError("El tipo de cita especificada no es correcta.")
            

        self._telefono=telefono

        if nombre_tipo_cita == "CORTE_NORMAL":
            self._tipo_de_cita = CorteNormal()
            
        elif nombre_tipo_cita == "TINTE":
            self._tipo_de_cita = Tinte()

        elif nombre_tipo_cita == "PEINADOS_PARA_BODA":
            self._tipo_de_cita = PeinadosParaBoda()

    def get_tipo_de_cita(self):
        """
        obtiene el atributo tipo_de_cita

        Parameters
        ----------
        None

        Returns
        -------
        self : _tipo_de_cita
            Tipo de cita que se puede llegar a dar
        """
        return self._tipo_de_cita