import barricadas

# Check que pase todas las funciones


def test_barricadaListasCorrectas():
    assert barricadas.checkListaOutput([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) is True


def test_barricadaListasIncorrectas():
    assert barricadas.checkListaOutput([1, 2, 3, 4, 5], [6, 9, 2, 1]) is False


# Check que pase solo la funcion de longitud
def test_mismaLongitudListas():
    assert barricadas.checkLongitudEsIgual(
        [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) is True


def test_diferenteLongitudListas():
    assert barricadas.checkLongitudEsIgual(
        [1, 2, 3, 4], [1, 2, 3, 4, 5]) is False


# Check que pase solo la funcion de repetición
def test_countCancionesOutputEsIgualInput():
    assert barricadas.checkCountCanciones(
        [1, 2, 3, 4, 4], [4, 2, 1, 3, 4]) is True


def test_countCancionesOutputEsDiferenteInput():
    assert barricadas.checkCountCanciones(
        [1, 2, 3, 4, 4, 4], [5, 4, 3, 1, 2, 4]) is False


# Check que pase solo la funcion de integridad
def test_integridadCorrecto():
    assert barricadas.checkIntegridad(['1', '2', '3', '4', '5'], [
                                      '1', '3', '2', '5', '4']) is True


def test_integridadIncorrecto():
    assert barricadas.checkIntegridad(
        [1, 2, 3, 4, 5], [1, 2, 3, 4, 4]) is False
