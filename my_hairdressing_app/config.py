import os
import etcd3
from dotenv import load_dotenv

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
        load_dotenv()
        
        dateformat_log = None
        format_log = None
        level_console_log = None
        level_file_log = None
        filename_file_log = None

        self.app_config = None

        try:
            dateformat_log = os.getenv('DATEFORMAT_LOG')
            format_log = os.getenv('FORMAT_LOG')
            level_console_log = os.getenv('LEVEL_CONSOLE_LOG')
            level_file_log = os.getenv('LEVEL_FILE_LOG')
            filename_file_log = os.getenv('FILENAME_FILE_LOG')  
        except Exception:
            pass

        if self.app_config == None:
            try:
                etcd = etcd3.client(self.app_config['host'], self.app_config['port'])

                dateformat_log = etcd.get('/config/logging/DATEFORMAT_LOG')
                format_log = etcd.get('/config/logging/FORMAT_LOG')
                level_console_log = etcd.get('/config/logging/LEVEL_CONSOLE_LOG')
                level_file_log = etcd.get('/config/logging/LEVEL_FILE_LOG')
                filename_file_log = etcd.get('/config/logging/FILENAME_FILE_LOG')
                self.app_config['logging'] = Config.get_dict_config(dateformat_log, format_log, level_console_log, level_file_log, filename_file_log)
            except Exception:
                pass
       
        if dateformat_log != None and format_log != None and level_console_log != None and level_file_log != None and filename_file_log != None:
            self.app_config = Config.get_dict_config(dateformat_log, format_log, level_console_log, level_file_log, filename_file_log)
        else:
            self.app_config = Config.get_dict_config()

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
    def get_dict_config(
        dateformat = '%d-%m-%Y %H:%M:%S',
        format_log = '%(asctime)s %(levelname)s: %(name)s::%(funcName)s -> (linea %(lineno)d) %(message)s',
        level_console = 'WARNING',
        level_file = 'INFO',
        filename_file = '/var/log/app.log'
    ):
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
                        'datefmt': dateformat, 
                        'format': format_log
                    }
                }, 
                'handlers': {
                    'console': {
                        'level': level_console,
                        'class': 'logging.StreamHandler',
                        'formatter': 'standard',
                        'stream': 'ext://sys.stdout'
                    }, 
                    'file': {
                        'class': 'logging.FileHandler', 
                        'level': level_file, 
                        'formatter': 'standard', 
                        'filename': filename_file
                    }, 
                },
                'root': {
                    'level': 'INFO',
                    'handlers': ['console', 'file']
                }
            }
        }

