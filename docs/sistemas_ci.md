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
