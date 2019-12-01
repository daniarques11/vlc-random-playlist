from accesoXML import getDiccionarioRutas


def test_diccionarioContieneMenosDe25Canciones():
    assert getDiccionarioRutas("libraryP.xml") == {'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\A veure que en fem.mp3': '190029', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Cold as Ice.mp3': '431202', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Zero.mp4': '11255567', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\No dudaria.mp4': '938421'}

def test_diccionarioContieneCancionesMinimas():
    assert getDiccionarioRutas("libraryDefinitivo.xml") == {'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\A veure que en fem.mp3': '190029', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Cold as Ice.mp3': '431202', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Zero.mp4': '11255567', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\No dudaria.mp4': '938421', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Alegria.mp3': '56246672', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Extraterrestres.mp3': '56246696', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Bliss.mp3': '1444567172', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Plug in Baby.mp3': '1444567175', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Hysteria.mp3': '1444567078', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Time Is Running Out.mp3': '1444567073', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Uprising.mp3': '1444567211', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\United States of Eurasia.mp3': '1444567214', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Guiding Light.mp3': '1444567215', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Unnatural Selection.mp3': '1444567216', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\I Belong to You.mp3': '1444567218', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Supermassive Black Hole.mp3': '14445672113', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Starlight.mp3': '14445672112', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Knights Of Cydonia.mp3': '144456721111', "C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Don't Stop Me Now.mp3": '224566771012', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Bohemian Rhapsody.mp3': '26788909011', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\My Way.mp3': '16486', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\New York, New York.mp3': '1794125', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Benvolgut.mp3': '189921', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Camins.mp3': '8423212', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Keine Lust.mp3': '563211334', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Baby Jane.mp3': '78455342', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\American Idiot.mp3': '654642341', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Holidays.mp3': '654642343', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Boulevard of Broken Dreams.mp3': '654642344', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Wake me up when September ends.mp3': '654642351', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\21 Guns.mp3': '654642326', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Know Your Enemy.mp3': '654642313'}