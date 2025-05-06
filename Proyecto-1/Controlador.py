from Model import *

agregar_tarea("preparar Almuerzo")
agregar_tarea("Arreglar cocina")
agregar_tarea("Acomodar Mercado")
agregar_tarea("barrer patio")




Marcar_completada(1)

print(Listar_tareas())

Eliminar_tarea(30)

print(Listar_tareas())