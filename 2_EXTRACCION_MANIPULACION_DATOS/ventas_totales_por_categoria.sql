-- Esta consulta calcula la suma de las ventas agrupadas por categoría de producto.
SELECT 
    p.Categoria,
    SUM(v.Cantidad * p.PrecioUnitario) AS VentasTotales
FROM 
    ventas v
JOIN 
    productos p ON v.ProductoID = p.ProductoID
GROUP BY 
    p.Categoria;
