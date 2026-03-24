# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app
from app.database import reset_database
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def run_around_tests():
    # Setup
    reset_database()
    yield # Test
    # Teardown
    reset_database()

def test_crear_cliente_exito():
    response = client.post("/clientes/", json={
        "nombre": "Juan",
        "email": "juan@test.com",
        "edad": 25,
        "tipo": "NORMAL"
    })
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["nombre"] == "Juan"

def test_crear_cliente_validacion_pydantic():
    # FastAPI valida automáticamente
    response = client.post("/clientes/", json={
        "nombre": "Maria",
        "email": "correo-invalido",
        "edad": 15,
        "tipo": "OTRO"
    })
    assert response.status_code == 422

def test_realizar_venta():
    client.post("/clientes/", json={"nombre": "Pedro", "email": "p@t.com", "edad": 30, "tipo": "VIP"})
    client.post("/productos/", json={"nombre": "PC", "precio": 1000.0, "stock": 10})
    
    response = client.post("/ventas/", json={"cliente_id": 1, "producto_id": 1, "cantidad": 1})
    
    assert response.status_code == 200
    assert response.json()["total"] == 850.0
    
    response_prod = client.get("/productos/")
    assert response_prod.json()[0]["stock"] == 9
