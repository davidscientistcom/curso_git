# src/infrastructure/api/routers/productos.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from src.use_cases.productos_use_cases import CrearProductoUseCase, ListarProductosUseCase
from src.infrastructure.api.dependencies import get_producto_repository

router = APIRouter(prefix="/productos", tags=["productos"])

class ProductoRequest(BaseModel):
    nombre: str
    precio: float
    stock: int

class ProductoResponse(ProductoRequest):
    id: int

@router.post("/", response_model=ProductoResponse)
def crear_producto(req: ProductoRequest, repo = Depends(get_producto_repository)):
    use_case = CrearProductoUseCase(repo)
    return use_case.execute(**req.model_dump())

@router.get("/", response_model=List[ProductoResponse])
def listar_productos(repo = Depends(get_producto_repository)):
    use_case = ListarProductosUseCase(repo)
    return use_case.execute()
