# Uso de tests :test_tube:

Para los archivos fuente del proyecto se van a implementar una serie de tests para compobar el correcto funcionamiendo de estos.
En _Python_ existen varios frameworks para la implementación de tests. Vamos a tener en cuenta dos de ellas, **Pytests** y **Unittest**.

La implementación de test es algo mas sencilla con _Pytests_ ya que se construyen con funciones directamente para testear el código deseado. Sin embargo en _Unittest_ se deben crear estructuras de clases. Esto puede ser una ventaja a la ora de organización de código para agrupar los diferentes test que podamos llegar a tener, pero con _Pytest_ podríamos organizarlos por archivos fuentes y ejecutar el que deseemos en cada momento.
También destacar que según he podido [leer](https://www.pythonpool.com/python-unittest-vs-pytest/), _pytest_ es más rápido y eficiente.
Por último añadir la posibilidad de ejecución con argumentos para lanzar los tests desde consola pudiendo indicar la información que queremos recibir de los tests lanzados, añadir el debugger de _Python_, etc.

Al igual que en el repositorio oficial de GitHub de [pytest](https://github.com/pytest-dev/pytest), hemos creado la carpeta _testing_ en la que almacenaremos los archivos fuentes para los testeos.

Enlaces con información adicional:
- https://realpython.com/pytest-python-testing
- https://docs.pytest.org/

## Assertions

Para el uso de _asserts_ en los tests realizados vamos a hacer uso de la biblioteca que nos trae python por defecto con la que podremos realizar todo lo deseado sin necesidad de instalar bibliotecas externas evitando asi posibles dependencias.
