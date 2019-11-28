from servicios import *


vlcRuta = '"C:/Program Files (x86)/VideoLAN/VLC/vlc"'
libreria = "libraryP.xml"
listaRutas = getListaRutasRandom(libreria)
stringRutas = getStringRutas(listaRutas)
ejecutarVLC(vlcRuta, stringRutas)
