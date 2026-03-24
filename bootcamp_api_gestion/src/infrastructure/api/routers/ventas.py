# src/infrastructure/api/routers/ventas.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from src.use_cases.ventas_use_cases import RealizarVentaUseCase
from src.infrastructure.api.dependencies import get_cliente_repository, get_producto_repository, get_venta_repository

router = APIRouter(prefix="/ventas", tags=["ventas"])

class VentaRequest(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int

@router.post("/")
def crear_venta(
    req: VentaRequest,
    cliente_repo = Depends(get_cliente_repository),
    producto_repo = Depends(get_producto_repository),
    venta_repo = Depends(get_venta_repository)
):
    use_case = RealizarVentaUseCase(cliente_repo, producto_repo, venta_repo)
    try:
        resultado = use_case.execute(req.cliente_id, req.producto_id, req.cantidad)
        return resultado
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
