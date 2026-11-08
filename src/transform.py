import pandas as pd
REQUIRED=["venta_id","fecha","cliente_id","producto_id","producto","cantidad","precio_unitario","total_venta","canal","region"]
def transformar(df):
    missing=[c for c in REQUIRED if c not in df.columns]
    if missing: raise ValueError(f"Faltan columnas: {missing}")
    entrada=len(df); x=df.copy()
    x["fecha"]=pd.to_datetime(x["fecha"],errors="coerce")
    for c in ["cantidad","precio_unitario","total_venta"]: x[c]=pd.to_numeric(x[c],errors="coerce")
    for c in ["producto","venta_id"]: x[c]=x[c].astype("string").str.strip()
    ok=(x.fecha.notna() & x.venta_id.notna() & x.venta_id.ne("") & x.producto.notna() & x.producto.ne("") &
        x.cantidad.notna() & x.cantidad.gt(0) & x.precio_unitario.notna() & x.precio_unitario.ge(0) &
        x.total_venta.notna() & x.total_venta.ge(0))
    rejected=x.loc[~ok].copy(); clean=x.loc[ok].copy()
    before=len(clean); clean=clean.drop_duplicates("venta_id",keep="first"); duplicated=before-len(clean)
    clean["total_venta"]=(clean.cantidad*clean.precio_unitario).round(2)
    clean["fecha"]=clean.fecha.dt.strftime("%Y-%m-%d"); clean["cantidad"]=clean.cantidad.astype(int)
    metrics={"registros_entrada":entrada,"registros_validos":len(clean),"registros_rechazados":len(rejected),"duplicados_id":duplicated}
    return clean,rejected,metrics
