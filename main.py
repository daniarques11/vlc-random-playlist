from parseadorXML import parser
from cancionesRandom import cancionesRandom

def api():
    dicioRutas = parser("libraryP.xml")
    print(cancionesRandom(dicioRutas))

api()