from invocarVLC import *
from accesoXML import *
from logica import *


def main():
    vlcRuta = '"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"'
    libreria = "libraryDefinitivo.xml"
    diccionarioRutas = getDiccionarioRutas(libreria)
    listaRandom = getCancionesRandom(diccionarioRutas)
    ejecutarVLC(vlcRuta, listaRandom)


main()
