FROM python:3.8.10-alpine
LABEL version="0.1.2" maintainer="antoniojr997@gmail.com"

RUN apk update \
    && apk upgrade \
    && apk add bash \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    rust \
    # Flag -S: creamos el grupo de sistema.
    # Flag -G: indicamos el nombre del grupo donde se añade el usuario.
    && addgroup -S pyAlpine  && adduser -S pyAlpine -G pyAlpine \
    && pip install poetry
USER pyAlpine

# Definición del directorio de trabajo.
WORKDIR /app/test    

# Movemos el fichero de depencencias y el fuente del gestor de tareas al directorio de trabajo.
COPY poetry.lock pyproject.toml tasks.py /app/test/

# Añadimos a PATH el directorio para la instalación de dependencias con Poetry
ENV PATH = "$PATH:/home/pyAlpine/.local/bin"

# Instalamos las dependencias para instalar a su vez el gestor de tareas
RUN poetry config virtualenvs.create false \
    && poetry install 

# Ejecución de los tests.
ENTRYPOINT ["invoke", "test"]