from invoke import task, run

@task
def installdeps(c):
    """
    Instalará las dependencias especificadas en el archivo requirements.txt mediante Pip.
    """

    print("Instalando las dependencias...")
    
    try:
        run("pip3 install -r requiremets.txt")
        print("La instalación ha terminado con éxito!")
    except Exception:
        print("Ha ocurrido un error en la instalación.")


