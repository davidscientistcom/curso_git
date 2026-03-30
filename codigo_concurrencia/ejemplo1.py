import threading
import time

# 1. LA IMPLEMENTACIÓN INSEGURA
class UnsafeCounter:
    def __init__(self):
        self.value = 0
        
    def increment(self):
        # Separar lectura y escritura para forzar la race condition
        current = self.value
        time.sleep(0.00001)  # Forzamos cambio de contexto aquí
        self.value = current + 1

# 2. EL TEST (TDD)
def test_unsafe_counter_race_condition():
    counter = UnsafeCounter()
    
    def worker():
        for _ in range(50):
            counter.increment()
            
    threads = [threading.Thread(target=worker) for _ in range(10)]
    
    for t in threads: t.start()
    for t in threads: t.join()
        
    total_esperado = 10 * 50  # = 500
    print(f"Esperado: {total_esperado}")
    print(f"Resultado real: {counter.value}")
    print(f"Incrementos PERDIDOS: {total_esperado - counter.value}")
    assert counter.value < total_esperado, (
        f"RACE CONDITION DEMOSTRADA: esperábamos {total_esperado} "
        f"pero obtuvimos {counter.value}. "
        f"Se perdieron {total_esperado - counter.value} incrementos."
    )