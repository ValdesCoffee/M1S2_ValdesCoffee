productos = []  # Lista vacía donde se van a guardar todos los productos como diccionarios

def mostraremuñoa():  # Función para mostrar el menú principal
    print("\n1) Agregar producto\n2)Mostrar inventario\n3)Calcular estadisticas")  # Opciones del sistema
    print("\n 4) Salir (❁´◡`❁)")  # Opción para salir

def Agregarproducto(nombre,precio, cantidad, categoria, lista):  # Función que recibe datos y agrega un producto
    nuevo_producto ={  # Se crea un diccionario con la info del producto
        "Producto": nombre,  # Nombre del producto
        "Precio": precio,  # Precio por unidad
        "Cantidad": cantidad,  # Cantidad disponible
        "Categoria": categoria,  # Categoría del producto
    }
    lista.append(nuevo_producto)  # Se agrega el diccionario a la lista principal

def Mostrarproducto(productos):  # Función para mostrar todos los productos
    for idx, mostrar in enumerate(productos):  # Recorre la lista con índice incluido
        print(f"{idx+1}. Producto: {mostrar['Producto']} | Precio: {mostrar['Precio']} | Cantidad: {mostrar['Cantidad']} | Categoria: {mostrar['Categoria']}")  # Imprime cada producto bonito
    print("Listo ☆")  # Mensaje final

def calcularproducts(productos):  # Función para calcular el valor total de cada producto
    for producto in productos:  # Recorre cada producto de la lista
        iti = producto["Producto"]  # Guarda el nombre del producto
        precio = producto["Precio"]  # Guarda el precio
        cantidadeofjoijgi = producto["Cantidad"]  # Guarda la cantidad (nombre medio cursed pero sirve XD)

        propeso = precio * cantidadeofjoijgi  # Calcula el valor total (precio * cantidad)

        print(f"\nTu {iti} tiene este precio {precio} por unidad")  # Muestra precio unitario
        print(f"Con el precio total de {propeso}")  # Muestra precio total

while True:  # Bucle infinito para que el programa siga corriendo hasta que el usuario salga
    mostraremuñoa()  # Muestra el menú
    sdk= input("Elige una opcion por favor: ")  # Pide al usuario una opción

    if sdk== "1":   # Si elige agregar productos
        cantidad_a_registrar= int(input("Ingrese la cantidad de productos que va a registrar: "))  # Cuántos productos quiere ingresar
        for producto in range(cantidad_a_registrar):  # Bucle para repetir el ingreso varias veces
            iti= input("Coloque su producto: ")  # Pide nombre del producto
            precio= float(input("Coloque el precio: "))  # Pide precio y lo convierte a float
            cantidadeofjoijgi= int(input("Coloque la cantidad de su producto: "))  # Pide cantidad y la convierte a entero
            categoria= input("❁ Coloque su categoria:  ")  # Pide categoría
            Agregarproducto(iti,precio,cantidadeofjoijgi,categoria,productos)  # Llama a la función para guardar el producto

    elif sdk == "2":  # Si elige mostrar productos
         Mostrarproducto(productos)  # Llama a la función para mostrar inventario

    elif sdk == "3":  # Si elige calcular estadísticas
         calcularproducts(productos)  # Llama a la función que calcula totales

    elif sdk == "4":  # Si elige salir
        print("Saliendo del sistema.｡.:*☆")  # Mensaje de despedida
        break  # Rompe el bucle infinito y termina el programa