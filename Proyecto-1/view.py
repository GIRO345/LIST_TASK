#se encarga de mostar mensajes e interraractua con el usuario
def mostrar_menu(): #defino la funcion MENU
    print("\n~~~===Gestor de tareas===~~~")#MENU
    print("1. Agregar tarea")#MENU
    print("2. listar tarea")#MENU
    print("3. Marcar tarea completada")#MENU
    print("4. Eliminar tarea")#MENU
    print("0. Salir")

def obtener_seleccion(): #funcion 
    mostrar_menu() #muestrar menu
    while True: # ciclo en el cual SI EL USUARIO SE EQUIVOCA VUELVA A IMPRIMIR EL MENU, HASTA QUE SELECCIONE LA OPCION CORRECTA
        try: #captura de exepciones "error" que pueden ocurrir
         seleccion = int(input("selecione de 0 a 4: ")) # capturo el numero 
        except ValueError:#exepcion de tipo value error
            print("Dijite un numero válido") #imprima
            continue #continua la siguiente linea
        if seleccion < 0 or seleccion > 4  : # condicional "se la seleccion echa por el usuario es menor que 0 o es mayor que 4 "
            print("Numero no valido, solo [0 de 4]") #imprima numero no valido
            continue #continua la siguiente linea
        else: #si no 
            return seleccion #lo que retorna la funcion obtener seleccion
    
def Mostar_tareas(Tareas): #funcion
    if len(Tareas) == 0 : #si la longitud de La lista Tareas es 0 en este caso VACIA
        print("No hay tareas Aún") #Imprima 
    else: #si no,  esta vacia
        print("######### Tareas #########") #menu
        print("ID", "Estado","\t", "Tarea")#menu
        for index in range(0 , len(Tareas)): #PARA recorrer el indice desde 0 hasta todo lo que haya en la lista "Tareas"
            estado = "completado " if Tareas [index]["esta_completada"] else "Pendiente" #el estado, se va a marcar completado
            #si el indice, usuario dijita el indice de la tarea de tareas, no queda en estado pendiente
            print(index, "-", estado, "\t", Tareas[index]["descripcion"])#menu

def mostrar_mensaje (mensaje):#funcion 
    print(mensaje)


def obtener_indice():#funcion
    try: #captura de exepcion
        indice = int(input("dijite el indice: ")) #pide al usuario el indice de la tarea
        return indice #retorna la funcion
    except ValueError: #exepcion tipo valueError
        print ("El numero dijitado, !NO! es valido")


def obtener_tarea(): #funcion
    tarea = input(("Escriba la tarea: ")) # pide al usuario la tarea que desea agregar a la lista
    return tarea #retorna la funcion