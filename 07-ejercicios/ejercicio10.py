"""
Ejercicio 10:
Crear un programa que pida la nota de 15 alumnos e indique cuantos han aprobado y cuántos han suspendido
"""

aprobados = 0
desaprobados = 0

for contador in range(1,16):
    nota = int(input(f"Ingresa la nota {contador}: "))
    if nota <= 10:
        desaprobados += 1
    else:
        aprobados += 1

print(f"La cantidad de aprobados es: {aprobados}")
print(f"La cantidad de desaprobados es: {desaprobados}")
