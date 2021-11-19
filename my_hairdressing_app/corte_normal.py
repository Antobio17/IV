from .tipo_cita import tipo_cita

class CorteNormal(tipo_cita):
    """
    Objeto valor que representa un tipo de cita 

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
        Contructor que llama al contructor padre del que hereda
        al cual le pasa un _nombre y una _duracion
        """
        _nombre='CORTE_NORMAL'
        _duracion = {
                'tiempo1':20,
                }
        super().__init__(_nombre,_duracion)
