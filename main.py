productos = []
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

    productos.append(producto)
    print("✓ Producto agregado")
def Mostrarproducto(productos):
    for idx, mostrar in enumerate(productos):
        print(f"{idx+1}. Producto: {mostrar['Producto']} | Precio: {mostrar['Precio']} | Cantidad: {mostrar['Cantidad']} | Categoria: {mostrar['Categoria']}")
    print("Listo ☆")
def Agregarproducto(nombre,precio, cantidad, categoria, lista):
    nuevo_producto ={
        "Producto": nombre, 
        "Precio": precio,
        "Cantidad": cantidad,
        "Categoria": categoria,
    }
    lista.append(nuevo_producto)
while True:
    mostraremuñoa()
    sdk = input("Elige una opción: ")

    if sdk== "1":   
        cantidad_a_registrar= int(input("Ingrese la cantidad de productos que va a registrar: "))
        for producto in range(cantidad_a_registrar):
            iti= input("Coloque su producto: ")
            precio= float(input("Coloque el precio: "))
            cantidadeofjoijgi= int(input("Coloque la cantidad de su producto: "))
            categoria= input("❁ Coloque su categoria:  ")
            Agregarproducto(iti,precio,cantidadeofjoijgi,categoria,productos)

    elif sdk == "2":
         Mostrarproducto(productos)
    elif sdk == "3":
        print("Pendiente")
    elif sdk == "4":
        break
    else:
        print(" Opción inválida")