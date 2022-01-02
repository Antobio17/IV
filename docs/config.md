# Almacenamiento y gestión de la configuración :gear:
Los requisitos para almacenar nuestra configuración son:
- Poder almacenar la configuración de manera remota.
- Tener un fallback para cuando no podamos acceder remotamente a ella con un archivo de configuración en nuestro repositorio local.
- Tener un segundo fallback para cuando no podemos acceder a ninguno de los dos anteriores con configuración por defecto en el propio código.

## Configuración local: .env
Para almacenar la configuración se ha optado por usar un fichero **Dotenv** . Se usarán pares claves valor para la definicion de las variables de entorno. Al usar este tipo de variables podremos añadirlas a los _Sistemas de CI_ para su uso en la ejecución de tests como en **CircleCI** por ejemplo:

![Valores de entorno](/docs/images/vars_env.png "Valores de entorno")

## Configuración remota

Para el almacenamiento de la configuración remota se va a usar **ETCD3** por su simplicidad. Usando la _API_ para _Python_ únicamente deberémos hacer solicitudes **GET** con el cliente al que accederemos a través del host y el puerto una vez configurado.

### Github Action
El fichero **.env**, al ser el encargado de almacenar nuestra configuración será esencial que no se añada nunca al repositorio remoto. Para ello se ha creado una **Github Action** que en primer lugar comprobará, mediante un script, si el _.gitignore_ contiene el valor _.env_. Además comprobará si el archivo no se ha commiteado y subido al repositorio.

---

Esto se define en las issues [#40](https://github.com/Antobio17/IV/issues/40) y [#45](https://github.com/Antobio17/IV/issues/45). 