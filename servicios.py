from parseadorXML import getDiccionarioRutas
from cancionesRandom import getCancionesRandom
import os

# Obtener diccionario con rutas como keys, e id como valores
# para luego devolver lista con rutas random


def ejecutarVLC(vlcRuta, listaCanciones):
    stringRutas = getStringRutas(listaCanciones)
    comandoCMD = vlcRuta + " " + stringRutas + "--play-and-exit"
    os.popen(comandoCMD)


def getStringRutas(listaRutas):
    stringResultado = ''
    rutasNoValidas = ""
    for ruta in listaRutas:
        if os.access(ruta, os.F_OK):
            stringResultado = stringResultado + '"' + ruta + '" '
        else:
            rutasNoValidas += ruta + " "

    if rutasNoValidas != "":
        print("Las rutas: " + rutasNoValidas + "no existe en el directorio")
    return stringResultado


def verificarVLC(vlcRuta):
    try:
        assert (os.access(vlcRuta, os.F_OK)) is True
    except:
        print("El programa VLC no se encuentra en esta ruta")
        exit()

