import inventario

# Función para separar visualmente los menús
def separador():
    print("-"*15)

def menu_principal():
    separador()
    print("""
BIENVENIDO 
1. AGREGAR PRODUCTO
2. LISTA PRODUCTOS
3. ACTUALIZAR CANTIDAD
4. ELIMINAR PRODUCTO
5. CALCULAR VALOR TOTAL DEL INVENTARIO
6. SALIR
""")
    separador()

def menu_agregar():
    while True:
        separador()
        print("""
=== AGREGAR PRODUCTO ===
1. Ingresar nuevo producto
2. Volver al menú principal
""")
        separador()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio (Q): "))
            cantidad = int(input("Cantidad: "))
            inventario.agregar_producto(nombre, precio, cantidad)
            print("Producto agregado ✔")
        elif opcion == "2":
            break
        else:
            print("Opción inválida, intente de nuevo.")
   
def menu_lista():
    pass

def menu_actualizar():
    pass

def menu_eliminar():
    pass

def menu_salir():
    pass