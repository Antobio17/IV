# Sistema de logging :writing_hand:

## Requisitos
La elección de la biblioteca de logs debe cumplir una serie de requisitos:
- Añadir las minimas dependencias posibles al proyecto.
- Una libreria minimamente mantenida para evitar deprecations.
- Poder hacer logs por archivos y consola.
- Tener la configuración del proyecto unificada en un mismo fichero.

## Logging de Python
_Python_ incorpora un [sistema propio de logging](https://docs.python.org/3/library/logging.config.html). La ventaja de usar este sistema es que no tenemos por que incorporar dependencias para crear nuestros registros, que es nuestro primer requisito de uso. 

Podemos dividir la configuración del _logging_ en tres partes:
1. **Formatters**: darán formato a los mensajes de logging.
2. **Handlers**: en el que se le indicará uno de nuestros _formatters_ y podremos definir la salida del logging (consola, archivo, .etc).
3. **Loggers**: en el que se indicará uno de los _handlers_ creados.

El "inconveniente" del logging vanila de python es la necesidad de tener un fichero donde almacenar la configuración para cargarla posteriormente con una llamada a un método definido.

## Logging518 de Poetry
_Logging518_ resuelve lo comentado anteriormente. Aprovechando el archivo de configuración _pyproject.toml_ donde tenemos configuración de **Poetry** podemos añadir el _logging_ tal y como indica la propia [documentación](https://pypi.org/project/logging518/) del paquete. 

Además no es necesario cargar la configuración tal y como tendríamos que hacer sin _Logging518_, desde un fichero:

```python
import logging
import logging.config

logging.config.fileConfig('logging.conf')
```

Unicamente deberiamos importar el logger con el nombre que hayamos usado. Si hemos llamado _log_ a nuestro logger solo tendriamos que importarlo de la siguiente forma:

```python
from logging518 import log
```

---

Sin embargo si nos decidieramos por **Logging518** puede que en el futuro tengamos problemas de mantenimiento incumpliendo uno de nuestros requisitos. Podemos ver como en [su repositorio](https://github.com/mharrisb1/logging518) unicamente ha trabajado el autor y tiene poca actividad.
Por lo tanto vamos a configurar nuestro logging mediante la biblioteca del core de _Python_.

Se va a usar un archivo **YML** para la configuración de la aplicación que no sea privada y un **dotenv** para la información privada como APIKEYs almacenada como _clave=valor_. Se ha decidido separar esta información ya que en los archivos **YML** podemos montar estructuras de datos o definir tipos para usar configuración mas compleja.