@echo off
echo Creando estructura de carpetas del proyecto...

REM Carpeta principal opcional (si quieres que se cree dentro de ella)
REM mkdir cobol-python-kitchen-system
REM cd cobol-python-kitchen-system

mkdir backend
mkdir backend\api
mkdir backend\cobol
mkdir backend\python_services

mkdir data

mkdir mobile_app
mkdir tablet_app

mkdir docs

echo.
echo Carpetas creadas correctamente.
pause
