# Uso de tests :test_tube:

Para los archivos fuente del proyecto se van a implementar una serie de tests para compobar el correcto funcionamiendo de estos.
En _Python_ existen varios framework y librerías para la construcción de tests, para este proyecto se van a tener en cuenta dos de ellas, **Pytests** y **Unittest**.

Las dos herramientas son bastante similares pero para mi hay algo bastante significativo que las diferencia y es la **respuesta de la ejcución** al lanzar estos tests.
En el caso de que ningún test de error, ambos nos dirán que se han ejecutado sin problemas mostrando el tiempo que han tardado, sin embargo, la diferencia aparece cuando un test falla. En _unittest_ únicamente nos dirá que ha habido un error, pero en _pytests_ además mostrará en que test se ha producido el error. Esto puede ser bastante util en el caso de tener una gran batería de test ya que nos permitirá identificar rapidamente donde tenemos el problema.
También destacar que según he podido (leer)[https://www.pythonpool.com/python-unittest-vs-pytest/], _pytest_ es más rápido y eficiente.
Por último añadir la posibilidad de ejecución con argumentos para lanzar los tests desde consola pudiendo indicar la información que queremos recibir de los tests lanzados, añadir el debugger de _Python_, etc.

Al igual que en el repositorio oficial de GitHub de (pytest)[https://github.com/pytest-dev/pytest], hemos creado la carpeta _testing_ en la que almacenaremos los archivos fuentes para los testeos.

Enlaces con información adicional:
- (https://realpython.com/pytest-python-testing/)[https://realpython.com/pytest-python-testing/].
- (https://docs.pytest.org/)[https://docs.pytest.org/].

## Assertions

Para el uso de _asserts_ en los tests realizados vamos a hacer uso de la biblioteca que nos trae python por defecto con la que podremos realizar todo lo deseado sin necesidad de instalar bibliotecas externas evitando asi posibles dependencias.
