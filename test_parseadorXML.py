from parseadorXML import getDiccionarioRutas as getdic


def test_correctoXML():
    assert getdic("libraryPP.xml") == exit()