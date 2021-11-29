from invoke import task, run

@task
def installdeps(c):
    """
    Instalará las dependencias especificadas en el archivo requirements.txt mediante Pip.
    """

    print("Instalando las dependencias...")
    
    try:
        run("poetry install")
        print("La instalación ha terminado con éxito!")
    except Exception:
        print("Ha ocurrido un error en la instalación.")


@task
def check(c):
    """
    Comprobará la sintaxis de los archivos del proyecto mediante pyflakes.
    """

    print("Comprobando sintaxis...")
    run("pyflakes my_hairdressing_app")
    print("Todo correcto. La comprobación ha terminado con éxito!")

@task
def test(c):
    """
    Lanzará todos los tests definidos en el directorio tests
    """

    print("Lanzando tests...")
    run("pytest testing/")
    print("Tests superados con éxito!")