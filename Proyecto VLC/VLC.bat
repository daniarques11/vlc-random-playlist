@echo off
echo.
echo Esta estructura de carpetas se creara en el directorio en el que se encuentra este archivo .bat
echo.
set /p agree="Estas seguro de que quieres continuar? (y/n) "
goto :%agree%

:y
cls
echo.
md .\Musica .\Videos 
md .\Musica\Pop .\Musica\Rock .\Musica\"Hip Hop" .\Musica\Indie .\Musica\Pop .\Musica\"80's" .\Musica\"90's" .\Musica\"Heavy Metal" .\Musica\Punk .\Musica\Reggaeton .\Musica\Reggae .\Musica\Alternative .\Musica\Others
md .\Videos\Clips .\Videos\Cortos .\Videos\Medios .\Videos\Largos .\Videos\Peliculas .\Videos\Youtube
cls
echo.
echo Carpetas creadas satisfactoriamente
echo.
tree /a .
echo.
pause
cls
echo.
echo Introduce tus canciones en las diferentes carpetas creadas por generos.
echo.
pause
cls
echo.
echo Presiona cualquier tecla para continuar con el siguiente script
echo.
pause > nul
cls
.\PLAYLIST.bat

:n
exit
