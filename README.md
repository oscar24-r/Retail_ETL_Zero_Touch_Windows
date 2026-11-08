# Retail ETL Zero-Touch — Sesión 17

Proyecto didáctico que continúa la arquitectura ETL de la Sesión 16. Incluye dataset sintético retail (150 filas), versión con errores, Python/Pandas, SQLite, logs, reportes, pruebas y lanzador Windows.

> No se ha proporcionado aquí el CSV/código original de la Sesión 16. Los datos incluidos son demostrativos y se pueden reemplazar conservando las columnas requeridas.

## 1. Requisitos
Windows 10/11, Python >=3.10 y uv.
Instala uv en PowerShell:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Cierra y abre la terminal; verifica `uv --version`.

## 2. Preparar entorno
En PowerShell, desde la carpeta que contiene `pyproject.toml`:
```powershell
uv sync --extra dev
uv run pytest -v
```
Se esperan 5 pruebas aprobadas.

## 3. Ejecutar manualmente
```powershell
uv run python -m src.pipeline_maestro --origen csv
```
El proceso lee el CSV con errores, valida, rechaza registros inválidos, elimina duplicados, recalcula total, guarda SQLite y genera salidas.

## 4. Verificar resultados
- `data/output/ventas_consolidadas.csv`
- `data/output/ventas_rechazadas.csv`
- `data/retail.db` (tablas `ventas_consolidadas`, `ejecuciones`; vista `resumen_region`)
- `reports/reporte_ejecucion.json`
- `logs/pipeline.log`

Abrir la base con DB Browser for SQLite y ejecutar `sql/consultas.sql`.

## 5. Configurar el BAT
Editar `ejecutar_etl.bat`. Cambiar `C:\ETL\Retail_ETL_Zero_Touch_Windows` por la ruta absoluta real. Verificar que `uv` está disponible en PATH para la cuenta que ejecutará la tarea. Probar desde CMD:
```cmd
ejecutar_etl.bat
```
El BAT devuelve el código de salida del pipeline; 0=éxito, 1=fallo ETL, 10=no se pudo entrar a la carpeta.

## 6. Programar en Windows
1. `Win + R` → `taskschd.msc`.
2. Elegir **Crear tarea**.
3. General: nombre `Retail ETL Zero-Touch`; usar cuenta con permisos.
4. Desencadenadores → Nuevo → Diario → 23:00 (hora de ejemplo).
5. Acciones → Nueva → Iniciar un programa. Programa: ruta completa al `.bat`. “Iniciar en”: carpeta raíz del proyecto.
6. Configurar condiciones de energía/red según corresponda.
7. Configuración: permitir ejecución bajo demanda; si ya se está ejecutando, no iniciar otra instancia.
8. Guardar; Windows podría solicitar credenciales.
9. Clic derecho sobre tarea → Ejecutar.
10. Verificar Último resultado, `logs/scheduler.log`, `logs/pipeline.log`, hora de modificación de salidas y nuevo registro en `ejecuciones`.

## 7. Prueba de fallo controlado
Renombrar temporalmente el CSV de entrada, ejecutar tarea y revisar el log/código de salida. Restaurar el nombre y ejecutar de nuevo.

## 8. Power BI
Conectar Power BI Desktop al CSV limpio o SQLite. En la práctica, actualizar manualmente después del ETL. Para actualización desatendida de un modelo publicado se requiere Power BI Service, credenciales, gateway si aplica y permisos/licencia/capacidad; configurar refresh programado o API. No asumir que abrir un PBIX desde Task Scheduler produce un refresh headless fiable.

## Seguridad
Usar rutas absolutas, permisos mínimos, no guardar contraseñas en BAT/repositorio, evitar instancias simultáneas y establecer retención/backups/alertas antes de producción.
