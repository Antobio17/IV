from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class AppointmentType(ABC):
    """
    Clase abstracta que representa un tipo de cita.

    Methods
    -------
    getDuration(self)
    """

    def __init__(self, name: str, duration: dict):
        """
        Contructor sin parametro que le asigna
        un nombre que viene a ser el nombre de 
        la clase y un diccinario que almacena lo
        que tarde por intervalos

        Attributes
        ----------
        name : String
            Nombre que identificativo del tipo de cita.
        duration : dict
            Diccionario que almacenará la duración y los tiempos por los que trascurre el tipo de cita.
        """
        self.name = name
        self.duration = duration


    def getDuration(self):
        """
        Método que devuelve la propiedad duration del objeto valor.

        Returns
        -------
        duration : dict
            Diccionario que almacenará la duración y los tiempos por los que trascurre el tipo de cita.
        """
        return self.duration
