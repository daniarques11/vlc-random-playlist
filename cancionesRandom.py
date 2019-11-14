import random
import barricadas


def cancionesRandom(diccionarioCanciones):
    try:
        assert isinstance(diccionarioCanciones, dict) == True
        #Assert para comprobar si la entrada es un diccionario
    except AssertionError:
        return "La entrada no es un diccionario"
    else:
        listaCanciones = getListaCanciones(diccionarioCanciones)
        listaDesordenada = desordenarCanciones(listaCanciones)
        if barricadas.barricada(listaDesordenada, listaCanciones) == True:
            return listaDesordenada
        else:
            return "Algo ha ido mal"


def getListaCanciones(diccionarioCanciones):
    listaCanciones = []
    for key in diccionarioCanciones:
        listaCanciones.append(key)
    return listaCanciones


def desordenarCanciones(listaCanciones):
    listaCopia = listaCanciones[:]
    assert listaCopia is not listaCanciones
    listaDesordenada = []
    while listaCopia != []:
        numeroRandom = random.randint(0, len(listaCopia) - 1)
        # quitar un elemento de lista y meterlo al final de listaDesordenada
        listaDesordenada.append(listaCopia.pop(numeroRandom))
    return listaDesordenada


print(cancionesRandom({'13472392':
                       {'name': 'A veure que', 'band': 'Joan Manuel Serrat',
                           'album': '100 mejores canciones', 'ruta': 'C:\\efef'},
                       '21846173':
                       {'name': 'Cold as Ice', 'band': 'Foreigner',
                           'album': 'Foreigner', 'ruta': 'C:\\eqriq2r812ru2'},
                       '237461794':
                       {'name': 'Zero', 'band': 'Imagine Dragons',
                        'album': 'Zero', 'ruta': 'C:\\eqr463563634'},
                       '536351351':
                       {'name': 'No dudaria', 'band': 'Antonio Flores',
                        'album': 'Antonio', 'ruta': 'C:uahweufb3e'}
                       }))
