# Paso 1: Preparar el Entorno
# Instala las librerías necesarias con el siguiente comando:
# pip install pandas numpy matplotlib

import pandas as pd  # Importa la librería de manipulación de datos Pandas
import numpy as np  # Importa la librería NumPy para operaciones numéricas
import matplotlib.pyplot as plt  # Importa la librería de visualización Matplotlib

# Paso 2: Cargar los Datos
# Leer los archivos CSV en DataFrames de pandas

# Cargar los archivos CSV
clientes = pd.read_csv('clientes.csv')  # Carga el archivo CSV 'clientes.csv' en un DataFrame
productos = pd.read_csv('productos.csv')  # Carga el archivo CSV 'productos.csv' en un DataFrame
ventas = pd.read_csv('ventas.csv')  # Carga el archivo CSV 'ventas.csv' en un DataFrame

# Paso 3: Analizar Series Temporales de Ventas
# Identificar tendencias ascendentes o descendentes

# Convertir FechaVenta a formato de fecha
ventas['FechaVenta'] = pd.to_datetime(ventas['FechaVenta'])  # Convierte la columna 'FechaVenta' a tipo datetime

# Agrupar ventas por fecha y sumar solo la columna 'Cantidad'
ventas_diarias = ventas.groupby('FechaVenta')['Cantidad'].sum().reset_index()  # Agrupa las ventas por fecha y suma las cantidades

# Graficar ventas diarias con gráfico de barras
plt.figure(figsize=(15, 6))  # Tamaño de la figura
plt.bar(ventas_diarias['FechaVenta'], ventas_diarias['Cantidad'], width=1.0)  # Genera un gráfico de barras para las ventas diarias
plt.title('Ventas Diarias')  # Añade un título al gráfico
plt.xlabel('Fecha')  # Etiqueta el eje x como 'Fecha'
plt.ylabel('Cantidad Vendida (Unidades)')  # Etiqueta el eje y como 'Cantidad Vendida (Unidades)'
plt.xticks(rotation=45)  # Rota las etiquetas del eje x para mayor legibilidad
plt.tight_layout()  # Ajusta el diseño para que todo encaje bien
plt.show()  # Muestra el gráfico


# Paso 4: Análisis de Comportamiento de Compra de Clientes
# Calcular y graficar el comportamiento de compra de los clientes

# Calcular ventas totales por cliente
ventas_por_cliente = ventas.groupby('ClienteID')['Cantidad'].sum().reset_index()  # Agrupa las ventas por 'ClienteID' y suma las cantidades

# Graficar la distribución de ventas por cliente con gráfico de barras
plt.figure(figsize=(15, 6))  # Tamaño de la figura
plt.bar(ventas_por_cliente['ClienteID'], ventas_por_cliente['Cantidad'], color='blue')  # Genera un gráfico de barras para la distribución de ventas por cliente
plt.title('Distribución de Ventas por Cliente')  # Añade un título al gráfico
plt.xlabel('ClienteID')  # Etiqueta el eje x como 'ClienteID'
plt.ylabel('Total de Ventas por Cliente (Unidades)')  # Etiqueta el eje y como 'Total de Ventas por Cliente (Unidades)'
plt.xticks(rotation=90)  # Rota las etiquetas del eje x para mayor legibilidad
plt.tight_layout()  # Ajusta el diseño para que todo encaje bien
plt.show()  # Muestra el gráfico

# Productos con bajas ventas
# Selecciona solo columnas numéricas antes de agrupar y sumar
ventas_por_producto = ventas.select_dtypes(include=[np.number]).groupby('ProductoID').sum().reset_index()  # Agrupa las ventas por 'ProductoID' y suma las cantidades
productos_bajas_ventas = ventas_por_producto[ventas_por_producto['Cantidad'] < ventas_por_producto['Cantidad'].quantile(0.1)]  # Identifica productos con ventas por debajo del décimo percentil

print("Productos con bajas ventas:")
print(productos_bajas_ventas)  # Imprime la lista de productos con bajas ventas
