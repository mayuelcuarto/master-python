"""

# Condicional if

SI se cumple esta condición:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones

# Operadores de comparación
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores lógicos
and Y
or O
! negación
not NO

"""

#Ejemplo 1
print("########### EJEMPLO 1 ###########")

color = "verde"
#color = input("Adivina cual es mi color favorito:")

if color == "rojo":
   print("Enhorabuena!!")
   print("El color es ROJO")
else:
   print("Color incorrecto!")

#Ejemplo 2
print("\n########### EJEMPLO 2 ###########")

year = 2020
#year = int(input("¿En que año estamos? "))

if year < 2021:
    print("Estamos antes de 2021!!")
else:
    print("Es un año posterior a 2021")

#Ejemplo 3
print("\n########### EJEMPLO 3 ###########")

nombre = "Cristhian Mayuri"
ciudad = "Lima"
continente = "Europa"
edad = 37
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad!!")

    if continente != "Europa":
        print(f"{nombre} NO es Europeo")
    else:
        print(f"Es europeo y de ciudad {ciudad}")
else:
    print(f"{nombre} NO es mayor de edad!!")

#Ejemplo 4
print("\n########### EJEMPLO 4 ###########")

dia = 1
#dia = int(input("Introduce el número del día de la semana: "))

"""
if dia == 1:
    print("Es Lunes")
else:
    if dia == 2:
        print("Es Martes")
    else:
        if dia == 3:
            print("Es Miércoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
                else:
                    print("Es fin de semana")
"""

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miércoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")

#Ejemplo 5
print("\n########### EJEMPLO 5 ###########")

edad_minima = 18
edad_maxima = 65
edad_oficial = 17
#edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Está en edad de trabajar!!")
else:
    print("NO está en edad de trabajar!!")

#Ejemplo 6
print("\n########### EJEMPLO 6 ###########")

pais = "Rusia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} NO es un país de habla hispana :(")

#Ejemplo 7
print("\n########### EJEMPLO 7 ###########")

pais = "España"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un país de habla hispana")
else:
    print(f"{pais} SI es un país de habla hispana :)")

#Ejemplo 8
print("\n########### EJEMPLO 8 ###########")

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un país de habla hispana")
else:
    print(f"{pais} SI es un país de habla hispana :)")