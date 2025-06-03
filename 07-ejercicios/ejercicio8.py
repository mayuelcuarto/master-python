"""
Ejercicio 8:
Conseguir el tanto por ciento de un número y un porcentaje ingresados
"""

numero = int(input("Ingresa el número: "))
porcentaje = int(input(f"Qué porcentaje quieres sacar de {numero}: "))

tanto_porciento = numero * (porcentaje/100)
print(f"El porcentaje es: {tanto_porciento}")