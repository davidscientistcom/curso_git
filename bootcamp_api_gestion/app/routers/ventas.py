# app/routers/ventas.py
from fastapi import APIRouter, HTTPException
from app.schemas import VentaCreate, VentaOut
from app.database import clientes_db, productos_db, ventas_db

router = APIRouter(prefix="/ventas", tags=["ventas"])

@router.post("/", response_model=VentaOut)
def realizar_venta(venta: VentaCreate):
    cliente = next((c for c in clientes_db if c["id"] == venta.cliente_id), None)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
        
    if not cliente.get("activo", False):
        raise HTTPException(status_code=400, detail="El cliente no esta activo")
        
    producto = next((p for p in productos_db if p["id"] == venta.producto_id), None)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
        
    if producto["stock"] < venta.cantidad:
        raise HTTPException(status_code=400, detail="No hay suficiente stock")
        
    descuento = 0.0
    if cliente["tipo"] == "VIP":
        descuento = 0.15
    elif cliente["tipo"] == "NORMAL" and venta.cantidad > 10:
        descuento = 0.05
        
    total = (producto["precio"] * venta.cantidad) * (1 - descuento)
    producto["stock"] -= venta.cantidad
    
    nueva_venta = venta.model_dump()
    nueva_venta["id"] = len(ventas_db) + 1
    nueva_venta["total"] = total
    nueva_venta["descuento_aplicado"] = descuento
    
    ventas_db.append(nueva_venta)
    return nueva_venta
