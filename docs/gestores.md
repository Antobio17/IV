# Gestores :gear:

## Gestor de dependencias: _Pip_ :arrow_down:

Se ha elegido **Pip** como gestor de dependencias por la simplicidad de uso. 

Bastaría con crear un archivo **_requirements.txt_** en el que declararemos nuestras dependencias de la forma: _dependencia==version_.

Para instalar las dependencias ejecutaremos:

```python
pip3 install -r requirements.txt
```

## Gestor de tareas: _Invoke_ :bookmark_tabs:

Se ha elegido **Invoke** como gestor de tareas por varios motivos:
- Amplia documentación de la herramienta para poder apoyarse en el uso de esta.
- Proporciona una API limpia y de alto nivel para ejecutar comandos de shell y organizar funciones de tareas desde un archivo **tasks.py**.
- Desde el propio **task.py** con Invoke podría lanzar el comando para la instalación de dependencias unificando asi los gestores.
