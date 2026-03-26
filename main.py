def mostrar_menu():
    print("\n1) Agregar producto")
    print("2) Mostrar inventario")
    print("3) Calcular estadísticas")
    print("4) Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Not created")
    elif opcion == "2":
        print("Función aún no implementada")
    elif opcion == "3":
        print("Not created")
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("✕ Opción inválida, intenta otra vez")