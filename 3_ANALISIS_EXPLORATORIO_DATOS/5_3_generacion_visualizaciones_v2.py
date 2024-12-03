# Paso 1: Preparar el Entorno
# Instala las librerías necesarias si aún no las tienes:
# pip install matplotlib seaborn pandas numpy

import pandas as pd  # Importa la librería de manipulación de datos Pandas
import matplotlib.pyplot as plt  # Importa la librería de visualización Matplotlib
import seaborn as sns  # Importa la librería de visualización Seaborn

# Paso 2: Cargar los Datos
# Leer los archivos CSV en DataFrames de pandas

# Cargar los archivos CSV
clientes = pd.read_csv('clientes.csv')  # Carga el archivo CSV 'clientes.csv' en un DataFrame
productos = pd.read_csv('productos.csv')  # Carga el archivo CSV 'productos.csv' en un DataFrame
ventas = pd.read_csv('ventas.csv')  # Carga el archivo CSV 'ventas.csv' en un DataFrame

# Paso 3: Crear Visualizaciones

# 1. Gráfico de Barras: Ventas Totales por Categoría de Producto

# Verificar que la columna 'Categoria' existe en productos
if 'Categoria' in productos.columns:
    # Calcular ventas totales por categoría de producto
    ventas_productos = ventas.merge(productos, on='ProductoID')  # Une las tablas 'ventas' y 'productos' en 'ProductoID'
    ventas_categoria = ventas_productos.groupby('Categoria')['Cantidad'].sum().reset_index()  # Agrupa las ventas por 'Categoria' y suma las cantidades

    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))  # Crea una nueva figura con un tamaño específico
    sns.barplot(x='Categoria', y='Cantidad', data=ventas_categoria)  # Genera un gráfico de barras con los datos de ventas por categoría
    plt.title('Ventas Totales por Categoría de Producto')  # Añade un título al gráfico
    plt.xlabel('Categoría')  # Etiqueta el eje x como 'Categoría'
    plt.ylabel('Cantidad Vendida')  # Etiqueta el eje y como 'Cantidad Vendida'
    plt.xticks(rotation=45)  # Rota las etiquetas del eje x para mejor legibilidad
    plt.show()  # Muestra el gráfico

    # Análisis
    print("Este gráfico de barras muestra las ventas totales agrupadas por la categoría de producto. Se puede observar cuál categoría tiene el mayor volumen de ventas.")
else:
    print("La columna 'Categoria' no existe en el DataFrame 'productos'.")

# 2. Gráfico de Barras: Tendencia de Ventas Diarias

# Convertir FechaVenta a formato de fecha
ventas['FechaVenta'] = pd.to_datetime(ventas['FechaVenta'])  # Convierte la columna 'FechaVenta' a tipo datetime

# Agrupar ventas por fecha
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

# Análisis
print("Este gráfico de barras muestra la tendencia de ventas diarias. Se pueden identificar patrones y fluctuaciones en las ventas a lo largo del tiempo.")

# 3. Histograma: Distribución de Ventas por Producto

# Crear histograma
plt.figure(figsize=(10, 6))  # Crea una nueva figura con un tamaño específico
sns.histplot(ventas['Cantidad'], bins=30, kde=True)  # Genera un histograma para la distribución de ventas por producto con una línea KDE
plt.title('Distribución de Ventas por Producto')  # Añade un título al gráfico
plt.xlabel('Cantidad Vendida')  # Etiqueta el eje x como 'Cantidad Vendida'
plt.ylabel('Frecuencia')  # Etiqueta el eje y como 'Frecuencia'
plt.show()  # Muestra el gráfico

# Análisis
print("Este histograma muestra la distribución de la cantidad de ventas por producto. La línea KDE ayuda a visualizar la densidad de las ventas.")

# 4. Diagrama de Dispersión: Ventas por Cliente

# Calcular ventas totales por cliente
ventas_cliente = ventas.groupby('ClienteID')['Cantidad'].sum().reset_index()  # Agrupa las ventas por 'ClienteID' y suma las cantidades

# Crear diagrama de dispersión
plt.figure(figsize=(10, 6))  # Crea una nueva figura con un tamaño específico
sns.scatterplot(x='ClienteID', y='Cantidad', data=ventas_cliente)  # Genera un gráfico de dispersión para las ventas por cliente
plt.title('Ventas por Cliente')  # Añade un título al gráfico
plt.xlabel('ClienteID')  # Etiqueta el eje x como 'ClienteID'
plt.ylabel('Cantidad Vendida')  # Etiqueta el eje y como 'Cantidad Vendida'
plt.show()  # Muestra el gráfico

# Análisis
print("Este diagrama de dispersión muestra las ventas totales por cliente. Se pueden identificar clientes con compras altas y bajas.")