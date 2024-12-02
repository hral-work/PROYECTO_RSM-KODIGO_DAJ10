-- Esta consulta determina los productos más populares en cada región (top 3), basándose en la cantidad total vendida.

SELECT 
    Region,
    NombreProducto,
    CantidadTotalVendida
FROM (
    SELECT 
        v.Region,
        p.NombreProducto,
        SUM(v.Cantidad) AS CantidadTotalVendida,
        ROW_NUMBER() OVER (PARTITION BY v.Region ORDER BY SUM(v.Cantidad) DESC) AS rn
    FROM 
        ventas v
    JOIN 
        productos p ON v.ProductoID = p.ProductoID
    GROUP BY 
        v.Region, p.NombreProducto
) AS ventas_rankeadas
WHERE 
    ventas_rankeadas.rn <= 3
ORDER BY 
    Region, CantidadTotalVendida DESC;

