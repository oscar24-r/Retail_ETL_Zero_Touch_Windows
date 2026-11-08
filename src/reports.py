import json
from datetime import datetime
from .config import OUTPUT,REPORTS
def guardar(clean,rejected,m):
    OUTPUT.mkdir(parents=True,exist_ok=True); REPORTS.mkdir(parents=True,exist_ok=True)
    clean.to_csv(OUTPUT/"ventas_consolidadas.csv",index=False,encoding="utf-8-sig")
    rejected.to_csv(OUTPUT/"ventas_rechazadas.csv",index=False,encoding="utf-8-sig")
    report={**m,"fecha_reporte":datetime.now().isoformat(timespec="seconds"),
            "ventas_totales":round(float(clean.total_venta.sum()),2),
            "ticket_promedio":round(float(clean.total_venta.mean()),2) if len(clean) else 0}
    (REPORTS/"reporte_ejecucion.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
