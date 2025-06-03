"""
Ejercicio 3: Programa que compruebe si una variable está vacia
y si está vacía rellenarlo con texto en minusculas y mostrarlo en mayusculas
"""

texto = input("Ingrese un texto cualquiera:")

if len(texto.strip()) <= 0:
    texto = "el texto se encuentra vacío"
    print(texto.upper())
else:
    print(f"Usted ingreso el texto {texto}")