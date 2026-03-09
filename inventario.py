productos = []

def agregar_producto(nombre, precio, cantidad):
    """
    Agrega un producto al inventario.
    """
    producto = {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
    productos.append(producto)

def listar_productos():
    """
    Devuelve la lista completa de productos.
    """
    return productos

def actualizar_producto(valor_buscar, tipo_buscar, tipo_actualizar, nuevo_valor):
    """
    Actualiza todos los productos que coincidan con valor_buscar en tipo_buscar.
    
    - valor_buscar: valor por el cual buscamos el producto
    - tipo_buscar: 'nombre', 'precio' o 'cantidad'
    - tipo_actualizar: 'nombre', 'precio' o 'cantidad'
    - nuevo_valor: valor que se va a asignar
    """
    encontrados = 0
    for p in productos:
        if str(p[tipo_buscar]) == str(valor_buscar):
            if tipo_actualizar == "nombre":
                p['nombre'] = nuevo_valor
            elif tipo_actualizar == "precio":
                p['precio'] = float(nuevo_valor)
            elif tipo_actualizar == "cantidad":
                p['cantidad'] = int(nuevo_valor)
            encontrados += 1
    return encontrados  

def eliminar_producto(valor_buscar, tipo_buscar):
    """
    Elimina todos los productos que coincidan con valor_buscar en tipo_buscar.
    
    - valor_buscar: valor por el cual buscamos el producto
    - tipo_buscar: 'nombre', 'precio' o 'cantidad'
    
    Devuelve la lista de productos eliminados.
    """
    eliminados = []
    for p in productos[:]:  
        if str(p[tipo_buscar]) == str(valor_buscar):
            productos.remove(p)
            eliminados.append(p)
    return eliminados

def calcular_valor_total():
    """
    Devuelve la suma de precio * cantidad de todos los productos.
    """
    return sum(p['precio'] * p['cantidad'] for p in productos)