from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class tipo_cita(ABC):
    """
    Clase padre abstracta que contiene lo básico que tiene un tipo de cita
    """
    @abstractmethod
    

    def __init__(self,_nombre,_duracion):
        """
        Contructor sin parametro que le asigna
        un nombre que viene a ser el nombre de 
        la clase y un diccinario que almacena lo
        que tarde por intervalos

        Attributes
        ----------
        nombre : String
            nombre que tiene este tipo de cita
        duracion : dict
            Diccionario que almacenará el tiempo que 
            se da entre que se comienza, 
            se pausa y se termina el tipo de 
            tratamiento en la peluqueria

        Methods
        -------
        None
        """
        self._nombre=_nombre
        self._duracion=_duracion

    def getDuration(self):
        """
        Método que devuelve la propiedad _duración del objeto valor.

        Returns
        -------
        _duracion : str
            Duración de la cita.
        """
        return self._duracion
