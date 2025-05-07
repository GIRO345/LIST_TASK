#se encargara de recibir las acciones del usuario y coordinar la vita
from Model import * #llamo desde el archivo model a todas las funciones dentro de ese archivo
from view import * #llamo desde el archivo view a todas las funciones dentro de ese archivo


while True:
    opcion = obtener_seleccion()#

    if opcion == 1 : #si la opcion es igual 1
        nombre_tarea = obtener_tarea() #obtengo la tarea mediante la funcion
        agregar_tarea (nombre_tarea) #agrego la tarea mediante la descripcion 
    elif opcion == 2 :
        todas_tareas = Listar_tareas()
        Mostar_tareas(todas_tareas)
    elif opcion == 3:
        indice = obtener_indice()
        Marcar_completada(indice)
    elif opcion == 4:
        indice = obtener_indice()
        Eliminar_tarea = (indice)
    else :
        print("Bye")
        break