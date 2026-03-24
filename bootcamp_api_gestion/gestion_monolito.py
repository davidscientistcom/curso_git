# gestion_monolito.py
# FASE 0: Ejemplo de Anti-Patrones y Código Espagueti
# NO USAR EN PRODUCCIÓN

clientes_db = []
productos_db = []
ventas_db = []

def crear_cliente(nombre, email, edad, tipo):
    if nombre != "" and nombre is not None:
        if email != "" and "@" in email:
            if type(edad) == int:
                if edad >= 18:
                    if tipo == "VIP" or tipo == "NORMAL":
                        nuevo_id = len(clientes_db) + 1
                        cliente = {
                            "id": nuevo_id,
                            "nombre": nombre,
                            "email": email,
                            "edad": edad,
                            "tipo": tipo,
                            "activo": True
                        }
                        clientes_db.append(cliente)
                        return True
                    else:
                        print("Tipo de cliente invalido")
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def crear_producto(nombre, precio, stock):
    if not isinstance(nombre, str) or len(nombre) == 0:
        return {"error": "Nombre invalido"}
    
    if type(precio) == int or type(precio) == float:
        if precio > 0:
            if type(stock) == int and stock >= 0:
                prod_id = len(productos_db) + 1
                producto = {
                    "id": prod_id,
                    "nombre": nombre,
                    "precio": precio,
                    "stock": stock
                }
                productos_db.append(producto)
                return producto
            else:
                return {"error": "Stock invalido"}
        else:
            return {"error": "Precio negativo"}
    else:
        return {"error": "Precio no numerico"}

def realizar_venta(cliente_id, producto_id, cantidad):
    cliente = None
    for c in clientes_db:
        if c["id"] == cliente_id:
            cliente = c
            break
            
    if cliente is not None:
        if cliente["activo"] == True:
            producto = None
            for p in productos_db:
                if p["id"] == producto_id:
                    producto = p
                    break
                    
            if producto is not None:
                if producto["stock"] >= cantidad:
                    if cantidad > 0:
                        descuento = 0
                        if cliente["tipo"] == "VIP":
                            descuento = 0.15
                        elif cliente["tipo"] == "NORMAL" and cantidad > 10:
                            descuento = 0.05
                            
                        total = (producto["precio"] * cantidad) * (1 - descuento)
                        producto["stock"] = producto["stock"] - cantidad
                        
                        venta = {
                            "id": len(ventas_db) + 1,
                            "cliente_id": cliente_id,
                            "producto_id": producto_id,
                            "cantidad": cantidad,
                            "total": total,
                            "descuento_aplicado": descuento
                        }
                        ventas_db.append(venta)
                        return venta
                    else:
                        return "La cantidad debe ser mayor a cero"
                else:
                    return "No hay suficiente stock"
            else:
                return "Producto no encontrado"
        else:
            return "El cliente no esta activo"
    else:
        return "Cliente no encontrado"

def borrar_datos_para_testing():
    global clientes_db, productos_db, ventas_db
    clientes_db = []
    productos_db = []
    ventas_db = []
