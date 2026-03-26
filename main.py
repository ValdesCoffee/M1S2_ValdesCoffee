inventario = []
def mostraremuñoa():
    print("\n1) Agregar producto\n2)Mostrar inventario\n3)Calcular estadisticas")
    print("\n 4) Salir (❁´◡`❁)")
def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("✓ Producto agregado")

while True:
    mostraremuñoa()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        print("Pendiente")
    elif opcion == "3":
        print("Pendiente")
    elif opcion == "4":
        break
    else:
        print(" Opción inválida")