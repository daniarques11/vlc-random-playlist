from parseadorXML import getDiccionarioRutas
from cancionesRandom import getCancionesRandom
from os import access, F_OK, popen

# Obtener diccionario con rutas como keys, e id como valores
# para luego devolver lista con rutas random


def ejecutarVLC(vlcRuta, listaCanciones):
    verificarVLC(vlcRuta)
    stringRutas = getStringRutas(listaCanciones)
    comandoCMD = vlcRuta + " " + stringRutas + "--play-and-exit"
    popen(comandoCMD)


def getStringRutas(listaRutas):
    stringResultado = ''
    rutasNoValidas = ""
    for ruta in listaRutas:
        if access(ruta, F_OK):
            stringResultado = stringResultado + '"' + ruta + '" '
        else:
            rutasNoValidas += ruta + " "

    if rutasNoValidas != "":
        print("Las rutas: " + rutasNoValidas + "no existe en el directorio")
    return stringResultado


def verificarVLC(ruta):
    if not access(ruta[1:-1], F_OK):
        print("El programa VLC no se encuentra en esta ruta")
        exit()
