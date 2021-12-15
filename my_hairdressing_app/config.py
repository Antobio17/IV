import yaml

class Config:
    """
    Entidad encargada de cargar la configuración de la app.

    Attributes
    ----------
    config : dict
        Diccionario que almacenará la configuración de la aplicación.

    Methods
    -------
    get_logging_config(self, date: str, shift, appointment)
    """
    def __init__(self):
        """
        Constructor de la entidad.

        Returns
        ----------
        None
        """
        with open('config.yml', 'r') as stream:
            self.app_config = yaml.load(stream, Loader=yaml.FullLoader)

    def get_logging_config(self):
        """
        Método que devuelve la configuración del logging.

        Returns
        -------
        logging_config : dict
            Configuración del logging.
        """
        return self.app_config['logging']