# src/domain/repositories/interfaces.py
from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.cliente import Cliente
from src.domain.entities.producto import Producto
from src.domain.entities.venta import Venta

class ClienteRepository(ABC):
    @abstractmethod
    def save(self, cliente: Cliente) -> Cliente: pass
    @abstractmethod
    def get_by_id(self, cliente_id: int) -> Optional[Cliente]: pass
    @abstractmethod
    def get_all(self): pass

class ProductoRepository(ABC):
    @abstractmethod
    def save(self, producto: Producto) -> Producto: pass
    @abstractmethod
    def update(self, producto: Producto) -> Producto: pass
    @abstractmethod
    def get_by_id(self, producto_id: int) -> Optional[Producto]: pass
    @abstractmethod
    def get_all(self): pass

class VentaRepository(ABC):
    @abstractmethod
    def save(self, venta: Venta) -> Venta: pass
