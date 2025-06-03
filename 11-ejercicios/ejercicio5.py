"""
Ejercicio 5:
Crear una lista con el contenido de esta tabla:
VIDEOJUEGOS
ACCION: GTA, COD, PUBG
AVENTURA: ASSASIN'S CREED, CRASH BANDICOT, PRINCE OF PERSIA
DEPORTES: FIFA, PRO EVOLUTION, MOTO GP

Mostrar esta información ordenada
"""

videojuegos = [
    {
        "categoria":"ACCION",
        "juegos": ["GTA","COD","PUBG"]
    },
    
    {
        "categoria":"AVENTURA",
        "juegos":["ASSASIN'S CREED","CRASH BANDICOT","PRINCE OF PERSIA"]
    },
    {
        "categoria":"DEPORTES",
        "juegos":["FIFA","PRO EVOLUTION","MOTO GP"]
    }
]

for categoria in videojuegos:
    print(f"---------Categoria: {categoria['categoria']}---------")
    for juego in categoria['juegos']:
        print(f"Juego: {juego}")