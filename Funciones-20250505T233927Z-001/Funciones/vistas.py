def menu_principal():
    print("##### MENU #####")
    print("1. Area del triangulo")
    print("2. Area del rectangulo")
    print("3. Area del pentangono")
    print("4. Area del circulo")
    print("0. salir")
    
def obtener_opcion():
    while True : # crea un bucle  para cuando se digite un numero no valido se reinicie 
        menu_principal()
        try: # control de exepciones " controlo los errores que puedan ocurrir en el codigo" intenta abrir y leer un archivo.
         opcion = int(input("Dijite La opcion de [0 A 4]: "))
        except : #manejo el tipo de error en este caso valueError - o se deja en blanco para capturar todos los tipos de Errores
            print ("Careacteres no Válidos, Ingrese Solo numeros")
            continue
        finally: #El bloque finally se ejecuta siempre, independientemente de si se produjo una excepción o no, asegurando que el archivo se cierre correctamente.
            if opcion < 0: #condicional
                print("ERROR: ¡NUMERO NO VALIDO!")
                continue #continuo a la siguiente linea 
            elif opcion <= 5: #
                return opcion
            else:
             print("ERROR: ¡NUMERO NO VALIDO!")
            continue
        
def obtener_dato(Nombre_dato, Figura):
    while True :
        try:
            dato = float(input("Escriba "+Nombre_dato+" del "+Figura+":"))
        except :
            print("Error al ingresar dato para ", Figura)
            continue
        
        return dato



        

    