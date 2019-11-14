import barricadas

#Check que pase todas las funciones
def test_correctLists():
    assert barricadas.barricada([1,2,3,4,5], [5,4,3,2,1]) is True


def test_incorrectLists():
    assert barricadas.barricada([1,2,3,4,5], [6,9,2,1]) is False


#Check que pase solo la funcion de longitud
def test_correctLenList():
    assert barricadas.checkLongitudEsIgual([1,2,3,4,5], [1,2,3,4,5]) is True


def test_incorrectLenList():
    assert barricadas.checkLongitudEsIgual([1,2,3,4], [1,2,3,4,5]) is False


#Check que pase solo la funcion de repetición
def test_correctRepInt():
    assert barricadas.checkRepeticion([1,2,3,4,4], [1,2,3,4,4]) is True


def test_incorrectRepInt():
    assert barricadas.checkRepeticion([1,2,3,4,4,4], [1,2,3,4,4,5]) is False


#Check que pase solo la funcion de integridad
def test_correctIntegInt():
    assert barricadas.checkIntegridad([1,2,3,4,5],[1,2,3,4,5]) is True


def test_incorrectIntegInt():
    assert barricadas.checkIntegridad([1,2,3,4,5], [1,2,3,4,4]) is False