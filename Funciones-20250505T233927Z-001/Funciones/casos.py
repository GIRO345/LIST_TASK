opcion = int(input("Escriba un numero: "))
if opcion == 1 :
    print ("uno")
elif opcion == 2:
    print("dos")
else :
    print("otro numero ")
    

opcion = int(input("Escriba un numero: "))
match opcion :
    case 1: 
        print ("uno")
    case 2: 
        print ("dos")
    case 3: 
        print("otro numero ")