from parseadorXML import parser
from cancionesRandom import cancionesRandom
import os


def getListaRutasRandom():
    dicioRutas = parser("libraryP.xml")
    listaRandom = cancionesRandom(dicioRutas)
    return listaRandom


def convertirListaAString(lista):
    return " ".join(str(elemento) for elemento in lista)


print(convertirListaAString(getListaRutasRandom()))
