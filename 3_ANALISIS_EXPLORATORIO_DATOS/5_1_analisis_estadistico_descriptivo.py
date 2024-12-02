# Paso 1: Preparar el Entorno
# Se debe tener las librerías necesarias instaladas. Pueden ser instaladas usando pip:
# pip install pandas numpy

import pandas as pd  # Importa la librería de manipulación de datos Pandas
import numpy as np  # Importa la librería NumPy para operaciones numéricas
import matplotlib.pyplot as plt  # Importa la librería de visualización Matplotlib

# Paso 2: Cargar los Datos
# Leer los archivos CSV en DataFrames de pandas

# Cargar los archivos CSV en un DataFrame
clientes = pd.read_csv('clientes.csv')  
productos = pd.read_csv('productos.csv') 
ventas = pd.read_csv('ventas.csv') 

# Paso 3: Calcular Estadísticas Básicas
# Calcular estadísticas básicas como medias, medianas y desviaciones estándar

# Estadísticas descriptivas para ventas
ventas_descriptivas = ventas.describe()  # Genera estadísticas descriptivas para el DataFrame 'ventas'

# Media y mediana
media_ventas = ventas['Cantidad'].mean()  # Calcula la media de la columna 'Cantidad' en 'ventas'
mediana_ventas = ventas['Cantidad'].median()  # Calcula la mediana de la columna 'Cantidad' en 'ventas'
desviacion_estandar_ventas = ventas['Cantidad'].std()  # Calcula la desviación estándar de la columna 'Cantidad' en 'ventas'

print("Paso 3: Calcular Estadísticas Básicas")
print("Estadísticas Básicas de Ventas:")
print(ventas_descriptivas)
print(f"Media de Ventas: {media_ventas}")
print(f"Mediana de Ventas: {mediana_ventas}")
print(f"Desviación Estándar de Ventas: {desviacion_estandar_ventas}")

# Paso 4: Identificar Variables Importantes
# Calcular el número de transacciones, ventas promedio por cliente, etc.

# Número de transacciones
num_transacciones = ventas.shape[0]  # Calcula el número de transacciones (filas) en el DataFrame 'ventas'

# Ventas promedio por cliente
ventas_por_cliente = ventas.groupby('ClienteID')['Cantidad'].sum()  # Agrupa las ventas por 'ClienteID' y suma la 'Cantidad' vendida
ventas_promedio_cliente = ventas_por_cliente.mean()  # Calcula la media de las ventas por cliente

print("Paso 4: Identificar Variables Importantes")
print(f"Número de Transacciones: {num_transacciones}")
print(f"Ventas Promedio por Cliente: {ventas_promedio_cliente}")

# Paso 5: Analizar la Distribución de las Ventas
# Analizar la distribución de las ventas para detectar patrones estacionales o concentraciones en determinados productos

# Distribución de ventas por producto
ventas_por_producto = ventas.groupby('ProductoID')['Cantidad'].sum()  # Agrupa las ventas por 'ProductoID' y suma la 'Cantidad' vendida

# Gráfica de distribución de ventas por producto
plt.figure(figsize=(10, 6))  # Crea una nueva figura con un tamaño específico
ventas_por_producto.plot(kind='bar')  # Genera un gráfico de barras con los datos de ventas por producto
plt.title('Paso 5 Analizar la Distribución de las Ventas - Distribución de Ventas por Producto')  # Añade un título al gráfico
plt.xlabel('ProductoID')  # Etiqueta el eje x como 'ProductoID'
plt.ylabel('Cantidad Vendida')  # Etiqueta el eje y como 'Cantidad Vendida'
plt.show()  # Muestra el gráfico

# Análisis de ventas estacionales (FechaVenta está en formato 'YYYY-MM-DD')
ventas['FechaVenta'] = pd.to_datetime(ventas['FechaVenta'])  # Convierte la columna 'FechaVenta' a un tipo de dato datetime
ventas['Mes'] = ventas['FechaVenta'].dt.month  # Crea una nueva columna 'Mes' basada en el mes de 'FechaVenta'
ventas_por_mes = ventas.groupby('Mes')['Cantidad'].sum()  # Agrupa las ventas por 'Mes' y suma la 'Cantidad' vendida

# Gráfica de ventas por mes
plt.figure(figsize=(10, 6))  # Crea una nueva figura con un tamaño específico
ventas_por_mes.plot(kind='line')  # Genera un gráfico de líneas con los datos de ventas por mes
plt.title('Paso 5: Analizar la Distribución de las Ventas - Ventas por Mes')  # Añade un título al gráfico
plt.xlabel('Mes')  # Etiqueta el eje x como 'Mes'
plt.ylabel('Cantidad Vendida')  # Etiqueta el eje y como 'Cantidad Vendida'
plt.show()  # Muestra el gráfico

# Paso 6: Resumir y Guardar Resultados
# Finalmente, guarda los resultados del análisis para su inclusión en el informe final

# Guardar estadísticas básicas en un archivo CSV
ventas_descriptivas.to_csv('estadisticas_basicas_ventas.csv')  # Guarda el DataFrame 'ventas_descriptivas' en un archivo CSV

# Guardar resumen de ventas por cliente
ventas_por_cliente.to_csv('ventas_por_cliente.csv')  # Guarda el DataFrame 'ventas_por_cliente' en un archivo CSV

# Guardar análisis de ventas por mes
ventas_por_mes.to_csv('ventas_por_mes.csv')  # Guarda el DataFrame 'ventas_por_mes' en un archivo CSV

print("Análisis completado y resultados guardados.")