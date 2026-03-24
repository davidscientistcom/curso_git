# app/routers/clientes.py
from fastapi import APIRouter
from app.schemas import ClienteCreate, ClienteOut
from app.database import clientes_db

router = APIRouter(prefix="/clientes", tags=["clientes"])

@router.post("/", response_model=ClienteOut)
def crear_cliente(cliente: ClienteCreate):
    nuevo_id = len(clientes_db) + 1
    nuevo_cliente = cliente.model_dump()
    nuevo_cliente["id"] = nuevo_id
    nuevo_cliente["activo"] = True
    
    clientes_db.append(nuevo_cliente)
    return nuevo_cliente

@router.get("/", response_model=list[ClienteOut])
def listar_clientes():
    return clientes_db
