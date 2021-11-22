FROM python:3.8.0-alpine
LABEL version="0.1.2" maintainer="antoniojr997@gmail.com"

RUN apk update \
    && apk upgrade \
    && apk add bash \
    && addgroup -S pyAlpine  && adduser -S pyAlpine -G pyAlpine
USER pyAlpine

# Definición del directorio de trabajo.
WORKDIR /app/test    

# Movemos el fichero de depencencias y el fuente del gestor de tareas al directorio de trabajo.
COPY . /app/test/

# Añadimos a PATH el directorio para el log de Python.
ENV PATH = "$PATH:/home/pyContainer/.local/bin"

# Instalamos las dependencias para instalar a su vez el gestor de tareas
# Hacemos la instalación como usuario root ya que algunos paquetes como pyflakes lo necesitan.USER root
RUN pip install -r /app/test/requirements.txt

# Ejecución de los tests.
USER pyAlpine
ENTRYPOINT ["invoke", "test"]