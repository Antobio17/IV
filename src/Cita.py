

class cita:
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
    get_telefono()
        Nos devuelve el atributo telefono
    get_tipo_de_cita()
        Nos devuelve el atributo tipo de cita
    
    """

    def __init__(self,telefono,nombre_tipo_cita):
        """
        Constructor de la entidad que inicializaremos el numero
        de telefono, así como el nombre del tipo de cita, pues
        con este parametro se puede contruir el diccionario ya que
        los demás valores son contantes en funcion del nombre

        Parameters
        ----------
        telefono : str
        tipo_de_cita : dict
        
        """
        self._telefono=telefono
        self._tipo_de_cita=nombre_tipo_cita
    
    def get_telefono(self):
        """
        Obtiene atributo telefono

        Parameters
        ----------
        None

        Returns
        -------
        self : _telefono
            número de telefono
        """
        return self._telefono

    def get_tipo_de_cita(self):
        """
        obtiene el atributo tipo_de_cita

        Parameters
        ----------
        None

        Returns
        -------
        self : _tipo_de_cita
            tipo de cita que se puede llegar a dar
        """
        return self._tipo_de_cita

    
        
        
        
