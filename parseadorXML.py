<<<<<<< HEAD
=======
import xml.etree.ElementTree as ET


def parser(library):
    tree = ET.parse(library)
    root = tree.getroot()
    tracksDic= {}

    for library in root.iter("library"):
        for tracks in library:
            for track in tracks.findall("track"):
                tracksDic[track.attrib['ruta']] = track.attrib['id']
    return tracksDic
>>>>>>> f9fe5bec4b589332e443a9e8175e6d038c3d0d76
