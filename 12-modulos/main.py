"""
Modulos: Son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos que los puedes consultar aquí:
https://docs.python.org/3.13/py-modindex.html

Podemos conseguir que ya vienen en el lenguaje, modulos en internet
y también podemos crear nuestros propios modulos.
"""

# Importar modulo propio
# import mimodulo
# from mimodulo import holaMundo

from mimodulo import *

print(holaMundo("Cristhian Mayuri"))
print(calculadora(3,2,True))

# Modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada:" + fecha_personalizada)

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())

# Modulo matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Número PI: ", float(math.pi))
print("Redondear: ", math.ceil(6.56789))
print("Redondear: ", math.floor(6.56789))

# Modulo random
import random

print("Número aleatorio entre 15 y 67: ", random.randint(15,67))