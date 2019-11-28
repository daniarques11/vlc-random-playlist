import random
import barricadas
from barricadas import checkListaOutput as Check


def cancionesRandom(cancionesDict):
    assert isinstance(cancionesDict, dict) is True
    # Assert para comprobar si la entrada es un diccionario

    listaCanciones = getListaDeDictKeys(cancionesDict)
    listaDesordenada = desordenarLista(listaCanciones)
    # Comprobar que listaDesordenada es realmente
    # una lista desordenada de listaCanciones
    assert Check(listaDesordenada, listaCanciones) is True
    return listaDesordenada


def getListaDeDictKeys(diccionario):
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
        # quitar un elemento de lista y meterlo al final de listaDesordenada
        listaDesordenada.append(listaCopia.pop(numeroRandom))
    return listaDesordenada
