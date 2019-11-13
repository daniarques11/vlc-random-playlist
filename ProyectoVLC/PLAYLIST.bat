@echo off
cls
IF EXIST "C:\Program Files\VideoLAN\VLC\vlc.exe" (set comandovlc="C:\Program Files\VideoLAN\VLC\vlc") ELSE (ECHO No encontrado)
IF EXIST "C:\Program Files (x86)\VideoLAN\VLC\vlc.exe" (set comandovlc="C:\Program Files (x86)\VideoLAN\VLC\vlc") ELSE (ECHO No encontrado en x86)
echo %rutavlc%

:menu
echo.
echo -1: Musica
echo.
echo -2: Video
echo.
echo -3: Webcam
echo.
echo -4: Exit
echo.
set /p opcion="Elige una opcion: "
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
echo -4: Volver al menu
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
echo -5: Volver al menu
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
echo -3: Volver al menu
echo.
set /p opcionw="Elige una opcion: "
cls
goto :w%opcionw%

:4
exit


:m1
%comandovlc% .\Musica --random
goto :1

:m2


:m3


:m4
goto :menu


:v1


:v2


:v3


:v4


:v5
goto :menu


:w1


:w2


:w3
goto :menu



pause
