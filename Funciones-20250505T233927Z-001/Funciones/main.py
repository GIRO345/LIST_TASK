from vistas import obtener_opcion
from vistas import obtener_dato
from areas import *

seleccion = obtener_opcion()

if seleccion == 4:
    Radio = obtener_dato("Radio", "circulo")
    area = calcular_area_circulo (Radio)
elif  seleccion ==1:
    Base = obtener_dato ("Base", "Triangulo")
    Altura = obtener_dato ("Altura", "Triangulo")
    area = area_triangulo (Base,Altura)
elif seleccion == 2:
    Base = obtener_dato ("Base", "Altura")
    Altura = obtener_dato ("Altura", "Rectangulo")
    area = Area_rectangulo (Base,Altura)
elif seleccion == 3:
    Lado = obtener_dato ("Lado", "Apotema")
    Apotema = obtener_dato ("Altura", "pentagono")
    area = Area_pentagono (Lado,Apotema)
    
    
print("El Calculo del area es: ",area)















#print("El area del triangulo es:", area)
##print("El calculo del area es: ", area)

#print("El Calculo del area es: ", calcular_area_circulo(12.5))
