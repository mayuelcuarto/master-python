"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista.
Plus: Usar wile y for
"""

coleccion = []

contador = 0
while len(coleccion) < 120:
    #valor = input("Ingrese un valor para la lista:")
    coleccion.append(f"elemento-{contador}")
    print(f"El valor se ingreso en el {coleccion[contador]}")
    contador+=1

"""
for longitud in range(0,120):
    #valor = input("Ingrese un valor para la lista:")
    coleccion.append(f"elemento-{longitud}")
    print(f"El valor se ingreso en el {coleccion[longitud]}")
"""

print(coleccion)