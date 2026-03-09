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
    while True:
        separador()
        print("""
=== LISTA DE PRODUCTOS ===
1. Ver todos los productos
2. Volver al menú principal
""")
        separador()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            productos = inventario.listar_productos()
            if not productos:
                print("No hay productos en el inventario.")
            else:
                for p in productos:
                    print(f"{p['nombre']} - Q{p['precio']} - Cantidad: {p['cantidad']}")
        elif opcion == "2":
            break
        else:
            print("Opción inválida, intente de nuevo.")

def menu_actualizar():
    while True:
        separador()
        print("""
=== ACTUALIZAR PRODUCTO ===
1. Actualizar producto
2. Volver al menú principal
""")
        separador()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            tipo_buscar = input("Buscar producto por (nombre/precio/cantidad): ").lower()
            valor_buscar = input(f"Ingrese el valor del {tipo_buscar} a buscar: ")
            tipo_actualizar = input("Qué desea actualizar? (nombre/precio/cantidad): ").lower()
            nuevo_valor = input("Ingrese el nuevo valor: ")
            actualizados = inventario.actualizar_producto(valor_buscar, tipo_buscar, tipo_actualizar, nuevo_valor)
            if actualizados > 0:
                print(f"{actualizados} producto(s) actualizado(s) ✔")
            else:
                print("No se encontró ningún producto que coincida")
        elif opcion == "2":
            break
        else:
            print("Opción inválida, intente de nuevo.")

def menu_eliminar():
    while True:
        separador()
        print("""
=== ELIMINAR PRODUCTO ===
1. Eliminar producto
2. Volver al menú principal
""")
        separador()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            tipo_buscar = input("Eliminar producto por (nombre/precio/cantidad): ").lower()
            valor_buscar = input(f"Ingrese el valor del {tipo_buscar} a eliminar: ")
            eliminados = inventario.eliminar_producto(valor_buscar, tipo_buscar)
            if eliminados:
                print(f"{len(eliminados)} producto(s) eliminado(s) ✔")
            else:
                print("No se encontró ningún producto que coincida")
        elif opcion == "2":
            break
        else:
            print("Opción inválida, intente de nuevo.")

def calcular_valor_inventario():
    while True:
        separador()
        print("""
=== VALOR TOTAL DEL INVENTARIO ===
1. Mostrar valor total
2. Volver al menú principal
""")
        separador()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            total = inventario.calcular_valor_total()
            print(f"Valor total: Q{total}")
        elif opcion == "2":
            break
        else:
            print("Opción inválida, intente de nuevo.")

def menu_salir():
    separador()
    print("""
GRACIAS POR USAR ESTE PROGRAMA
""")
    separador()



while True:
    menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        menu_agregar()
    elif opcion == "2":
        menu_lista()
    elif opcion == "3":
        menu_actualizar()
    elif opcion == "4":
        menu_eliminar()
    elif opcion == "5":
        menu_valor()
    elif opcion == "6":
        menu_salir()
        break
    else:
        print("Opción inválida, intente de nuevo.")