# app/main.py
from fastapi import FastAPI
from src.infrastructure.api.routers import clientes, productos, ventas

app = FastAPI(title="Gestión de Ventas API - Arquitectura Limpia")

app.include_router(clientes.router)
app.include_router(productos.router)
app.include_router(ventas.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a la API con Clean Architecture y SOLID - Fase 2"}
