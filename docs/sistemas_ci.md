# Sistemas de Integración Continua :recycle:

En la actualidad multitud de _Sistemas de Integración Continua_. Vamos a proceder a elegir algunos de ellos para probarlos y ver cuales se adaptan más para los requisitos de este proyecto. Estos son:
- Poder correr el lenguaje utilizado en nuestro proyecto para lanzar los tests programados.
- Probar distintas versiones de _Python_.
- Poder integrar el CI con Github.
- Ser un sistema demandado por el panorama laboral actual.

## Travis :man_with_gua_pi_mao:

### Pasos de configuración :gear:

- Uno de los principales inconvenientes de **Travis** son los planes de pago. Esto puede suponer un problema para algunos usuarios que prefieran optar por otros _Sistemas de Integración Continua_ antes que pagar una cuota mensual. Pero realmente sin probarlo no sabemos si realmente puede merecer la pena, no para uso personal alomejor, pero si para propuesta y uso en una empresa ya que sería ella la encargada del mantenimiento. Para ello vamos a utilizar el **mes gratuirto** que nos ofrece para ver si realmente merece la pena.

- Usando la opción de **Trigger Build** desde _Travis_ crearemos el fichero **.travis.yaml** que será el encargado de proporcionar la configuración para la herramienta en la rama especificada. Este detalle parece una tontería pero es de bastante utilidad ya que en **Azure** no puedes elegir una rama ya existente, debes crear una nueva a partir de master.

```yaml
language: python
python:
  - "2.7"
  - "3.8.10"
  - "nightly"

# Comandos para instalar las dependencias
install:
  - pip install poetry
  - poetry install
  
# Comandos para lanzar los tests
script:
  - invoke test
```

- Una vez hecho esto se crearán 3 jobs (uno can cada versión de _Python_ especificada) en los que se lanzarán los tests del repositorio tal y como hemos indicado en el **YAML**.

![Jobs en Travis](/docs/images/jobs_travis.png "Jobs en Travis")

- Podremos entrar en cada **Job** para ver el log resultante de la ejecución.

![Job con error](/docs/images/failed_job_travis.png "Job con error")

![Job ejecutado con éxito](/docs/images/successfull_job_travis.png "Job ejecutado con éxito")

## Circle CI :hammer_and_wrench:

### Pasos de configuración :gear:

- Como cada uno de los anteriores _Sistemas de CI_ lo primero que debemos hacer es iniciar sesión mediante nuestra cuenta de _Github_ y autorizar el uso de **CircleCI**.

- Una vez enlazadas las cuentas y elegido el repositorio podremos pasar a configurar nuestro **YAML** de **CircleCI**. En este caso vamos a hacer uso de nuestra imagen construida y desplegada en **Dockerhub**.

![Configuración del YAML en CircleCI](/docs/images/yaml_configuration_circleci.png "Configuración del YAML en CircleCI")

- Una vez configurado el **YAML** podremos commitear los cambios y lanzarlo. Esto creará un _Pipeline_ donde se lanzarán los _jobs_ especificados en el archivo de configuración.

![Pipelines en CircleCI](/docs/images/pipelines_circleci.png "Pipelines en CircleCI")

- Además, podremos ver el _log_ step por step de la ejecución de nuestro _pipeline_.

![Steps del pipeline en CircleCI](/docs/images/steps_circleci.png "Steps del pipeline en CircleCI")

- Como estamos usando  nuestra propia imagen _Docker_ desplegada en **Dockerhub** no necesitamos configurar el manejo de la cache en nuestro **YAML** ya que todas las dependencias vienen instaladas en la imagen. Así le sacamos partido a nuestro _Dockerfile_ construido facilitándonos la configuración de **Circle CI** en nuestro repositorio.

## Github Actions :octocat:

Al igual que nuestra **Github Action** para construir y subir la imagen _Docker_ a _DockerHub_ podemos crear otra para pasar los tests del repositorio cuando deseemos.

### Pasos de configuración :gear:

