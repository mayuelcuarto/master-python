"""
Ejercicio 9:
Hacer un programa que pida números al usuario indefinidamente hasta ingresar el 111
"""
numero = 0
while numero != 111:
    numero = int(input("Ingresa un nuevo número: "))
    print(f"Has introducido el número: {numero}")