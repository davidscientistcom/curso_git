# src/domain/entities/cliente.py
from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class Cliente(BaseModel):
    id: Optional[int] = None
    nombre: str
    email: EmailStr
    edad: int
    tipo: str
    activo: bool = True

    @validator("edad")
    def validar_edad(cls, v):
        if v < 18: raise ValueError("Debe ser mayor de edad")
        return v
        
    @validator("tipo")
    def validar_tipo(cls, v):
        if v not in ["VIP", "NORMAL"]: raise ValueError("Tipo invalido")
        return v
