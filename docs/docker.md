# Contendor :computer:

Para la contenerización de la aplicación se ha usado _**Docker**_, tecnología de creación de contenedores que permite la creación y el uso de contenedores de Linux. 

## Elección del contenedor _base_ :house:

Existen diferentes versiones de Python montadas en distintas distribuciones Linux. Nuestro objetivo es elegir un contenedor base lo mas simple posible en el que no tengamos carga extra la cual no usaremos pero si todo lo necesario para montar y correr nuestra aplicación.

Unas de las primeras opciones consideradas como contenedor base ha sido `python:3.8.0-alpine`, sin embargo buscando información he encontrado que puede causar algunos problemas la contrucción de un contenedor sobre esta versión y ser mucho mas lenta y pesada que otras ([+info](https://pythonspeed.com/articles/alpine-docker-python/)):

> Most Python packages these days include binary wheels on PyPI, significantly speeding install time. But if you’re using Alpine Linux you need to compile all the C code in every Python package that you use.

Pero para realmente comprobar la veracidad de esto, la mejor opción es configurar nuestro _**Dockerfile**_ y ejecutarlo nosotros mismos. Vamos a considerar dos contenedores base para realizar las correspondientes pruebas: `python:3.8.0-alpine` y `python:3.8.0-slim`.

### python:3.8.0-alpine

Partiendo de un Dockerfile lo mas simple posible se han hecho pruebas de construcción del contenedor para ver que problemas nos podíamos encontrar:
- Uno de los "problemas" que nos hemos encontrado ha sido la necesidad de instalar algunas librerias para poder instalar _Poetry_ como **Rust** y **Cargo** entre otras.

Para medir el tiempo que tarda en construirse el contenedor se ha lanzado el comando:

```shell
time docker --no-cache build .
```

Obteniendo la salida:

```shell
Successfully built 529533260c3e

real	3m42,015s
user	0m0,090s
sys	0m0,067s
```

Para medir el tiempo que tarda en ejecutarse nuestros tests en el contenedor vamos a lanzar el siguiente comando (la imagen docker debe está subida a Dockerhub):

```shell
docker run -t -v `pwd`:/app/test nick-antobio17/iv
```

```shell
======================== 4 passed, 2 warnings in 0.02s =========================
Tests superados con éxito!
```

### python:3.8.0-slim

Partiendo de un Dockerfile lo mas simple posible se han hecho pruebas de construcción del contenedor para ver que problemas nos podíamos encontrar. Esta vez no hemos tenido que instalar ninguna dependencia y el contenedor se ha construido con cierta facilidad.

Para medir el tiempo que tarda en construirse el contenedor se ha vuelto a lanzar el comando:

```shell
time docker build --no-cache .
```

Obteniendo la salida:

```shell
Successfully built 5bfec2d103cc

real	0m11,869s
user	0m0,088s
sys	0m0,062s
```

Para medir el tiempo que tarda en ejecutarse nuestros tests en el contenedor vamos a lanzar el siguiente comando (la imagen docker debe está subida a Dockerhub):

```shell
docker run -t -v `pwd`:/app/test nick-antobio17/iv
```

```shell
============================== 4 passed in 0.02s ===============================
Tests superados con éxito!
```

---

Como podemos observar el tiempo de construcción del contenedor es bastante significativo pero el importante, el tiempo de ejecución de los tests, es el mismo.

Por el tiempo de construcción de la imagen, la "facilidad" al montar el _Dockerfile_ y por una ejecución de tests mas limpia sin warnings se va a proceder a usar la imagen base **slim** para _Python_.

Se ha tenido que establecer el [virtualenvs](https://python-poetry.org/docs/configuration/#virtualenvscreate) en _false_. En caso de no hacerlo al instalar las dependencias y ejecutar **invoke** obtendríamos este error ya que tal y como se comenta en la documentación oficial de **Poetry** creará un nuevo entorno virtual en el que instalará estas dependencias impidiendo ejecutarlas desde nuestro _workdir_.

```shell
docker: Error response from daemon: OCI runtime create failed: container_linux.go:380: starting container process caused: exec: "invoke": executable file not found in $PATH: unknown.
```

## DockerHub :whale:

El contendor ha sido publicado en [este enlace](https://hub.docker.com/repository/docker/antobio17/iv/) por medio de una _Github Action_. Para la configuración de esta se han seguido los pasos [_Github_](https://docs.github.com/es/actions/publishing-packages/publishing-docker-images). La imagen se subirá a Dockerhub cuando realicemos un push a cualquier rama de nuestro proyecto pero únicamente cuando se modifique el _Dockerfile_. No se ha incluido los Pull Requests ya que estos harán un push en **main** que ya está contemplado.
