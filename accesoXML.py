import xml.etree.ElementTree as ET


def getDiccionarioRutas(libreriaXML):
    try:
        tree = ET.parse(libreriaXML)
    except FileNotFoundError:
        print("No se ha encontrado el archivo " + libreriaXML +
              ", comprueba que la ruta del archivo coincide con la ruta de la variable libreria en main.py")
        exit()
    except:
        print("La variable libreria en main.py no es un archivo XML (como cadena de caracteres)")
        exit()
    else:
        root = tree.getroot()
        cancionesDict = {}

        for libreriaXML in root.iter("library"):
            for tracks in libreriaXML:
                for track in tracks.findall("track"):
                    cancionesDict[track.attrib['ruta']] = track.attrib['id']
        print(cancionesDict)
        return cancionesDict
