"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

numeros = [1,13,4,15,6,8,9,12]

print("--------LISTA NORMAL---------")
for numero in numeros:
    print(f"Elemento: {numero}")

def recorrerLista(numeros):
    cadena = ""
    for numero in numeros:
        cadena += "Elemento: " + str(numero) + "\n"
    return(cadena)

print("\n--------LISTA ORDENADA---------")

numeros.sort();

print(recorrerLista(numeros))

print(f"La longitud de la lista es: {len(numeros)}")

try:
    numero_buscar = int(input("Ingrese el número que desea buscar:"))

    comprobar = isinstance(numero_buscar, int)
    while not comprobar or numero_buscar <= 0:
        numero_buscar = int(input("Ingrese el número que desea buscar:"))
    else:
        print(f"Has introducido el {numero_buscar}")

    print(f"###BUSCAR EN LA LISTA EL NÚMERO {numero_buscar}###")

    search = numeros.index(numero_buscar)
    print(f"El número buscado existe en la lista, es el índice: {search}")
except:
    print("El número no está en la lista, lo siento")