"""
UNA FUNCION ES UN CONJUNTO DE INSTRUCCIONES AGRUPADAS
BAJO UN NOMBRE CONCRETO QUE PUEDEN REUTILIZARSE INVOCANDO
A LA FUNCION TANTAS VECES COMO SEA NECESARIO

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1
print("##### EJEMPLO 1 ####")

# Definir funcion
def muestraNombre():
    print("Cristhian")
    print("Juan")
    print("Francisco")
    print("Aitor")
    print("Nestor")
    print("\n")

# Invocar funcion
muestraNombre()
muestraNombre()
muestraNombre()

# Ejemplo 2: parametros
print("##### EJEMPLO 2 ####")

"""
def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombreInput = input("Introduce tu nombre: ")
edadInput = int(input("Introduce tu edad: "))
mostrarTuNombre(nombreInput, edadInput)
"""

# Ejemplo 3
print("##### EJEMPLO 3 ####")

def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} X {contador} = {operacion}")
    
    print("\n")

tabla(3)
tabla(7)
tabla(12)

# Ejemplo 3.1
print("--------------------")
for numero_tabla in range(1,11):
    tabla(numero_tabla)

# Ejemplo 4: Parametros opcionales
print("\n##### EJEMPLO 4 ####")

def getEmpleado(nombre,dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado('Cristhian Mayuri',44385495)

# Ejemplo 5: Return o devolver datos
print("\n##### EJEMPLO 5 ####")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame('Cristhian Mayuri'))

# Ejemplo 6
print("\n##### EJEMPLO 6 ####")

def calculadora(numero1,numero2,basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return(cadena)

print(calculadora(3,2,True))

# Ejemplo 7
print("\n##### EJEMPLO 7 ####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Cristhian", "Mayuri Quiroz"))

# Ejemplo 8: Funciones Lambda
print("\n##### EJEMPLO 8 ####")

dime_el_year = lambda year: f"El año es {year * 50}"

print(dime_el_year(2025))