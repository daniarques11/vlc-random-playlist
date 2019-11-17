@echo off
cls
echo.
color 4
echo Tu programa VLC esta instalado?
echo.
rem Comprobacion de donde esta instalado el programa vlc
IF EXIST "C:\Program Files\VideoLAN\VLC\vlc.exe" (ECHO VLC esta instalado!) ELSE (ECHO No encontrado VLC)
IF EXIST "C:\Program Files\VideoLAN\VLC\vlc.exe" (set vlc="C:\Program Files\VideoLAN\VLC\vlc") 
echo.
IF EXIST "C:\Program Files (x86)\VideoLAN\VLC\vlc.exe" (ECHO VLC esta instalado!) ELSE (ECHO No encontrado VLC en x86)
IF EXIST "C:\Program Files (x86)\VideoLAN\VLC\vlc.exe" (set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc") 
echo.
rem Si no se establece la variable vlc con la ruta, se ejecuta el instalador
IF DEFINED %vlc% (ECHO VLC no esta instalado, continua para instalarlo)
pause > nul
cls
IF DEFINED %vlc% (vlcInstall.exe)
pause
set opcionesvlc=
rem DANI PODEMOS USAR LA SIGUIENTE VARIABLE PARA METER LAS CARPETAS (O UNICA CANCION) QUE SE VA A REPRODUCIR, COMO HE PUESTO EN LA LINEA 77-81
rem variable pada poner solo una cancion
set cancionUnica=
rem variable para escoger el genero de las playlist random
set generoRandom=
cls

rem Menu principal general
:menu
color f
echo Selecciona la opcion que desees (1,2,3,4):
echo.
echo -1: Musica
echo.
echo -2: Video
echo.
echo -3: Webcam
echo.
echo -x: Exit
echo.
set /p opcion="Elige una opcion: "
cls
goto :%opcion%

rem Menu principal de musica sin opciones seleccionadas
:1
color 3
echo Estas con las opciones de audio:
echo.
echo -1: Canciones aleatorias por genero
echo.
echo -2: Escoger una unica cancion
echo.
echo -3: Permitir repeticion
echo. 
echo -p: Reproducir
echo.
echo -z: Atras
echo.
echo -x: Exit
echo.
set /p opcionm="Elige una opcion: "
cls
goto :m%opcionm%

rem Menu para una vez seleccionada la carpeta de género 
:11
color 1
echo Estas con las opciones de audio:
echo.
echo -1: Canciones aleatorias por genero (Seleccionado: %generoRandom%)
echo.
echo -2: Escoger una unica cancion
echo.
echo -3: Permitir repeticion
echo. 
echo -p: Reproducir
echo.
echo -z: Atras
echo.
echo -x: Exit
echo.
set /p opcionm="Elige una opcion: "
cls
goto :m1%opcionm%

rem Menu para una vez seleccionada la unica cancion
:12
echo Estas con las opciones de audio:
echo.
color 6
echo -1: Canciones aleatorias por genero
echo.
echo -2: Escoger una unica cancion (Seleccionada: %cancionrep%)
echo.
echo -3: Permitir repeticion
echo.
echo -p: Reproducir
echo.
echo -z: Atras
echo.
echo -x: Exit
echo.
set /p opcionm="Elige una opcion: "
cls
goto :m2%opcionm%

rem Menu con repeticion activada
:13
echo Estas con las opciones de audio:
echo.
color 1
echo -1: Canciones aleatorias por genero
echo.
echo -2: Escoger una unica cancion
echo.
echo -3: Permitir repeticion (Seleccionado)
echo.
echo -p: Reproducir
echo.
echo -z: Atras
echo.
echo -x: Exit
echo.
set /p opcionm="Elige una opcion: "
cls
goto :m3%opcionm%

rem Menu con genero y repeticion
:113
echo Estas con las opciones de audio:
echo.
color d
echo -1: Canciones aleatorias por genero (Seleccionado %generoRandom%)
echo.
echo -2: Escoger una unica cancion
echo.
echo -3: Permitir repeticion (Seleccionado)
echo.
echo -p: Reproducir
echo.
echo -z: Atras
echo.
echo -x: Exit
echo.
set /p opcionm="Elige una opcion: "
cls
goto :m13%opcionm%

:123
echo Estas con las opciones de audio:
echo.
color 6
echo -1: Canciones aleatorias por genero
echo.
echo -2: Escoger una unica cancion (Seleccionada: %cancionrep%)
echo.
echo -3: Permitir repeticion (Seleccionado)
echo.
echo -p: Reproducir
echo.
echo -z: Atras
echo.
echo -x: Exit
echo.
set /p opcionm="Elige una opcion: "
cls
goto :m23%opcionm%

:2
echo Estas con las opciones de video:
echo.
echo -1: Pantalla completa
echo.
echo -2: Reproduccion en video-wall
echo.
echo -3: Seleccionar minutos
echo. 
echo -4: Seleccionar subtitulos
echo.
echo -5: Reproducir
echo.
set /p opcionv="Elige una opcion: "
cls
goto :v%opcionv%

:3
echo Estas con las opciones de webcam:
echo.
echo -1: Activar webcam
echo.
echo -2: Visualizacion en video-wall
echo.
echo -3: Exit
echo.
set /p opcionw="Elige una opcion: "
cls
goto :w%opcionw%

:4
exit

rem Menu para seleccionar el genero
:m1
rem AQUI BASTA PONER UNA OPCION QUE SEA "Quiere reproducir todas las canciones en la carpeta musica, o un genero especifico?" Y METER O BIEN TODA LA CARPETA MUSICA 
rem EN %cancionrep% O BIEN LA (O LAS) CARPETAS DE GENERO QUE EL USUARIO ESCOJA
echo Estos son los generos a escoger: 
echo.
echo -a: 80'
echo.
echo -b: 90'
echo.
echo -c: Alternative
echo. 
echo -d: Heavy Metal
echo.
echo -e: Hip hop
echo.
echo -f: Indie
echo.
echo -g: Others
echo.
echo -h: Pop
echo. 
echo -i: Punk
echo.
echo -j: Reggae
echo.
echo -k: Reggaeton
echo.
echo -l: Rock
echo.
echo -x: Volver atras
echo.
set /p oprandom="Escoge un genero para la reproduccion aleatoria: "
set opcionesvlc=--random 
cls
goto :1%oprandom%

rem Menu para seleccionar una unica cancion
:m2
set /p palabraClave="Introduce una palabra clave del nombre de la cancion (solo para .mp3):"
echo.
set cancionrep=*%palabraClave%*.mp3
cls
goto :12

rem Redireccion al menu de repetion
:m3
echo Repeticion activada
pause > nul
set opcionesvlc=%opcionesvlc%--loop
cls
goto :13

rem Redireccion al menu de nusica por no haber seleccionado nada
:mp
echo No has seleccionado nada para reproducir
pause > nul
cls
goto :1

rem Redireccion al menu general
:mz
cls
goto :menu

rem Redireccion a la salida
:mz
exit

rem Redireccion al selector de generos
:m11
cls
goto :m1

rem Redireccion al selector musica
:m12
cls
goto :12

rem Redireccion al menu con genero y repeticion activada
:m13
echo Repeticion activada
pause > nul
set opcionesvlc=%opcionesvlc%--loop
cls
goto :113

rem Ejecutar el vlc con la carpeta del genero y random
:m1p
%vlc% "./Musica/%generoRandom%" %opcionesvlc%
exit

rem Redireccion al menu general
:m1z
cls
goto :menu

rem Redireccion a la salida
:m1x
exit


rem Redireccion al menu para seleccionar el genero
:m21
cls
goto :m1

rem Menu para seleccionar una unica cancion
:m22
cls
goto :m2

rem Menu para seleccionar una unica cancion
:m23
echo Repeticion activada
pause > nul
set opcionesvlc=%opcionesvlc%--loop
goto :123

rem Ejecutar vlc
:m2p
%vlc% "./Musica/%/%cancionrep%" %opcionesvlc%
exit

rem Redireccion al menu general
:m2z
cls
goto :menu

rem Redireccion a la salida
:m2x
exit


rem Redireccion al menu para seleccionar el genero
:m31
cls
goto :m1

rem Menu para seleccionar una unica cancion
:m32
cls
goto :m2

rem Menu para seleccionar una unica cancion
:m33
echo Repeticion activada
pause > nul
set opcionesvlc=%opcionesvlc%--loop
cls
goto :123

rem Ejecutar vlc
:m3p
%vlc% "./Musica/%/%cancionrep%" %opcionesvlc%
exit

rem Redireccion al menu general
:m3z
cls
goto :menu

rem Redireccion a la salida
:m13x
exit

rem Redireccion al menu para seleccionar el genero
:m31
cls
goto :m1

rem Menu para seleccionar una unica cancion
:m32
cls
goto :m2

rem Menu para seleccionar una unica cancion
:m33
echo Repeticion activada
pause > nul
set opcionesvlc=%opcionesvlc%--loop
cls
goto :123

rem Ejecutar vlc
:m3p
%vlc% "./Musica/%/%cancionrep%" %opcionesvlc%
exit

rem Redireccion al menu general
:m3z
cls
goto :menu

rem Redireccion a la salida
:m3x
exit



rem Redireccion al menu para seleccionar el genero
:m13
cls
goto :m1

rem Menu para seleccionar una unica cancion
:m32
cls
goto :m2

rem Menu para seleccionar una unica cancion
:m33
echo Repeticion activada
pause > nul
set opcionesvlc=%opcionesvlc%--loop
cls
goto :123

rem Ejecutar vlc
:m3p
%vlc% "./Musica/%/%cancionrep%" %opcionesvlc%
exit

rem Redireccion al menu general
:m3z
cls
goto :menu

rem Redireccion a la salida
:m3x
exit


rem Redireccion al menu para seleccionar el genero
:m31
cls
goto :m1

rem Menu para seleccionar una unica cancion
:m32
cls
goto :m2

rem Menu para seleccionar una unica cancion
:m33
echo Repeticion activada
pause > nul
set opcionesvlc=%opcionesvlc%--loop
cls
goto :123

rem Ejecutar vlc
:m3p
%vlc% "./Musica/%/%cancionrep%" %opcionesvlc%
exit

rem Redireccion al menu general
:m3z
cls
goto :menu

rem Redireccion a la salida
:m3x
exit


:v1
set opcionesvlc=-f %opcionesvlc%
goto :2

:v2
echo Video-wall:
set /p numColumnas="Selecciona el número de columnas y pulsa enter:"
cls
set /p numFilas="Numero de filas:"
cls
set /p agree="Has seleccionado %columnas% columnas y %filas% filas. Es correcto? (y/n):"
cls
goto :%agree%

:y
set opcionesvlc=%opcionesvlc%--video-splitter wall --wall-cols %columnas% --wall-rows %filas%
goto :2

:n
goto :v2

:v3


:v4


:v5
%vlc% %videorep% %opcionesvideo%
exit

rem Opciones de webcam
:w1
%vlc% dshow://
exit


:w2


:w3
%vlc% dshow:// --video-splitter wall --wall-cols 2 --wall-rows 2
exit

 rem redirecciones por genero para asignar la variable por opcion, y sin comillas porque la direccion de ruta ya lleva al inicio y final
:1a
set generoRandom=80'
cls
goto :11

:1b
set generoRandom=90'
cls
goto :11

:1c
set generoRandom=Alternative
cls
goto :11

:1d
set generoRandom=Heavy Metal
cls
goto :11

:1e
set generoRandom=Hip Hop
cls
goto :11

:1f
set generoRandom=Indie
cls
goto :11

:1g
set generoRandom=Others
cls
goto :11

:1h
set generoRandom=Pop
cls
goto :11

:1i
set generoRandom=Punk
cls
goto :11

:1j
set generoRandom=Reggae
cls
goto :11

:1k
set generoRandom=Reggaeton
cls
goto :11

:1l
set generoRandom=Rock
cls
goto :11


:1x
cls
goto :1

pause
