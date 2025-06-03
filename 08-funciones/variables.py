"""
Una variable local es aquella que se defien dentro de la funcion
Una variable global es la que se declara fuera de la funcion y esta
disponible fuera y dentro de la funcion
"""

# Variable global

frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase = "Hola mundo!!"
    print("Dentro de la funcion")
    print(frase)

    year = 2021
    print(year)

    global website
    website = "elblogdelmayu.io"
    print("DENTRO: " + website)

    return "Dato devuelto: " + str(year)

print(holaMundo())
print("FUERA: " + website)