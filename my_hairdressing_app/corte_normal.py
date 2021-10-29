from dataclasses import dataclass
@dataclass(frozen=True)
class CorteNormal:
    """
    Entidad que representa una cita 

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
    def __init__(self):
        """
        Contructor sin parametro que le asigna
        un nombre que viene a ser el nombre de 
        la clase y un diccinario que almacena lo
        que tarde por intervalos
        """
        self._nombre='CORTE_NORMAL'
        self._duracion = {
                'tiempo1':20,
                }
