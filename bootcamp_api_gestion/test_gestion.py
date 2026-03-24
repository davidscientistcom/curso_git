import pytest
import gestion_monolito
import re
# FASE 0: Ejemplo de Tests Acoplados y Frágiles



def _validar_correo(correo):
        resultado = False
        pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
        if  re.fullmatch(pattern, correo):
            resultado = True
        else:
            resultado = False
        return resultado



def test_crear_cliente_exito():
    resultado = gestion_monolito.crear_cliente("Juan Perez", "juan@test.com", 25, "NORMAL")
    assert resultado == True
    assert len(gestion_monolito.clientes_db) == 1
    assert gestion_monolito.clientes_db[0]["id"] == 1

def test_crear_cliente_edad_invalida():
    resultado = gestion_monolito.crear_cliente("Maria", "maria@test.com", 15, "NORMAL")
    assert resultado == False


def test_crear_cliente_correo_invalido():
    correo = "mariatest.com"
    if not _validar_correo(correo):
        resultado = True
    else:        
        resultado = False

    assert resultado == True

def test_crear_cliente_correo_valido():
    correo = "maria@test.com"
    if  _validar_correo(correo):
        resultado = True
    else:        
        resultado = False
        
    assert resultado == True


def test_crear_producto_exito():
    resultado = gestion_monolito.crear_producto("Laptop", 1000.0, 50)
    assert "error" not in resultado
    assert resultado["nombre"] == "Laptop"
    assert len(gestion_monolito.productos_db) == 1

def test_realizar_venta_vip_exito():
    # TEST MUY FRÁGIL: Depende estrictamente de los anteriores.
    gestion_monolito.crear_cliente("Ana VIP", "maria@test.com", 30, "VIP")
    resultado = gestion_monolito.realizar_venta(2, 1, 1)
    
    assert type(resultado) is dict
    assert resultado["total"] == 850.0
    assert resultado["descuento_aplicado"] == 0.15
    assert gestion_monolito.productos_db[0]["stock"] == 49

def test_realizar_venta_sin_stock():
    resultado = gestion_monolito.realizar_venta(1, 1, 100)
    assert resultado == "No hay suficiente stock"

def test_cleanup():
    gestion_monolito.borrar_datos_para_testing()
    assert len(gestion_monolito.clientes_db) == 0
