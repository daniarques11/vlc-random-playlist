import xml.etree.ElementTree as ET
import types


def parsear(library):
    try:
        tree = ET.parse(library)
    except FileNotFoundError:
        print("No se ha encontrado el archivo " + library +
              ", comprueba que la ruta del archivo coincide con la ruta de la variable libreria en main.py")
        exit()
    except:
        print("La variable libreria en main.py no es un archivo XML")
        exit()
    else:
        root = tree.getroot()
        tracksDic = {}

        for library in root.iter("library"):
            for tracks in library:
                for track in tracks.findall("track"):
                    tracksDic[track.attrib['ruta']] = track.attrib['id']
        return tracksDic
