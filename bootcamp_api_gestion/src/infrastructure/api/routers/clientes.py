# src/infrastructure/api/routers/clientes.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from typing import List
from src.use_cases.clientes_use_cases import CrearClienteUseCase, ListarClientesUseCase
from src.infrastructure.api.dependencies import get_cliente_repository

router = APIRouter(prefix="/clientes", tags=["clientes"])

class ClienteRequest(BaseModel):
    nombre: str
    email: EmailStr
    edad: int
    tipo: str

class ClienteResponse(ClienteRequest):
    id: int
    activo: bool

@router.post("/", response_model=ClienteResponse)
def crear_cliente(req: ClienteRequest, repo = Depends(get_cliente_repository)):
    use_case = CrearClienteUseCase(repo)
    return use_case.execute(**req.model_dump())

@router.get("/", response_model=List[ClienteResponse])
def listar_clientes(repo = Depends(get_cliente_repository)):
    use_case = ListarClientesUseCase(repo)
    return use_case.execute()
