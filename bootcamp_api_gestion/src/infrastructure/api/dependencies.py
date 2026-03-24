# src/infrastructure/api/dependencies.py
from src.infrastructure.repositories.in_memory import InMemoryClienteRepository, InMemoryProductoRepository, InMemoryVentaRepository

_cliente_repo = InMemoryClienteRepository()
_producto_repo = InMemoryProductoRepository()
_venta_repo = InMemoryVentaRepository()

def get_cliente_repository(): return _cliente_repo
def get_producto_repository(): return _producto_repo
def get_venta_repository(): return _venta_repo
