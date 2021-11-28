FROM python:3.8.10-alpine
LABEL version="0.1.2" maintainer="antoniojr997@gmail.com"

RUN apk update \
    && apk upgrade \
    && apk add bash \
    # Flag -S: creamos el grupo de sistema.
    # Flag -G: indicamos el nombre del grupo donde se añade el usuario.
    && addgroup -S pyAlpine  && adduser -S pyAlpine -G pyAlpine
USER pyAlpine

# Definición del directorio de trabajo.
WORKDIR /app/test    

# Movemos el fichero de depencencias y el fuente del gestor de tareas al directorio de trabajo.
COPY pyproject.toml tasks.py /app/test/

# Añadimos a PATH el directorio para el log de Python.
# ENV PATH = "$PATH:/home/pyContainer/.local/bin"

# Instalamos las dependencias para instalar a su vez el gestor de tareas
# Hacemos la instalación como usuario root ya que algunos paquetes como pyflakes lo necesitan.
USER root 
RUN pip install flit \
    && flit install

# Ejecución de los tests.
USER pyAlpine 
ENTRYPOINT ["invoke", "test"]

