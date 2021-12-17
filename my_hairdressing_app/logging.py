import logging.config
from my_hairdressing_app.config import Config

class Logging:
    """
    Entidad encargada de instanciar el logging.

    Methods
    -------
    log(self, level: str, message: str)
    """
    def __init__(self, module_name: str, test = False):
        """
        Constructor de la entidad.

        Parameters
        ----------
        None
        """
        logging.config.dictConfig(Config(test).get_logging_config())
        self.logger = logging.getLogger(module_name)

    def get_logger(self):
        return self.logger
 