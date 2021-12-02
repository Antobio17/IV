FROM python:3.8.10-slim
LABEL version="0.1.2" maintainer="antoniojr997@gmail.com"

RUN apt-get update \
    # Al ser la versión slim del contenedor necesitamos instalar la libreria gcc.
    # && apt-get install gcc -y \
    && pip install poetry \
    # && apt-get clean \
    # Creamos el usuario:
        # Flag -r: crea una cuenta del sistema.
        # Flag -m: crea el directorio personal del usuario.
        # Flag -g: indicamos el nombre del grupo primario de la nueva cuenta.
    && groupadd -r pyContainer && useradd -m -g pyContainer pyContainer
USER pyContainer

# Definición del directorio de trabajo.
WORKDIR /app/test

# Movemos el fichero de depencencias y el fuente del gestor de tareas al directorio de trabajo.
COPY poetry.lock pyproject.toml tasks.py /app/test/

# Añadimos a PATH el directorio para el log de Python.
ENV PATH = "$PATH:/home/pyContainer/.local/bin"
 

# Instalamos las dependencias para instalar a su vez el gestor de tareas
RUN poetry config virtualenvs.create false \
    && poetry install

# Ejecución de los tests.
USER pyContainer
ENTRYPOINT ["invoke", "test"]