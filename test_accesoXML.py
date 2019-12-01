from accesoXML import getDiccionarioRutas


def test_diccionarioDevueltoCorrectamente():
    assert getDiccionarioRutas("libraryP.xml") == {'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\A veure que en fem.mp3': '190029', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Adgasuodfhoiegoewgouegoegb.mp3': '431202', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Zero.mp4': '11255567', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\No dudaria.mp4': '938421'}