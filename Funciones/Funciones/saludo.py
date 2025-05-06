from datetime import datetime



def saludo (Nombre):
    hora = datetime.now ().hour
    if hora < 18:
        return "Hola: " + Nombre + "Buenas tardes"
    else:
        return "Hola: " + Nombre + " Buenas Noches"
    

print(saludo("Angel"))