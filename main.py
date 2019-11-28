from servicios import *
from parseadorXML import *
from cancionesRandom import *


def main():
    vlcRuta = '"C:/Program Files (x86)/VideoLAN/VLC/vlc"'
    libreria = "libraryP.xml"
    diccionarioRutas = parsear(libreria)
    listaRandom = cancionesRandom(diccionarioRutas)
    stringRutas = getStringRutas(listaRandom)
    ejecutarVLC(vlcRuta, stringRutas)


main()
