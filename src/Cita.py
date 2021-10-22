from datetime import datetime

class Cita:
    """
    Entidad que representa una cita 

    Attributes
    ----------
    telefono : String
        Número de telefono
    dia : datetime
        Tipo datetime que representa la fecha de la cita
    turno : String
        Cadena de texto que almacena el turno en el que se 
        dará la cita, siendo posible tomar los valores:
        mañana o tarde
    tipo_de_cita : dict
        Diccionario que almacenará el tipo de tratamiento, 
        así como el tiempo que se da entre que se comienza, 
        se pausa y se termina el tipo de tratamiento en la 
        peluqueria

    Methods
    -------
    muestra_cita()
        Muestra la cita
    introduce_cita()
        Añade una cita
    """


    def __init__(self,telefono,dia,turno,tipo_de_cita):
        """
        Constructor de la entidad.

        Parameters
        ----------
        telefono : str
        dia : datetime
        turno : str
        tipo_de_cita : dict
        
        """
        self.telefono=telefono
        self.dia=dia
        self.turno=turno
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

    def add_cita(self):
        

    def addd_cita(self,telefono: str,dia: datetime,turno: str,tipo_de_cita: dict):
        """
        Método para añadir una cita

        Parameters
        ----------
        telefono : str
        dia : datetime
        turno : str
        tipo_de_cita : dict

        Returns
        -------
        None
        """
        turno_type = ["maniana","tarde"]
        if (turno_type in turno) == False:
            raise AttributeError("El tipo de turno especificado no es correcto.")
        
        self.telefono = telefono
        self.dia = dia
        self.tipo_de_cita = tipo_de_cita    #Tipo dict
        
        
        
