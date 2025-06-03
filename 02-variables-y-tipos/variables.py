#Crear variables y asignarles un valor
texto = "Máster en Python"
texto2 = "con Victor Robles"
numero = 45
decimal = 6.7

#Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("---------------------")

#Reasignar variables
numero = 77
decimal = 8.9

print(numero)
print(decimal)

#Concatenacion
nombre = "Victor"
apellido = "Robles"
web = "victorroblesweb.es"

print(nombre + " " + apellido + " - " + web)
print(f"{nombre} {apellido} - {web}")
print("Hola me llamo {} {} y mi web es {}".format(nombre, apellido, web))

print(nombre, apellido, web)