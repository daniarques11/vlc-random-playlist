from invocarVLC import *


def test_getStringRutasCancionesCorrectas():
    assert getStringRutas(['C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\A veure que en fem.mp3', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\No dudaria.mp4', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Zero.mp4', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Cold as Ice.mp3']) == '"C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\A veure que en fem.mp3" "C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\No dudaria.mp4" "C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Zero.mp4" "C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Cold as Ice.mp3" '

def test_getStringRutasCancionesUnaIncorrecta():
    assert getStringRutas(['C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\A veure que en fem.mp3', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\No dudaria.mp4', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Zero.mp4', 'C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Adgasuodfhoiegoewgouegoegb.mp3']) =='"C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\A veure que en fem.mp3" "C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\No dudaria.mp4" "C:\\Users\\Thelpher\\Desktop\\DAW 1r\\VLC Projecte\\Musica\\Zero.mp4" '
    