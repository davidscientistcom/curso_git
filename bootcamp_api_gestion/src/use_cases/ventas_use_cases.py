# src/use_cases/ventas_use_cases.py
from src.domain.repositories.interfaces import ClienteRepository, ProductoRepository, VentaRepository
from src.domain.entities.venta import Venta

class RealizarVentaUseCase:
    def __init__(self, cliente_repo: ClienteRepository, producto_repo: ProductoRepository, venta_repo: VentaRepository):
        self.cliente_repo = cliente_repo
        self.producto_repo = producto_repo
        self.venta_repo = venta_repo

    def execute(self, cliente_id: int, producto_id: int, cantidad: int) -> Venta:
        if cantidad <= 0: raise ValueError("Cantidad debe ser mayor a cero")
        
        cliente = self.cliente_repo.get_by_id(cliente_id)
        if not cliente: raise ValueError("Cliente no encontrado")
        if not cliente.activo: raise ValueError("El cliente no esta activo")
        
        producto = self.producto_repo.get_by_id(producto_id)
        if not producto: raise ValueError("Producto no encontrado")
        if producto.stock < cantidad: raise ValueError("No hay suficiente stock")
        
        descuento = 0.0
        if cliente.tipo == "VIP":
            descuento = 0.15
        elif cliente.tipo == "NORMAL" and cantidad > 10:
            descuento = 0.05
            
        total = (producto.precio * cantidad) * (1 - descuento)
        producto.stock -= cantidad
        self.producto_repo.update(producto)
        
        venta = Venta(
            cliente_id=cliente_id,
            producto_id=producto_id,
            cantidad=cantidad,
            total=total,
            descuento_aplicado=descuento
        )
        return self.venta_repo.save(venta)
