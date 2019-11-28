from parseadorXML import parsear
from cancionesRandom import cancionesRandom
import os

# Obtener diccionario con rutas como keys, e id como valores
# para luego devolver lista con rutas random


def ejecutarVLC(vlcRuta, listaCanciones):
    stringRutas = getStringRutas(listaCanciones)
    comandoCMD = vlcRuta + " " + stringRutas + "--play-and-exit"
    os.popen(comandoCMD)


def getStringRutas(lista):
    stringResultado = ''
    for elemento in lista:
        stringResultado = stringResultado + '"' + elemento + '" '
    return stringResultado
