import logging.config
from my_hairdressing_app.config import Config

class Logging:
    """
    Entidad encargada de instanciar el logging.

    Methods
    -------
    log(self, level: str, message: str)
    """

    @staticmethod
    def info(module_name: str,  message: str, test = False):
        logging.config.dictConfig(Config(test).get_logging_config())
        logging.getLogger(module_name).info(message)

    @staticmethod
    def critical(module_name: str, message: str, test = False):
        logging.config.dictConfig(Config(test).get_logging_config())
        logging.getLogger(module_name).critical(message)

 