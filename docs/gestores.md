# Gestores :gear:

Para el uso de los siguientes gestores se deberán tener previamente instalados en el equipo.

## Gestor de dependencias :arrow_down:

Según el [PEP 621](https://www.python.org/dev/peps/pep-0621/) debemos almacenar los metadatos del proyecto en un fichero llamado **pyproject.toml**. En el almacenaremos información referente al proyecto (nombre, descripción...), a los usuarios implicados (autores, mantenedores...), dependencias, entre otras cosas.
En este proyecto se añadirá la impormación básica y las dependencias requeridas ya que, por el momento no necesitamos configuración adicional.

En el propio _PEP_ nos indican trés [herramientas](https://www.python.org/dev/peps/pep-0621/#dependencies-optional-dependencies) para realizar esa instalación: Flit, Poetry y Setuptools. Ya que solo necesitamos usarlo para instalar las dependencias del proyecto (ya que usaremos para acompañarlo un gestor de tareas) se podría optar por el uso de **Flit** ya que puede usar el propio fichero vanila de _pyproject.toml_ con la sintaxis que se especifica en la documentación oficial de _Python_. Lo único que necesitamos es definir el **Wheel** en _[build-system]_. Sin embargo a la hora de crear el Dockerfile no reconoce el nombre del _package_ a no ser que también lo movamos al _workdir_. Esto lo solucionaríamos con las etiquetas de flit en el archivo **pyproject.toml** pero no se recomienda ya que está en desuso.

```shell
raise ValueError("No file/folder found for module {}".format(name))
ValueError: No file/folder found for module my_hairdressing_app
```

Para solventar este problema por lo tanto vamos a hacer uso de **Poetry**.

## Gestor de tareas: _Invoke_ :bookmark_tabs:

[Instalación.](https://www.pyinvoke.org/installing.html)

Se ha elegido **Invoke** como gestor de tareas por varios motivos:
- Amplia documentación de la herramienta para poder apoyarse en el uso de esta.
- Proporciona una API limpia y de alto nivel para ejecutar comandos de shell y organizar funciones de tareas desde un archivo **tasks.py**.
- Desde el propio **task.py** con Invoke podría lanzar el comando para la instalación de dependencias unificando asi los gestores.
