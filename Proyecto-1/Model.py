##EN este proyecto se encarga de manejar los datos, es decir listar

Tareas = [] #lista 

def agregar_tarea (descripcion): #define funcion
    tarea ={
        "descripcion" : descripcion, #atributo "DESCRIPCION"
        "esta_completada" : False #atributo boolenao "FALse"
    }
    Tareas.append(tarea)

def Listar_tareas():
    return Tareas

def Marcar_completada(index):
    try: # captura exepcion 
        Tareas[index]["esta_completada"] = True #en la posicion #INDICE#
    except IndexError: #exepcion tipo indexError
        print("!!!!!indice no valido!!!!!") #imprime


def Eliminar_tarea (index):
    try: # capturar exepcion
        Tareas.pop(index) # con la funcion "POP" elimino la tarea dijitando el indice
    except IndexError: #exepcion tipo IndexError
        print("!!!!indice no valido!!!!!")
