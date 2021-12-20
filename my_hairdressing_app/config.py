import yaml
import etcd3
import json

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
    def __init__(self, test = False):
        """
        Constructor de la entidad.

        Returns
        ----------
        None
        """
        try:
            with open('config.yml', 'r') as stream:
                self.app_config = yaml.load(stream, Loader=yaml.FullLoader)
        except Exception:
            self.app_config = None 

        if self.app_config != None and 'logging' not in self.app_config:
            try:
                etcd = etcd3.client(self.app_config['host'], self.app_config['port'])
                self.app_config['logging'] = json.loads(etcd.get('/config/logging'))
            except Exception:
                self.app_config = Config.get_default_dict_config()
       

        if test:
            try:
                self.app_config['logging']['handlers']['file']['filename'] = '/tmp/app.log' 
            except KeyError:
                raise KeyError('No se ha configurado el nombre de archivo de log correctamente')



    def get_logging_config(self):
        """
        Método que devuelve la configuración del logging.

        Returns
        -------
        logging_config : dict
            Configuración del logging.
        """
        return self.app_config['logging']


    @staticmethod
    def get_default_dict_config():
        """
        Método que devuelve la configuración del logging.

        Returns
        -------
        default_config : dict
            Configuración por defecto de la aplicación.
        """
        return { 
            'logging' : {
                'version': 1, 
                'formatters': {
                    'standard': {
                        'datefmt': '%d-%m-%Y %H:%M:%S', 
                        'format': '%(asctime)s %(levelname)s: %(name)s::%(funcName)s -> (linea %(lineno)d) %(message)s'
                    }
                }, 
                'handlers': {
                    'console': {
                        'level': 'WARNING',
                        'class': 'logging.StreamHandler',
                        'formatter': 'standard',
                        'stream': 'ext://sys.stdout'
                    }, 
                    'file': {
                        'class': 'logging.FileHandler', 
                        'level': 'INFO', 
                        'formatter': 'standard', 
                        'filename': '/var/log/app.log'
                    }, 
                },
                'root': {
                    'level': 'INFO',
                    'handlers': ['console', 'file']
                }
            }
        }
