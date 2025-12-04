import subprocess
from fastapi import FastAPI, APIRouter
from backend.python_services.rutas.inventario import router as inventario_router

app = FastAPI()

# Registrar rutas
app.include_router(inventario_router)

@app.get("/cobol/ejecutar")
def ejecutar_cobol():
    try:
        resultado = subprocess.run(
            ["./cobol/ejemplo"],     # ejecuta el COBOL compilado
            capture_output=True,
            text=True
        )
        return {"salida": resultado.stdout}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def inicio():
    return {"mensaje": "Servidor de cocina funcionando"}
