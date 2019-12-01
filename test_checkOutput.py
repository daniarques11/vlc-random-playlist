from checkOutput import *

# Check que pase todas las funciones


def test_barricadaListasCorrectas():
    assert checkListaOutput([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) is True


def test_barricadaListasIncorrectas():
    assert checkListaOutput([1, 2, 3, 4, 5], [6, 9, 2, 1]) is False


# Check que pase solo la funcion de longitud
def test_mismaLongitudListas():
    assert checkLongitudEsIgual(
        [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) is True


def test_diferenteLongitudListas():
    assert checkLongitudEsIgual(
        [1, 2, 3, 4], [1, 2, 3, 4, 5]) is False


# Check que pase solo la funcion de repetición
def test_countCancionesOutputEsIgualInput():
    assert checkCountCanciones(
        [1, 2, 3, 4, 4], [4, 2, 1, 3, 4]) is True


def test_countCancionesOutputEsDiferenteInput():
    assert checkCountCanciones(
        [1, 2, 3, 4, 4, 4], [5, 4, 3, 1, 2, 4]) is False


# Check que pase solo la funcion de integridad
def test_integridadCorrecto():
    assert checkIntegridad(['1', '2', '3', '4', '5'], [
                                      '1', '3', '2', '5', '4']) is True


def test_integridadIncorrecto():
    assert checkIntegridad(
        [1, 2, 3, 4, 5], [1, 2, 3, 4, 4]) is False
