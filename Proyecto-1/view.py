def mostrar_menu():
    print("\n~~~===Gestor de tareas===~~~")
    print("1. Agregar tarea")
    print("2. listar tarea")
    print("3. Marcar tarea completada")
    print("4. Eliminar tarea")
    print("0. Salir")

def obtener_seleccion():
    mostrar_menu()
    while True:
        try:
         seleccion = int(input("selecione de 1 a 5: "))
        except ValueError:
            print("Dijite un numero válido")
            continue
        if seleccion < 1 or seleccion > 5 :
            print("Numero no valido, solo [0 de 5]")
            continue
        else:
            return seleccion
    
def Mostar_tareas(Tareas):
    if len(Tareas) == 0 :
        print("No hay tareas Aún")
    else:
        print("######### Tareas #########")
        print("ID", "Estado","\t", "Tarea")
        for index in range(0 , len(Tareas)):
            estado = "completado " if Tareas [index]["esta completada"] else "Pendiente"
            print(index, "-", estado, "\t", Tareas[index]["descripcion"])

def mostrar_mensaje (mensaje):
    print(mensaje)


def ontener_indice():
    try:
        indice = int(input("dijite el indice"))
        return indice
    except ValueError:
        print ("El numero dijitado, !NO! es valido")


def ontener_tarea():
    tarea = input(("Escriba la tarea: ")) 
    return tarea