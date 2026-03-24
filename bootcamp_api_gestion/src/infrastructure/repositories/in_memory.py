# src/infrastructure/repositories/in_memory.py
from typing import List, Optional
from src.domain.entities.cliente import Cliente
from src.domain.entities.producto import Producto
from src.domain.entities.venta import Venta
from src.domain.repositories.interfaces import ClienteRepository, ProductoRepository, VentaRepository

class InMemoryClienteRepository(ClienteRepository):
    def __init__(self):
        self._clientes = []
        self._next_id = 1
    def save(self, cliente: Cliente) -> Cliente:
        cliente.id = self._next_id
        self._next_id += 1
        self._clientes.append(cliente)
        return cliente
    def get_by_id(self, cliente_id: int) -> Optional[Cliente]:
        return next((c for c in self._clientes if c.id == cliente_id), None)
    def get_all(self):
        return self._clientes

class InMemoryProductoRepository(ProductoRepository):
    def __init__(self):
        self._productos = []
        self._next_id = 1
    def save(self, producto: Producto) -> Producto:
        producto.id = self._next_id
        self._next_id += 1
        self._productos.append(producto)
        return producto
    def update(self, producto: Producto) -> Producto:
        for idx, p in enumerate(self._productos):
            if p.id == producto.id:
                self._productos[idx] = producto
                break
        return producto
    def get_by_id(self, producto_id: int) -> Optional[Producto]:
        return next((p for p in self._productos if p.id == producto_id), None)
    def get_all(self):
        return self._productos

class InMemoryVentaRepository(VentaRepository):
    def __init__(self):
        self._ventas = []
        self._next_id = 1
    def save(self, venta: Venta) -> Venta:
        venta.id = self._next_id
        self._next_id += 1
        self._ventas.append(venta)
        return venta
