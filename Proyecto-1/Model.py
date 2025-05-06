##EN este proyecto almacenara los datos

Tareas = []

def agregar_tarea (descripcion):
    tarea ={
        "descripcion" : descripcion,
        "esta_completada" : False
    }
    Tareas.append(tarea)