# Guía de clase — paso a paso

1. Presentar el caso: ventas retail llegan en CSV; hay datos erróneos y deben actualizarse cada noche.
2. Comparar `ventas_retail.csv` con `ventas_retail_con_errores.csv`.
3. Preparar entorno con `uv sync --extra dev`; explicar que uv instala dependencias, no ejecuta ETL.
4. Leer módulos: extract → transform → load → reports → audit; `pipeline_maestro.py` coordina.
5. Ejecutar `uv run python -m src.pipeline_maestro --origen csv`.
6. Inspeccionar CSV limpio/rechazado, JSON, logs y SQLite.
7. Ejecutar `uv run pytest -v`; explicar cada prueba.
8. Editar ruta absoluta de `ejecutar_etl.bat`; probar desde CMD.
9. Abrir `taskschd.msc`; crear tarea, definir cuenta, trigger diario, acción BAT y directorio “Iniciar en”.
10. Ejecutar la tarea manualmente desde Task Scheduler y verificar evidencia en logs, SQLite y marcas de tiempo.

## Preguntas
- ¿En qué se diferencian programar y orquestar?
- ¿Por qué usar rutas absolutas?
- ¿Qué significa headless?
- ¿Qué demuestra que una ejecución programada terminó correctamente?
- ¿Por qué Power BI se actualiza después de validar la salida ETL?

## Entregable
Proyecto, captura de tarea programada, evidencia de ejecución, logs, CSV limpio/rechazado, reporte JSON y SQLite.
