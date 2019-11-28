from parseadorXML import parsear
from cancionesRandom import cancionesRandom
import os

# Obtener diccionario con rutas como keys, e id como valores
# para luego devolver lista con rutas random

def getStringRutas(lista):
    stringResultado = ''
    for elemento in lista:
        stringResultado = stringResultado + '"' + elemento + '" '
    return stringResultado


def ejecutarVLC(vlcRuta, stringRutas):
    comandoCMD = vlcRuta + " " + stringRutas + "--play-and-exit"
    os.popen(comandoCMD)
