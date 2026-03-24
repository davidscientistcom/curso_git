# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app
from src.infrastructure.repositories.in_memory import InMemoryClienteRepository, InMemoryProductoRepository, InMemoryVentaRepository
from src.infrastructure.api.dependencies import get_cliente_repository, get_producto_repository, get_venta_repository
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def override_dependencies():
    test_cliente_repo = InMemoryClienteRepository()
    test_producto_repo = InMemoryProductoRepository()
    test_venta_repo = InMemoryVentaRepository()
    
    app.dependency_overrides[get_cliente_repository] = lambda: test_cliente_repo
    app.dependency_overrides[get_producto_repository] = lambda: test_producto_repo
    app.dependency_overrides[get_venta_repository] = lambda: test_venta_repo
    
    yield
    
    app.dependency_overrides.clear()

def test_crear_cliente_arquitectura_limpia():
    response = client.post("/clientes/", json={
        "nombre": "Arquitecto",
        "email": "arca@test.com",
        "edad": 40,
        "tipo": "VIP"
    })
    assert response.status_code == 200
    assert response.json()["nombre"] == "Arquitecto"

def test_realizar_venta_arquitectura_limpia():
    client.post("/clientes/", json={"nombre": "Tio Bob", "email": "bob@clean.com", "edad": 60, "tipo": "VIP"})
    client.post("/productos/", json={"nombre": "Libro Clean Code", "precio": 50.0, "stock": 100})
    
    response = client.post("/ventas/", json={"cliente_id": 1, "producto_id": 1, "cantidad": 2})
    
    assert response.status_code == 200
    assert response.json()["total"] == 85.0
