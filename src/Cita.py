from datetime import datetime

class Cita:
    """
    Entidad que representa una cita 

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
    get_cita()
        Muestra la cita
    """


    def __init__(self,telefono,tipo_de_cita):
        """
        Constructor de la entidad.

        Parameters
        ----------
        telefono : str
        tipo_de_cita : dict
        
        """
        self.telefono=telefono
        self.tipo_de_cita=tipo_de_cita #Esta tiene que ser un diccionario
    
    def get_cita(self):
        """
        Obtiene una cita

        Parameters
        ----------
        None

        Returns
        -------
        self : Cita
            Objeto de tipo cita
        """
        return self

    
        
        
        
