##EN este proyecto almacenara los datos

Tareas = []

def agregar_tarea (descripcion):
    tarea ={
        "descripcion" : descripcion,
        "esta_completada" : False
    }
    Tareas.append(tarea)

def Listar_tareas():
    return Tareas

def Marcar_completada(index):
    try:
        Tareas[index]["esta completada"] = True
    except IndexError:
        print("!!!!!indice no valido!!!!!") 


def Eliminar_tarea (index):
    try:
        Tareas.pop(index)
    except IndexError:
        print("!!!!indice no valido!!!!!")
