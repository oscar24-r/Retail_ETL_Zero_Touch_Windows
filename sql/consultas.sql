SELECT COUNT(*) FROM ventas_consolidadas;
SELECT region,COUNT(*) operaciones,ROUND(SUM(total_venta),2) ventas FROM ventas_consolidadas GROUP BY region ORDER BY ventas DESC;
SELECT * FROM ejecuciones ORDER BY id DESC;
SELECT * FROM resumen_region;
