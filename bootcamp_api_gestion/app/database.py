# app/database.py
# FASE 1: Separación de datos
clientes_db = []
productos_db = []
ventas_db = []

def reset_database():
    global clientes_db, productos_db, ventas_db
    clientes_db.clear()
    productos_db.clear()
    ventas_db.clear()
