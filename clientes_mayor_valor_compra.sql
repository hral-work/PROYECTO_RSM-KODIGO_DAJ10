--Esta consulta calcula el total gastado por cada cliente y ordena los resultados de mayor a menor.
SELECT 
    c.ClienteID,
    c.NombreCliente,
    SUM(v.Cantidad * p.PrecioUnitario) AS TotalGastado
FROM 
    ventas v
JOIN 
    clientes c ON v.ClienteID = c.ClienteID
JOIN 
    productos p ON v.ProductoID = p.ProductoID
GROUP BY 
    c.ClienteID, c.NombreCliente
ORDER BY 
    TotalGastado DESC;
