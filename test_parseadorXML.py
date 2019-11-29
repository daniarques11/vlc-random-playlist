from parseadorXML import getDiccionarioRutas as getDic
import pytest


def test_fileNotFoundXML():
    assert pytest.raises(FileNotFoundError, getDic("libraryPP.xml"))