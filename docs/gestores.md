# Gestores :gear:

Para el uso de los siguientes gestores se deberán tener previamente instalados en el equipo.

## Gestor de dependencias: _Pip_ :arrow_down:

[Instalación.](https://pip.pypa.io/en/stable/installation/)

Se ha elegido **Pip** como gestor de dependencias por la simplicidad de uso. 

Bastaría con crear un archivo **_requirements.txt_** en el que declararemos nuestras dependencias de la forma: _dependencia==version_.

Para instalar las dependencias se podrá ejecutar:

```shell
pip3 install -r requirements.txt
```

## Gestor de tareas: _Invoke_ :bookmark_tabs:

[Instalación.](https://www.pyinvoke.org/installing.html)

Se ha elegido **Invoke** como gestor de tareas por varios motivos:
- Amplia documentación de la herramienta para poder apoyarse en el uso de esta.
- Proporciona una API limpia y de alto nivel para ejecutar comandos de shell y organizar funciones de tareas desde un archivo **tasks.py**.
- Desde el propio **task.py** con Invoke podría lanzar el comando para la instalación de dependencias unificando asi los gestores.
