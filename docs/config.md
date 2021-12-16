# Almacenamiento y gestión de la configuración :gear:
Para almacenar la configuración se ha optado por usar dos ficheros: **YAML** y **dotenv**. Con los ficheros **YAML** tenemos la opción de construir estructuras de datos y definir tipos lo que nos dará una amplia posibilidad para almacenar la configuración de nuestra aplicación, como por ejemplo la configuración de logging.
El fichero **dotenv** se usará para la configuración privada como claves, IPs, etc. Al ser valores de tipo _clave=valor_ una mayor simplicidad pero da menos posibilidad a construir objetos.

## Github Action para comprobación de dotenv
El fichero **dotenv**, al ser el encargado de almacenar nuestra configuración privada será esencial que no se añada nunca al repositorio remoto. Para ello se ha creado una **Github Action** que en primer lugar comprobará, mediante un script, si el _.gitignore_ contiene el valor _.env_. Además comprobará si el **dotenv** se ha commiteado y subido al repositorio.

---

Esto se define en las issues [#40](https://github.com/Antobio17/IV/issues/40) y [#45](https://github.com/Antobio17/IV/issues/45) 