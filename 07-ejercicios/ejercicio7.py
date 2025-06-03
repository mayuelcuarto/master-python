"""
Ejercicio 7:
Mostrar todos los numeros impares que hay en un rango dado por el usuario
"""

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

if numero_1 < numero_2:
    while numero_1 <= numero_2:
        if numero_1 % 2 == 0:
            print(f"{numero_1} ES PAR")
        else:
            print(f"{numero_1} ES IMPAR")
        numero_1 += 1
else:
    print("El primer número debe ser menor que el segundo")