import random
from checkOutput import *
from checkOutput import checkListaOutput as checkOutput


def getCancionesRandom(cancionesDict):
    # Assert para comprobar si la entrada es un diccionario
    assert isinstance(cancionesDict, dict) is True

    listaCanciones = getListaAPartirDeKeys(cancionesDict)
    listaDesordenada = desordenarLista(listaCanciones)
    # Comprobar que listaDesordenada es realmente
    # una lista desordenada de listaCanciones
    assert checkOutput(listaDesordenada, listaCanciones) is True
    return listaDesordenada


def getListaAPartirDeKeys(diccionario):
    lista = []
    for key in diccionario:
        lista.append(key)
    return lista


def desordenarLista(lista):
    listaCopia = lista[:]
    assert listaCopia is not lista
    listaDesordenada = []
    while listaCopia != []:
        numeroRandom = random.randint(0, len(listaCopia) - 1)
        # Quitar un elemento de lista y meterlo al final de listaDesordenada
        elementoRandom = listaCopia.pop(numeroRandom)
        listaDesordenada.append(elementoRandom)
    return listaDesordenada
