"""
Ejericicio 4. 
Crear un script que tenga 4 variables, una lista, un string, un entero y un boolean
Y que imprima un mensaje según el tipo de dato de cada variable. Usar funciones
"""

lista = []
cadena = ""
entero = 0
boleano = True

def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "ENTERO"
    elif tipo == bool:
        result == "BOOLEANO"

    return result 


def imprimirTipo(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""

    if test:
        result = f"Este dato es de tipo: {traducirTipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    
    return result

print(imprimirTipo(lista, list))
print(imprimirTipo(cadena, str))
print(imprimirTipo(entero, int))
print(imprimirTipo(boleano, bool))