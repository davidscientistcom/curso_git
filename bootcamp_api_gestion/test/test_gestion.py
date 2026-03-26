import os
import sys
import pytest
import re

# Add repository package path so pytest can import gestion_monolito from subfolder
TEST_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(TEST_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import gestion_monolito

# FASE 0: Ejemplo de Tests Acoplados y Frágiles


def _validar_correo(correo):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return bool(re.fullmatch(pattern, correo))


@pytest.fixture(autouse=True)
def limpiar_base_datos():
    gestion_monolito.borrar_datos_para_testing()
    yield


def test_crear_cliente_exito():
    resultado = gestion_monolito.crear_cliente("Juan Perez", "juan@test.com", 25, "NORMAL")
    assert resultado
    assert len(gestion_monolito.clientes_db) == 1
    assert gestion_monolito.clientes_db[0]["id"] == 1


def test_crear_cliente_edad_invalida():
    resultado = gestion_monolito.crear_cliente("Maria", "maria@test.com", 15, "NORMAL")
    assert resultado is False


def test_crear_cliente_correo_invalido():
    correo = "mariatest.com"
    assert not _validar_correo(correo)


def test_crear_cliente_correo_valido():
    correo = "maria@test.com"
    assert _validar_correo(correo)


def test_crear_producto_exito():
    resultado = gestion_monolito.crear_producto("Laptop", 1000.0, 50)
    assert "error" not in resultado
    assert resultado["nombre"] == "Laptop"
    assert len(gestion_monolito.productos_db) == 1


def test_realizar_venta_vip_exito():
    gestion_monolito.crear_cliente("Ana VIP", "ana@test.com", 30, "VIP")
    gestion_monolito.crear_producto("Laptop", 1000.0, 50)
    resultado = gestion_monolito.realizar_venta(1, 1, 1)

    assert isinstance(resultado, dict)
    assert resultado["total"] == 850.0
    assert resultado["descuento_aplicado"] == 0.15
    assert gestion_monolito.productos_db[0]["stock"] == 49


def test_realizar_venta_sin_stock():
    gestion_monolito.crear_cliente("Cliente", "c@test.com", 30, "NORMAL")
    gestion_monolito.crear_producto("Mouse", 10.0, 5)
    resultado = gestion_monolito.realizar_venta(1, 1, 100)

    assert resultado == "No hay suficiente stock"


def test_cleanup():
    # La fixture autouse ya limpia antes de cada prueba
    assert len(gestion_monolito.clientes_db) == 0
    assert len(gestion_monolito.productos_db) == 0
    assert len(gestion_monolito.ventas_db) == 0
