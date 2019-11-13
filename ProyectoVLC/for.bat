@echo off

for /F "TOKENS=1 DELIMS=." %%I in ('dir') DO ECHO %%I
pause