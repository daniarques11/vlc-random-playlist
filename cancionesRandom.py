import random


def cancionesRandom(diccionarioCanciones):
    try:
        assert isinstance(diccionarioCanciones, dict) == True

    except AssertionError:
        return "La entrada no es un diccionario"
    else:
        listaCanciones = getListaCanciones(diccionarioCanciones)
#        desordenarCanciones(dictNumerado)
        return listaCanciones


def getListaCanciones(diccionarioCanciones):
    listaCanciones = []
    for key in diccionarioCanciones:
        listaCanciones.append(key)
    return listaCanciones


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
