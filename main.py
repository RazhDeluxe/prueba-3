import os, globales, json
os.system("cls")

def menu_general():
    while True:
        os.system("cls")
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadís;cas.")
        print("3. Salir del programa.")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("1. Asignar montos aleatorios.")
        elif opcion == 2:
            print("2. Ver estadís;cas.")
        elif opcion == 3:
            print("3. Salir del programa.")
            return
    
    
if __name__ == "__main":
    menu_general()
