"""
Ejercicio 3
Crear un programa que imprima por pantalla los cuadrados (un numero multiplicado por si mismo) 
de los primeros 60 numeros naturales. Resolverlo con for y con while.
"""

for numero_natural in range(61):
    print(f"El cuadrado de {numero_natural} es {numero_natural * numero_natural}")

numero_natural_2 = 0
while numero_natural_2 <= 60:
    print(f"El cuadrado de {numero_natural_2} es {numero_natural_2 * numero_natural_2}")
    numero_natural_2 += 1