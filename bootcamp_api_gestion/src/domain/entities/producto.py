# src/domain/entities/producto.py
from pydantic import BaseModel, validator
from typing import Optional

class Producto(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    stock: int

    @validator("precio")
    def precio_positivo(cls, v):
        if v <= 0: raise ValueError("Precio debe ser mayor a cero")
        return v
