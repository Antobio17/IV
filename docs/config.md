# Almacenamiento y gestión de la configuración :gear:
Los requisitos para almacenar nuestra configuración son:
- Poder almacenar la configuración de manera remota.
- Tener un fallback para cuando no podamos acceder remotamente a ella con un archivo de configuración en nuestro repositorio local.
- Tener un segundo fallback para cuando no podemos acceder a ninguno de los dos anteriores con configuración por defecto en el propio código.
- Poder construir estructutas de datos mas complejas que las **clave/valor**.

## Configuración local: config.yml
Para almacenar la configuración se ha optado por usar un fichero **YAML** . Con los ficheros **YAML** tenemos la opción de construir estructuras de datos y definir tipos lo que nos dará una amplia posibilidad para almacenar la configuración de nuestra aplicación, como por ejemplo la configuración de logging.

## Configuración remota

Para el almacenamiento de la configuración remota se va a usar **ETCD3** por su simplicidad. Usando la _API_ para _Python_ únicamente deberémos hacer solicitudes **GET** con el cliente al que accederemos a través del host y el puerto una vez configurado.

### Github Action
El fichero **config.yml**, al ser el encargado de almacenar nuestra configuración será esencial que no se añada nunca al repositorio remoto. Para ello se ha creado una **Github Action** que en primer lugar comprobará, mediante un script, si el _.gitignore_ contiene el valor _config.yml_. Además comprobará si el archivo no se ha commiteado y subido al repositorio.

---

Esto se define en las issues [#40](https://github.com/Antobio17/IV/issues/40) y [#45](https://github.com/Antobio17/IV/issues/45). 