import random
import barricadas


def cancionesRandom(diccionarioCanciones):
    try:
        assert isinstance(diccionarioCanciones, dict) is True
        # Assert para comprobar si la entrada es un diccionario
    except AssertionError:
        return "La entrada no es un diccionario"
    else:
        listaCanciones = getListaDeDictKeys(diccionarioCanciones)
        listaDesordenada = desordenarLista(listaCanciones)
        # Comprobar que listaDesordenada es realmente
        # una lista desordenada de listaCanciones
        assert barricadas.barricada(listaDesordenada, listaCanciones) is True
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
