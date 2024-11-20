-- Esta consulta determina los productos más populares en cada región, basándose en la cantidad total vendida.

SELECT 
    v.Region,
    p.NombreProducto,
    SUM(v.Cantidad) AS CantidadTotalVendida
FROM 
    ventas v
JOIN 
    productos p ON v.ProductoID = p.ProductoID
GROUP BY 
    v.Region, p.NombreProducto
ORDER BY 
    v.Region, CantidadTotalVendida DESC;
