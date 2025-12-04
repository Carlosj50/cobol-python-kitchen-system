from fastapi import APIRouter

router = APIRouter(prefix="/inventario")

@router.get("/listar")
def listar():
    return {"productos": ["Carlos", "Mariam"]}
