"""
Ejercicio 5
Crear un programa que muestre los numeros entre un numero y el otro
"""

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

if(numero_1 < numero_2):
    while numero_1 <= numero_2:
        print(f"{numero_1}")
        numero_1 += 1
else:
    print("El número 1 debe ser menor al número 2")