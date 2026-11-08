import argparse,time
from .audit import get_logger
from .extract import extraer
from .transform import transformar
from .load import cargar,auditar
from .reports import guardar
def ejecutar():
    log=get_logger(); t=time.perf_counter(); m={}
    try:
        log.info("INICIO ETL RETAIL")
        raw=extraer(); clean,rejected,m=transformar(raw)
        guardar(clean,rejected,m); cargar(clean)
        elapsed=time.perf_counter()-t; auditar(m,"OK",elapsed,"Pipeline completado")
        log.info("OK | %s",m); return 0
    except Exception as e:
        elapsed=time.perf_counter()-t; log.exception("FALLO ETL: %s",e)
        try: auditar(m,"ERROR",elapsed,str(e))
        except Exception: log.exception("No se pudo guardar auditoria")
        return 1
if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--origen",choices=["csv"],default="csv"); p.parse_args()
    raise SystemExit(ejecutar())
