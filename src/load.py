import sqlite3
from .config import DB_PATH
def cargar(df):
    DB_PATH.parent.mkdir(parents=True,exist_ok=True)
    with sqlite3.connect(DB_PATH) as c:
        df.to_sql("ventas_consolidadas",c,if_exists="replace",index=False)
        c.execute("""CREATE TABLE IF NOT EXISTS ejecuciones(id INTEGER PRIMARY KEY, fecha TEXT, estado TEXT,
        entrada INTEGER, validos INTEGER, rechazados INTEGER, duplicados INTEGER, duracion REAL, mensaje TEXT)""")
        c.execute("""CREATE VIEW IF NOT EXISTS resumen_region AS SELECT region,COUNT(*) operaciones,
        SUM(total_venta) ventas FROM ventas_consolidadas GROUP BY region""")
        c.commit()
def auditar(m,estado,duracion,mensaje):
    from datetime import datetime
    with sqlite3.connect(DB_PATH) as c:
        c.execute("INSERT INTO ejecuciones(fecha,estado,entrada,validos,rechazados,duplicados,duracion,mensaje) VALUES(?,?,?,?,?,?,?,?)",
        (datetime.now().isoformat(timespec="seconds"),estado,m.get("registros_entrada",0),m.get("registros_validos",0),
         m.get("registros_rechazados",0),m.get("duplicados_id",0),round(duracion,2),mensaje)); c.commit()
