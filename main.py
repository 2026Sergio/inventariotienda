def menu_principal():
    menu = """
BIENVENIDO 
1. AGREGAR PRODUCTO
2. LISTA PRODUCTOS
3. ACTUALIZAR CANTIDAD
4. ELIMINAR PRODUCTO
5. CALCULAR VALOR TOTAL DEL INVENTARIO
6. SALIR
"""
    print(menu)


while True:
    menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Agregar producto")

    elif opcion == "2":
        print("Lista de productos")

    elif opcion == "3":
        print("Actualizar cantidad")

    elif opcion == "4":
        print("Eliminar producto")

    elif opcion == "5":
        print("Calcular valor total")

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida")

def lista_producto():
    print("*"*15)

def Actualizar_producto():
    pass

def Eliminar_producto():
    pass

def Calcular_valor_inventario():
    pass

def salir():
    print("Saliendo del programa...")
    exit()