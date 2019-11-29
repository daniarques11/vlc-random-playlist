from parseadorXML import getDiccionarioRutas
from cancionesRandom import getCancionesRandom
from os import access, F_OK, popen

# Obtener diccionario con rutas como keys, e id como valores
# para luego devolver lista con rutas random


def ejecutarVLC(vlcRuta, listaCanciones):
    verificarRutaVLC(vlcRuta)
    stringRutas = getStringRutas(listaCanciones)
    comandoCMD = vlcRuta + " " + stringRutas + "--play-and-exit"
    popen(comandoCMD)


def getStringRutas(listaRutas):
    stringResultado = ''
    rutasNoValidas = ""
    for ruta in listaRutas:
        if access(ruta, F_OK):
            stringResultado += '"' + ruta + '" '
        else:
            rutasNoValidas += "\n" + ruta

    if rutasNoValidas != "":
        print("Las siguientes rutas de canciones no existen:" + rutasNoValidas)
    print(stringResultado)
    return stringResultado


def verificarRutaVLC(ruta):
    if not access(ruta[1:-1], F_OK):
        print("El programa VLC no se encuentra en " + ruta[1:-1] + ".")
        exit()
