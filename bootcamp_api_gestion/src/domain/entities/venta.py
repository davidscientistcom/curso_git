# src/domain/entities/venta.py
from pydantic import BaseModel
from typing import Optional

class Venta(BaseModel):
    id: Optional[int] = None
    cliente_id: int
    producto_id: int
    cantidad: int
    total: float
    descuento_aplicado: float
