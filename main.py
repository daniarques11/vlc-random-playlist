from servicios import *
from parseadorXML import *
from cancionesRandom import *


def main():
    vlcRuta = '"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"'
    libreria = "libraryP.xml"
    diccionarioRutas = getDiccionarioRutas(libreria)
    listaRandom = getCancionesRandom(diccionarioRutas)
    print(listaRandom)
    ejecutarVLC(vlcRuta, listaRandom)


main()
