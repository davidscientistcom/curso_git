# src/use_cases/productos_use_cases.py
from src.domain.repositories.interfaces import ProductoRepository
from src.domain.entities.producto import Producto

class CrearProductoUseCase:
    def __init__(self, producto_repo: ProductoRepository):
        self.producto_repo = producto_repo
        
    def execute(self, nombre: str, precio: float, stock: int) -> Producto:
        prod = Producto(nombre=nombre, precio=precio, stock=stock)
        return self.producto_repo.save(prod)

class ListarProductosUseCase:
    def __init__(self, producto_repo: ProductoRepository):
        self.producto_repo = producto_repo
        
    def execute(self):
        return self.producto_repo.get_all()
