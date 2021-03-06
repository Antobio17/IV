# MyHairdressingAPP :money_mouth_face:

![Tests Status](https://github.com/Antobio17/IV/actions/workflows/run_tests.yml/badge.svg)
![Docker Image Status](https://github.com/Antobio17/IV/actions/workflows/dockerhub.yml/badge.svg)
![Dotenv](https://github.com/Antobio17/IV/actions/workflows/dotenv_checker.yml/badge.svg)
[![CircleCI Tests Status](https://circleci.com/gh/Antobio17/IV/tree/master.svg?style=svg)](https://circleci.com/gh/Antobio17/IV/?branch=master)
[![Build Status](https://dev.azure.com/Antobio17/IV/_apis/build/status/Antobio17.IV?branchName=master)](https://dev.azure.com/Antobio17/IV/_build/latest?definitionId=2&branchName=master)

## Descripción del problema :spiral_notepad:

Dado un caso real, en donde a una peluquería normalmente acudía la gente sin previo aviso para esperar a poder ser atendida, tuvo que adaptarse a las nuevas normativas y habilitar un teléfono para la reserva de citas debido al COVID-19.

El problema aparece a la hora de reserva de los distintos tipos de cita, cada uno con diferente duración. En este proceso una mala disposición de las diferentes citas puede suponer un número menor de citas diarias, disminuyendo así las ganancias del negocio.

Además otro de los problemas que aparecen es la cantidad de articulos en el pedido mensual de productos para el negocio. Estos productos son utilizados para las citas y dependiendo del tipo de cita se agotarán antes o después.

### Propuesta

Se propone por tanto un sistema de gestión de cita previa "inteligente" que organizará la disposición de las reservas realizadas atendiendo a los siguientes [criterios](docs/criterios_citas.md).

La organización de la reserva de citas será automática (mediante un algoritmo), aunque si fuera necesario los trabajadores podrán añadir cintas "estrictas" a las cuales no afectarán los criteros de organización comentados anteriormente.

También se propone un sistema de gestión de pedidos mensuales para ajustar el gasto a las necesidades de la peluquería.

## Issues :adhesive_bandage:

Puedes acceder a información detallada de las Issues del repositorio desde [aquí](docs/issues.md).

## Tipos de usuario :busts_in_silhouette:

Puedes acceder a la información de los tipos de usuario desde [aquí](docs/tipos_usuario.md).

## Gestores :gear:

Puedes acceder a los gestores utilizados para esta aplicación desde [aquí](docs/gestores.md).

### Instalación de dependencias

La orden que se deberá ejecutar es la siguiente:

```shell
invoke installdeps
```

### Comprobación de sintaxis del proyecto

Para comprobar la sintaxis de los distintos archivos del proyecto se han valorado y probado varias opciones como _Pyflakes_ o _Pylint_. Finalmente se usará el checkeador _Pyflakes_ ya que realiza las comprobaciones en un menor tiempo y además de indicar el fichero junto con la línea donde está el error, muestra explicitamente la línea de código marcando la posición del mismo. 

La orden que se deberá ejecutar es la siguiente:

```shell
invoke check
```

### Uso de tests

Puedes acceder a la información relativa a los **tests** desde [aquí](docs/tests.md).

La orden que se deberá ejecutar es la siguiente:

```shell
invoke test
```

## Docker :computer:

Puedes acceder a la información de **contenerización** para esta aplicación desde [aquí](docs/docker.md).

## Sistemas de Integración Continua :recycle:

Puedes acceder a la información de los **Sistemas de Integración Continua** para esta aplicación desde [aquí](docs/sistemas_ci.md).

## Almacenamiento y gestión de la configuración :gear:

Puedes acceder a la información del **almacenamiento y gestión de la configuración** desde [aquí](docs/config.md).

## Configuración de un Sistema de logging :writing_hand:

Puedes acceder a la información del **Sistema de logging** para esta aplicación desde [aquí](docs/logging.md).
