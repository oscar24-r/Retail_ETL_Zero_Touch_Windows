@echo off
setlocal
REM CAMBIAR esta ruta por la ruta absoluta real del proyecto
set "PROJECT_DIR=C:\ESPECIALIZACION PYTHON\17. Sesion 17\SESION 17\Retail_ETL_Zero_Touch_Windows"
REM CAMBIAR AL DIRECTORIO DEL PROYECTO
cd /d "%PROJECT_DIR%"
if errorlevel 1 exit /b 10
REM Crear carpeta de logs si no existe
if not exist "logs" mkdir "logs"
echo ===== Inicio %date% %time% ===== >> logs\scheduler.log
REM Ejecutar el script de Python - Pipeline ETL
uv run python -m src.pipeline_maestro --origen csv >> logs\scheduler.log 2>&1
REM Capturar el código de salida del script de Python
set "RC=%ERRORLEVEL%"
echo Fin %DATE% %TIME% - Resultado: %RC% >> "logs\scheduler.log"
exit /b %RC%
