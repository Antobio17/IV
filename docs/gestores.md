# Gestores :gear:

Para el uso de los siguientes gestores se deberán tener previamente instalados en el equipo.

## Gestor de dependencias: _Pip_ :arrow_down:

Según el [PEP 621](https://www.python.org/dev/peps/pep-0621/) debemos almacenar los metadatos del proyecto en un fichero llamado **pyproject.toml**. En el almacenaremos información referente al proyecto (nombre, descripción...), a los usuarios implicados (autores, mantenedores...), dependencias, entre otras cosas.
En este proyecto se añadirá la impormación básica y las dependencias requeridas ya que, por el momento no necesitamos configuración adicional.

En el propio _PEP_ nos indican trés [herramientas](https://www.python.org/dev/peps/pep-0621/#dependencies-optional-dependencies) para realizar esa instalación: Flit, Poetry y Setuptools. Ya que solo necesitamos usarlo para instalar las dependencias del proyecto (ya que usaremos para acompañarlo un gestor de tareas) se va a optar por el uso de **Flit** ya que no se necesitan ficheros extra y usa el propio fichero vanila de _pyproject.toml_ con la sintaxis que se especifica en la documentación oficial de _Python_. Lo único que necesitamos es definir el **Wheel** en _[build-system]_.

Una vez instalado _Flit_ podemos pasar a instalar las dependencias que definamos ejecutando:

```shell
flit install
```

## Gestor de tareas: _Invoke_ :bookmark_tabs:

[Instalación.](https://www.pyinvoke.org/installing.html)

Se ha elegido **Invoke** como gestor de tareas por varios motivos:
- Amplia documentación de la herramienta para poder apoyarse en el uso de esta.
- Proporciona una API limpia y de alto nivel para ejecutar comandos de shell y organizar funciones de tareas desde un archivo **tasks.py**.
- Desde el propio **task.py** con Invoke podría lanzar el comando para la instalación de dependencias unificando asi los gestores.
