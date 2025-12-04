import subprocess

def ejecutar_cobol(nombre_programa):
    try:
        resultado = subprocess.run(
            [f"./cobol/{nombre_programa}"],
            capture_output=True,
            text=True
        )
        return resultado.stdout
    except Exception as e:
        return str(e)
