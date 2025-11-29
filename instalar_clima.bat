@echo off
echo Instalando Clima Global Pro...
echo.

:: Verificar si Python est? instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no est? instalado o no est? en el PATH
    echo Descarga Python desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Instalar dependencias
echo Instalando dependencias...
pip install flet requests

:: Crear carpeta de la aplicaci?n
if not exist "ClimaGlobalPro" mkdir ClimaGlobalPro

:: Copiar archivos
copy app_clima_decorado.py ClimaGlobalPro\
copy requirements.txt ClimaGlobalPro\

echo.
echo ? Instalaci?n completada!
echo.
echo Para ejecutar la aplicaci?n:
echo cd ClimaGlobalPro
echo python app_clima_decorado.py
echo.
pause
