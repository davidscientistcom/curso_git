# src/use_cases/clientes_use_cases.py
from src.domain.repositories.interfaces import ClienteRepository
from src.domain.entities.cliente import Cliente

class CrearClienteUseCase:
    def __init__(self, cliente_repo: ClienteRepository):
        self.cliente_repo = cliente_repo
        
    def execute(self, nombre: str, email: str, edad: int, tipo: str) -> Cliente:
        cliente = Cliente(nombre=nombre, email=email, edad=edad, tipo=tipo)
        return self.cliente_repo.save(cliente)

class ListarClientesUseCase:
    def __init__(self, cliente_repo: ClienteRepository):
        self.cliente_repo = cliente_repo
        
    def execute(self):
        return self.cliente_repo.get_all()
