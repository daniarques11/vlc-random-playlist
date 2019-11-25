from parseadorXML import parser
from cancionesRandom import cancionesRandom
import os
import subprocess


def getListaRutasRandom(libreria):
    dicioRutas = parser(libreria)
    listaRandom = cancionesRandom(dicioRutas)
    return listaRandom


def convertirRutasAString(lista):
    stringResultado = ''
    for elemento in lista:
        stringResultado = stringResultado + '"' + elemento + '" ' 
    return stringResultado


def ejecutarVLC(vlcRuta, stringRutas):
    ejecutable = vlcRuta + " " + stringRutas + "--play-and-exit"
    print(ejecutable)
    os.popen(ejecutable)


vlcRuta = '"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc"'
libreria = "libraryP.xml"
listaRutas = getListaRutasRandom(libreria)
stringRutas = convertirRutasAString(listaRutas)
ejecutarVLC(vlcRuta, stringRutas)
