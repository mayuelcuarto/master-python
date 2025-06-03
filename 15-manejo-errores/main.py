# Capturar excepciones y manejar errores en código
# susceptible a fallos

"""
try:
    nombre = input("¿Cuál es tu nombre?:")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, ingresa bien el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la iteración")
"""

# Multiples excepciones
"""
try:
    numero = int(input("Número para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero * numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros en el código!!")
#except ValueError:
#    print("Introduce un número correcto")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)
"""

# Excepciones personalizadas o lanzar excepcion

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido al master en python {nombre}")
except ValueError:
    print("Introduce los datos correctamente!!")
except Exception as e:
    print("Existe un error: ", type(e).__name__)