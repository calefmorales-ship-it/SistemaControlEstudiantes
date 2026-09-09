def show_menu():
    valid_options = ["1", "2", "3", "4", "5", "6", "7"]
    while True:
        print("===================================")
        print(" Sistema de Control de Estudiantes ")
        print("===================================")
        print("1. Agregar estudiante")
        print("2. Ver estudiantes")
        print("3. Top 3 estudiantes")
        print("4. Promedio general")
        print("5. Exportar CSV")
        print("6. Importar CSV")
        print("7. Salir\n")
        option = input("Seleccione una opción: ")
        if option in valid_options:
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    return option