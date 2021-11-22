# Contendor :computer:

Para la contenerización de la aplicación se ha usado _**Docker**_, tecnología de creación de contenedores que permite la creación y el uso de contenedores de Linux. 

## Elección del contenedor _base_ :house:

Existen diferentes versiones de Python montadas en distintas distribuciones Linux. Nuestro objetivo es elegir un contenedor base lo mas simple posible en el que no tengamos carga extra la cual no usaremos pero si todo lo necesario para montar y correr nuestra aplicación.

Unas de las primeras opciones consideradas como contenedor base ha sido `python:3.8.0-alpine`, sin embargo buscando información he encontrado que puede causar algunos problemas la contrucción de un contenedor sobre esta versión y ser mucho mas lenta y pesada que otras ([+info](https://pythonspeed.com/articles/alpine-docker-python/)):

> Most Python packages these days include binary wheels on PyPI, significantly speeding install time. But if you’re using Alpine Linux you need to compile all the C code in every Python package that you use.

Pero para realmente comprobar la veracidad de esto, la mejor opción es configurar nuestro _**Dockerfile**_ y ejecutarlo nosotros mismos. Vamos a considerar dos contenedores base para realizar las correspondientes pruebas: `python:3.8.0-alpine` y `python:3.8.0-slim`.

### python:3.8.0-alpine

Partiendo de un Dockerfile lo mas simple posible se han hecho pruebas de construcción del contenedor para ver que problemas nos podíamos encontrar:
- El primer "problema" que nos hemos encontrado ha sido la necesidad de ejecutar la instalación de las dependencias como usuario _root_. Para ello se ha usado el usuario con privilegios únicamente para esa instalación.
- El segundo y último incomveniente ha surgido a la hora de ejecutar el contendor ya que era necesaria la instalación previa de _bash_ para el uso de **invoke**.

Para medir el tiempo que tarda en construirse el contenedor se ha lanzado el comando:

```shell
time docker --no-cache build .
```

Obteniendo la salida:

```shell
Successfully built 529533260c3e

real	0m10,392s
user	0m0,070s
sys	    0m0,069s
```

### python:3.8.0-slim

Partiendo de un Dockerfile lo mas simple posible se han hecho pruebas de construcción del contenedor para ver que problemas nos podíamos encontrar. Esta vez solo hemmos tenido que solucionar el problema del usuario con privilegios (como era obvio). Sin embargo no hemos tenido que instalar otros paquetes como _bash_.

Para medir el tiempo que tarda en construirse el contenedor se ha vuelto a lanzar el comando:

```shell
time docker build --no-cache .
```

Obteniendo la salida:

```shell
Successfully built 5bfec2d103cc

real	0m11,869s
user	0m0,088s
sys	    0m0,062s
```


Como podemos observar el tiempo es muy similar, únicamente se diferencian en un segundo.
Se va a proceder por tanto a usar la imagen base de **alpine** para _Python_ ya que, aunque por poco ha sido mas rápida, la ejecución de los test no ha lanzado ningún warning al contrario que la version _slim_.

## DockerHub :whale:

El contendor ha sido publicado en [este enlace](https://hub.docker.com/repository/docker/antobio17/my_hairdressing_app/) por medio de una _Github Action_. Para la configuración de esta se han seguido los pasos [_Github_](https://docs.github.com/es/actions/publishing-packages/publishing-docker-images). Lo que si vamos a modificar en esta Github Action es cuando se lanzará. Añadiremos las opciones de Pull Request a la rama main y push en cualquier rama del repositorio unicamente cuando se modifique el Dockerfile.