- Lo primero crear el archivo encargado de la ejecución de los tests y añadirlo al directorio **.github/workflows/**.
- Una vez creado comenzaremos configurando cuando queremos que se lance la **Github Action**. En este caso, como queremos usarla para comprobar los tests únicamente se lanzará cuando se modifique algún archivo del directorio **my_hairdressing_app/** o del directorio **testing/**.
- Ahora pasamos a configurar el _job_ que ejecutará los tests. Al igual que en **Azure Pipelines** podemos configurar la acción para que compruebe diferentes versiones de _Python_. Vamos a seguir las buenas prácticas a la hora de construir el _job_ tal y como se indica en el repositorio oficial de [Github Actions](https://github.com/actions/starter-workflows/blob/main/ci/python-package.yml).

![Github Action para tests](/docs/images/tests_github_action.png "Github Action para tests")

## Azure Pipelines :desktop_computer:

Uno de los puntos muy positivos de **Azure Pipelines** es su completa y actualizada [documentación](https://docs.microsoft.com/es-es/azure/devops/pipelines), con una guía de integración con **Github** y otra de [Compilación de aplicaciones de Python](https://docs.microsoft.com/es-es/azure/devops/pipelines/ecosystems/python?view=azure-devops).

### Pasos de configuración :gear:

- Creamos nuestra cuenta de **Azure** accediendo mediante nuestra cuenta de **Github** y creamos el mismo repositorio que queremos enlazar, en este caso _IV_, donde construiremos nuestro **pipeline**.

![Construyendo el Pipeline](/docs/images/creating_pipeline_azure.png "Construyendo el Pipeline")

- En este **pipeline** podremos crear directamente un paquete _Python_ enlazado a nuestro repositorio de **Github** para ejecutar nuestra aplicación con distintas versiones de _Python_. Esto generará automáticamente un **YAML** de configuración que modificaremos para adaptarlo a nuestros gestores de dependencias y gestores de tareas. Siguiendo estos pasos el **YAML** podremos crearlo en la rama _master_ del repositorio o en una nueva rama creada a partir de esta. Como nosotros realmente lo que queremos es trabajar en la rama de nuestro Pull Request, crearemos directamente el **YAML** en nuestro proyecto y desde **Azure** al crear el _pipeline_ seleccionaremos la opcción de **_Existing Azure Pipelines YAML file_**.

![YAML existente en repositorio](/docs/images/existing_yaml_azure.png "YAML existente en repositorio")

![Configurando el YAML](/docs/images/yaml_configuration_azure.png "Configurando el YAML")

- La primera vez que ejecutemos nuestro **pipeline** dará error. Esto es debido a que necesitamos solicitar en un [formulario](https://aka.ms/azpipelines-parallelism-request) una "subvención gratuita de paralelismo" para poder lanzar los **jobs** con las diferentes versiones de _Python_. Una vez solicitado y concedido procederemos a ejecutarlo:

![Versiones de Python disponibles en Azure Pipelines](/docs/images/python_versions_azure.png "Versiones de Python disponibles en Azure Pipelines")

Como podemos ver no todas las versiones de _Python_ están disponibles en **Azure Pipelines** por lo que tendremos que elegir las mas cercanas a nuestro interés.

> ##[warning]Specifying an exact version is not recommended on Microsoft-Hosted agents. Patch versions of Python can be replaced by new ones on Hosted agents without notice, which will cause builds to fail unexpectedly. It is recommended to specify only major or major and minor version (Example: `3` or `3.6`)

Al ejecutar los _jobs_ con versiones específicas de _Python_ obtenemos el warning anterior. En este nos avisa de que no está recomendado utilizar una versión exacta ya que pueden cambiar en los _Hosted agents_. Para evitarnos errores inesperados pasaremos a especificar las versiones únicamente como _major y minor_.

![Pipeline ejecutado](/docs/images/executed_pipeline_azure.png "Pipeline ejecutado")

![Pipeline ejecutado](/docs/images/tests_azure.png "Pipeline ejecutado")

---

Para los requisitos especificados los cuatro **Sistemas de Integración Continua** testeados nos han dado buenos resultados con una facil configuración e integración. Sin embargo uno queda descartado por no tener una versión _freemium_ y solo tener un mes de prueba como es el caso de **Travis**. Aunque para el objetivo de la asignatura solo se pide la integración de dos sistemas he considerado dejar **CircleCI**, **Azure Pipelines** y **Github Actions**.

Por último, aunque estamos utilizando la versión _freemium_ **Azure Pipelines** tenemos 1800 minutos como límite de ejecución al mes (suficiente para este proyecto). Lo que haremos será configurar el **YAML** para que solo se lance cuando algún archivo del directorio **my_hairdressing_app/** o del directorio **testing/** han sido modificados.
