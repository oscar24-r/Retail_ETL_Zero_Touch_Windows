import pandas as pd,pytest
from src.transform import transformar
def sample():
 return pd.DataFrame([dict(venta_id="V1",fecha="2026-10-01",cliente_id="C1",producto_id="P1",producto="Mouse",cantidad=2,precio_unitario=10,total_venta=20,canal="Web",region="Lima")])
def test_valido():
 c,r,m=transformar(sample()); assert len(c)==1 and len(r)==0
def test_fecha_invalida():
 d=sample(); d.loc[0,"fecha"]="xxx"; c,r,m=transformar(d); assert len(c)==0 and len(r)==1
def test_duplicado():
 c,r,m=transformar(pd.concat([sample(),sample()])); assert len(c)==1 and m["duplicados_id"]==1
def test_cantidad_negativa():
 d=sample(); d.loc[0,"cantidad"]=-1; c,r,m=transformar(d); assert len(c)==0
def test_columnas_faltantes():
 with pytest.raises(ValueError): transformar(pd.DataFrame({"venta_id":["V1"]}))
