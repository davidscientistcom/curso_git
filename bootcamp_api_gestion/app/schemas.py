# app/schemas.py
from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class ClienteCreate(BaseModel):
    nombre: str
    email: EmailStr
    edad: int
    tipo: str

    @validator("edad")
    def validar_edad(cls, v):
        if v < 18: raise ValueError("El cliente debe ser mayor de edad")
        return v
        
    @validator("tipo")
    def validar_tipo(cls, v):
        if v not in ["VIP", "NORMAL"]: raise ValueError("Tipo invalido")
        return v

class ClienteOut(ClienteCreate):
    id: int
    activo: bool

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    stock: int

    @validator("precio")
    def precio_positivo(cls, v):
        if v <= 0: raise ValueError("Precio debe ser mayor a cero")
        return v

class ProductoOut(ProductoCreate):
    id: int

class VentaCreate(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int
    
    @validator("cantidad")
    def cantidad_positiva(cls, v):
        if v <= 0: raise ValueError("Cantidad debe ser mayor a cero")
        return v

class VentaOut(BaseModel):
    id: int
    cliente_id: int
    producto_id: int
    cantidad: int
    total: float
    descuento_aplicado: float
