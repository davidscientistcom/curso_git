# app/routers/productos.py
from fastapi import APIRouter
from app.schemas import ProductoCreate, ProductoOut
from app.database import productos_db

router = APIRouter(prefix="/productos", tags=["productos"])

@router.post("/", response_model=ProductoOut)
def crear_producto(producto: ProductoCreate):
    nuevo_id = len(productos_db) + 1
    nuevo_producto = producto.model_dump()
    nuevo_producto["id"] = nuevo_id
    
    productos_db.append(nuevo_producto)
    return nuevo_producto

@router.get("/", response_model=list[ProductoOut])
def listar_productos():
    return productos_db
