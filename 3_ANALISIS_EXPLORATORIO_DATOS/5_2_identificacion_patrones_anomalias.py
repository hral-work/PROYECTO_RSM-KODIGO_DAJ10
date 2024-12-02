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

# Graficar ventas diarias
plt.plot(ventas_diarias['FechaVenta'], ventas_diarias['Cantidad'])  # Genera un gráfico de líneas para las ventas diarias
plt.title('Ventas Diarias')  # Añade un título al gráfico
plt.xlabel('Fecha')  # Etiqueta el eje x como 'Fecha'
plt.ylabel('Cantidad Vendida')  # Etiqueta el eje y como 'Cantidad Vendida'
plt.show()  # Muestra el gráfico

# Paso 4: Análisis de Comportamiento de Compra de Clientes
# Calcular y graficar el comportamiento de compra de los clientes

# Calcular ventas totales por cliente
ventas_por_cliente = ventas.groupby('ClienteID')['Cantidad'].sum().reset_index()  # Agrupa las ventas por 'ClienteID' y suma las cantidades

# Graficar la distribución de ventas por cliente
plt.hist(ventas_por_cliente['Cantidad'], bins=20, edgecolor='black')  # Genera un histograma para las ventas por cliente
plt.title('Distribución de Ventas por Cliente')  # Añade un título al gráfico
plt.xlabel('Total de Ventas por Cliente')  # Etiqueta el eje x
plt.ylabel('Número de Clientes')  # Etiqueta el eje y
plt.show()  # Muestra el gráfico

# Paso 5: Identificar Anomalías
# Encontrar picos de ventas inusuales y productos con bajas ventas

# Detectar picos de ventas inusuales
q1 = ventas_diarias['Cantidad'].quantile(0.25)  # Calcula el primer cuartil (Q1) de las ventas diarias
q3 = ventas_diarias['Cantidad'].quantile(0.75)  # Calcula el tercer cuartil (Q3) de las ventas diarias
iqr = q3 - q1  # Calcula el rango intercuartil (IQR)
umbral_alto = q3 + 1.5 * iqr  # Establece el umbral para detectar valores atípicos

anomalies = ventas_diarias[ventas_diarias['Cantidad'] > umbral_alto]  # Identifica anomalías basadas en el umbral alto

plt.plot(ventas_diarias['FechaVenta'], ventas_diarias['Cantidad'])  # Genera un gráfico de líneas para las ventas diarias
plt.scatter(anomalies['FechaVenta'], anomalies['Cantidad'], color='red')  # Añade puntos de dispersión para las anomalías detectadas
plt.title('Anomalías en Ventas Diarias')  # Añade un título al gráfico
plt.xlabel('Fecha')  # Etiqueta el eje x como 'Fecha'
plt.ylabel('Cantidad Vendida')  # Etiqueta el eje y como 'Cantidad Vendida'
plt.show()  # Muestra el gráfico

# Productos con bajas ventas
# Selecciona solo columnas numéricas antes de agrupar y sumar
ventas_por_producto = ventas.select_dtypes(include=[np.number]).groupby('ProductoID').sum().reset_index()  # Agrupa las ventas por 'ProductoID' y suma las cantidades
productos_bajas_ventas = ventas_por_producto[ventas_por_producto['Cantidad'] < ventas_por_producto['Cantidad'].quantile(0.1)]  # Identifica productos con ventas por debajo del décimo percentil

print("Productos con bajas ventas:")
print(productos_bajas_ventas)  # Imprime la lista de productos con bajas ventas