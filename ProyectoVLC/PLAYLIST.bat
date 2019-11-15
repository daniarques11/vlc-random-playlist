@echo off
cls
IF EXIST "C:\Program Files\VideoLAN\VLC\vlc.exe" (set vlc="C:\Program Files\VideoLAN\VLC\vlc") ELSE (ECHO No encontrado)
IF EXIST "C:\Program Files (x86)\VideoLAN\VLC\vlc.exe" (set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc") ELSE (ECHO No encontrado en x86)
set opcionesvlc=
rem DANI PODEMOS USAR LA SIGUIENTE VARIABLE PARA METER LAS CARPETAS (O UNICA CANCION) QUE SE VA A REPRODUCIR, COMO HE PUESTO EN LA LINEA 77-81
set cancionesParaReproducir=

:menu
echo Selecciona la opcion que desees:
echo.
echo -1: Musica
echo.
echo -2: Video
echo.
echo -3: Webcam
echo.
echo -4: Exit
echo.
set /p opcion=" "
cls
goto :%opcion%

:1
echo Estas con las opciones de audio:
echo.
echo -1: Canciones aleatorias
echo.
echo -2: Escoger una unica cancion
echo.
echo -3: Permitir repeticion
echo. 
echo -4: Reproducir
echo.
set /p opcionm="Elige una opcion: "
cls
goto :m%opcionm%

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


:m1
rem AQUI BASTA PONER UNA OPCION QUE SEA "Quiere reproducir todas las canciones en la carpeta musica, o un genero especifico?" Y METER O BIEN TODA LA CARPETA MUSICA 
rem EN %cancionesParaReproducir% O BIEN LA (O LAS) CARPETAS DE GENERO QUE EL USUARIO ESCOJA
set opcionesvlc=%opcionesvlc%--random
goto :1

:m2
set /p palabraClave="Introduce una palabra clave del nombre de la cancion:"
echo.
set cancionesParaReproducir=*%palabraClave%*.mp3
goto :1


:m3


:m4
%vlc% %cancionesParaReproducir% %opciones%
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
%vlc% %cancionesParaReproducir% %opciones%
exit


:w1
%vlc% dshow://
exit


:w2


:w3
%vlc% dshow:// --video-splitter wall --wall-cols 2 --wall-rows 2
exit


pause
