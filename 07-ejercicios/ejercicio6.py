"""
Ejercicio 6:
Mostrar todas las tablas del 1 al 10
"""

for contador in range(1,11):
    print(f"\nTabla del {contador}\n")
    for multiplicador in range(1,11):
        print(f"{contador} X {multiplicador} = {contador * multiplicador}")