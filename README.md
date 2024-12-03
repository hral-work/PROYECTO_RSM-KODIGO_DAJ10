PROYECTO DE EVALUACIÓN RSM - KODIGO - DATA ANALYST JR - GRUPO 02

URL DE GITHUB: https://github.com/hral-work/PROYECTO_RSM-KODIGO_DAJ10.git

ALUMNOS:
Katia Elizabeth Martínez -  k00002733.
Rafael Alexander Martínez - k00002735.
Javier Antonio Valle - k00002730.
Hugo Robin Aparicio - k00002729.

ENTREGABLE DEL AVANCE 1: 21 de noviembre de 2024.
Diseño de base de datos | Extracción y Manipulación de datos.


1. GENERALIDADES DEL PROYECTO Y REQUERIMIENTOS 

Como proyecto final, los alumnos del bootcamp tienen que realizar un proyecto que consiste en optimizar las ventas de una tienda en línea mediante el análisis de datos, se debe diseñar una base de datos y analizar la información de ventas, clientes y productos. 

El proyecto se divide en varias fases, como se indica a continuación.
Diseño de Base de Datos.
Extracción y Manipulación de Datos.
Análisis Exploratorio de Datos.
Creación de Dashboard.
Modelo Predictivo (Opcional).
Reporte y Presentación.
El objetivo final es proporcionar estrategias basadas en datos para mejorar las ventas del cliente.

Toda la información recopilada, procedimientos, scripts y demas datos referentes al dimiensionamiento del analisis y solucion de requerimientos han sido plasmados en el documento PROYECTO_RSM_KODIGO_DAJ10.pdf
https://github.com/hral-work/PROYECTO_RSM-KODIGO_DAJ10/blob/main/PROYECTO_RSM_KODIGO_DAJ10.pdf

###################################################################

2. DATOS RELEVANTES, DESCRIPCION Y REVISION DE LOS INSUMOS
A continuación se describen los datos y el contenido de los tres Data Set que han sido proporcionados para proyecto.

2.1 Descripción del contenido

Data Set Clientes
Este dataset contiene información sobre los clientes de una empresa.

Data Set Productos
Este dataset incluye información sobre los productos ofrecidos.

Data Set Ventas
Este dataset contiene registros de ventas.

2.2 Relevancia de cada Data Set
Clientes: Este dataset es crucial para entender quiénes son los clientes de la empresa. Es la base para cualquier análisis de comportamiento del cliente, segmentación de mercado, y estrategias de marketing personalizadas.
Productos: Es fundamental para el análisis de inventarios, planificación de estrategias de precios, y análisis de ventas por categoría de producto.
Ventas: Este dataset es esencial para el análisis de rendimiento de ventas, tendencias de compra, y evaluación del impacto de las campañas de marketing.

2.3 Hallazgos Clave y Errores a Revisar.
Estos son procesos con herramientas básicas como editor de texto, excel y otros, en el documento de informe del proyecto bajo la seccion con éste mismo nombre podemos encontrar mas información donde se amplian todos esto datos.

###################################################################

3. DISEÑO DE LA BASE DE DATOS
   
3.1 Diagrama Entidad-Relación
Para la creación del diagrama entidad-relación (ERD) con base en los datasets proporcionados ("clientes", "productos" y "ventas"), identificamos las entidades principales, sus atributos, y las relaciones entre ellas. 
A continuación, se detalla cómo se puede construir el ERD y qué elementos clave se deben considerar.

Entidades y Atributos

Tabla Clientes:
ClienteID (llave primaria),
NombreCliente,
Email,
Telefono,
Direccion,

Tabla Productos:
ProductoID (llave primaria),
NombreProducto,
Categoria,
PrecioUnitario,

Tabla Ventas:
VentaID (llave primaria),
ClienteID (llave foránea),
ProductoID (llave foránea),
Cantidad,
FechaVenta,
Region,

Relación entre Clientes y Ventas:
Un cliente puede tener asociadas muchas ventas.
Cardinalidad: Uno a Muchos (1:N) desde Clientes a Ventas.
ClienteID en la tabla Ventas es una llave foránea que referencia a ClienteID en la tabla Clientes.

Relación entre Productos y Ventas:
Un producto puede estar asociado con muchas ventas.
Cardinalidad: Uno a Muchos (1:N) desde Productos a Ventas.
ProductoID en la tabla Ventas es una llave foránea que referencia a ProductoID en la tabla Productos.

Llaves y Cardinalidad
Llaves Primarias: ClienteID en Clientes, ProductoID en Productos, y VentaID en Ventas son llaves primarias que identifican de manera única a cada registro en sus respectivas tablas.
Llaves Foráneas: ClienteID y ProductoID en la tabla Ventas son llaves foráneas que crean relaciones entre las tablas, permitiendo la integridad referencial y conexiones lógicas entre datos.
Cardinalidad: Definida por las relaciones 1:N, ya que un cliente puede tener múltiples ventas y un producto puede ser vendido en múltiples transacciones.

Diagrama Visual

Para generar el diagrama se utilizó el lenguaje DBML (Database Markup Language):
https://dbdiagram.io/d/PROYECTO_FINAL-673c1b28e9daa85acaea168c

El codigo DBML se encuentra dentro de la carpeta 1_DISEÑO_DB:
https://github.com/hral-work/PROYECTO_RSM-KODIGO_DAJ10/blob/main/1_DISE%C3%91O_BD/dbml_rsmdb.txt

3.2 Implementación en el DBMS
Previo al análisis y normalización de datos es necesario que se ejecute la creación de la base de datos y tablas, una vez lista esa parte, se procede a cargar la información de los Data Sets en el ambiente habilitado.
Se decidió utilizar como motor de base datos SQLServer 2019 por la facilidad que se tiene en cuanto a disponibilidad y acceso al uso de un ambiente de desarrollo.

Los pasos requeridos en esta fase pueden resumirse así:
Crear la Base de Datos: Crear la base de datos RSMDB.
Crear Usuario y Roles: Crear un usuario rsmuser y asignarle roles de lectura y escritura.
Crear las Tablas: Crear las tablas clientes, productos y ventas con sus respectivas relaciones.
Verificar: Asegurar que las tablas y relaciones se han creado correctamente mediante consultas de verificación.

SCRIPT creacion_db_user_tablas.sql, ete se encuenta dentro de la carpeta 1_DISEÑO_DB: 

https://github.com/hral-work/PROYECTO_RSM-KODIGO_DAJ10/blob/main/1_DISE%C3%91O_BD/creacion_db_user_tablas.sql

###################################################################

4. EXTRACCION Y MANIPULACION DE DATOS
   
4.1 Importación de datos
SQL Server ofrece un asistente de Importación y Exportación para cargar datos desde archivos CSV a las tablas de SQL Server.

-Abrir SQL Server Management Studio (SSMS).

-Conectarse a la instancia de SQL Server.
Hacer clic derecho en la base de datos RSMDB y seleccionar Tasks -> Import Data.
Elegir el origen de datos:
Source: Flat File Source
File name: Seleccionamos el archivo CSV correspondiente (clientes.csv, productos.csv, o ventas.csv).

-Configuramos los delimitadores y otros parámetros según sea necesario.

-Elegir el destino de datos:
Destination: SQL Server Native Client
Server name: SQLSRV.
Database: RSMDB.
Configurar las opciones de mapeo de columnas para asegurar que las columnas de los archivos CSV correspondan correctamente a las columnas de las tablas SQL.

-Ejecutar el proceso de importación.

Una vez que los datos se hayan importado, verificamos que estén correctamente cargados ejecutando algunas consultas básicas en la base de datos.

Verificar que las tablas estén pobladas:
SELECT * FROM clientes;
SELECT * FROM productos;
SELECT * FROM ventas;


4.2 Consultas SQL para Extracción de Información

La siguientes, son consultas SQL para extraer la información solicitada, basadas en los datos de los datasets y el procedimiento de importación descritos anteriormente.

4.2.1. Ventas Totales por Categoría de Producto (ventas_totales_por_categoria.sql):
https://github.com/hral-work/PROYECTO_RSM-KODIGO_DAJ10/blob/main/2_EXTRACCION_MANIPULACION_DATOS/ventas_totales_por_categoria.sql
Esta consulta calcula la suma de las ventas agrupadas por categoría de producto.

4.2.2. Clientes con Mayor Valor de Compra (clientes_mayor_valor_compra.sql):
https://github.com/hral-work/PROYECTO_RSM-KODIGO_DAJ10/blob/main/2_EXTRACCION_MANIPULACION_DATOS/clientes_mayor_valor_compra.sql
Esta consulta calcula el total gastado por cada cliente y ordena los resultados de mayor a menor.
  
4.2.3. Productos Más Vendidos por Región (productos_mas_vendidos_por_region.sql):
https://github.com/hral-work/PROYECTO_RSM-KODIGO_DAJ10/blob/main/2_EXTRACCION_MANIPULACION_DATOS/productos_mas_vendidos_por_region.sql
Esta consulta determina los productos más populares en cada región, basándose en la cantidad total vendida-

Nota: Para el script de Productos Más Vendidos por Región, se tomo en consideración el comentario de evaluación realizado por Luis Quesada: En cuanto a las consultas, en los productos mas vendidos por region, sugiero mostrar solamente el top 3 por region, ya que actualmente muestra todos los productos y no da un vistazo rapido por region para facilidad de analisis.

###################################################################


5. ANALISIS EXPLORATORIO DE DATOS

5.1 Análisis Estadístico Descriptivo

Resumen del proceso que realiza el código:
Preparar el Entorno: Instalamos las librerías necesarias.
Cargar los Datos: Leer los archivos CSV para generar DataFrames.
Calcular Estadísticas Básicas: Calcula medias, medianas, desviaciones estándar y otras estadísticas descriptivas.
Identificar Variables Importantes: Calcular el número de transacciones y ventas promedio por cliente.
Analizar la Distribución de las Ventas: Analizar distribuciones de ventas.

Nombre del script: 5_1_analisis_estadistico_descriptivo_v4.py

# Paso 1: Preparar el Entorno
# Paso 2: Cargar los Datos
# Paso 3: Calcular Estadísticas Básicas
# Paso 4: Identificar Variables Importantes
# Paso 5: Analizar la Distribución de las Ventas
# Paso 6: Resumir y Guardar Resultados

Los resultados de este script se encuentran aca: https://github.com/hral-work/PROYECTO_RSM-KODIGO_DAJ10/tree/main/3_ANALISIS_EXPLORATORIO_DATOS

Interpretar los resultados.
Qué significan estos resultados.
Distribución de Ventas: La distribución de las ventas por cantidad muestra que la mayoría de las transacciones están concentradas alrededor de la media de 4.93 unidades, con una variabilidad moderada.
Ventas por Cliente: La media de ventas por cliente puede ayudar a identificar qué tan valiosos son los clientes en promedio, lo que es crucial para estrategias de marketing y retención.
Variabilidad de Ventas: La desviación estándar ayuda a entender la dispersión en los datos de ventas, lo que es útil para detectar ventas anómalas o patrones inusuales.
Tendencias de Ventas: Conocer la media, mediana y la distribución de las ventas puede ayudar a planificar el inventario y optimizar las estrategias de precios y promociones.
Estos insights pueden proporcionar una base para tomar decisiones de negocio informadas y estratégicas. 


5.2 Identificación de patrones, tendencias.

Procedimiento para este requerimiento:
Preparar el Entorno: Instalamos las librerías necesarias.
Cargar los Datos: Lee los archivos CSV en DataFrames.
Analizar Series Temporales de Ventas: Agrupar ventas por fecha y generar gráfica.
Análisis de Comportamiento de Compra de Clientes: Ventas totales por cliente y su gráfica.
Productos con Bajas Ventas: Imprime lista de productos con bajas ventas.

Nombre del script: 5_2_identificacion_patrones_v5.py

# Paso 1: Preparar el Entorno
# Paso 2: Cargar los Datos
# Paso 3: Analizar Series Temporales de Ventas
# Paso 4: Análisis de Comportamiento de Compra de Clientes

El resultado de este script se muestra aca: https://github.com/hral-work/PROYECTO_RSM-KODIGO_DAJ10/tree/main/3_ANALISIS_EXPLORATORIO_DATOS

Resumen de Resultados y sus Implicaciones.

Análisis de Ventas Diarias:
Gráfico de Barras: Visualización de las ventas diarias. Permite identificar tendencias ascendentes o descendentes en las ventas, ayudando a comprender los patrones de demanda y detectar posibles estacionalidades.
Comportamiento de Compra de Clientes:
Ventas Totales por Cliente: Calcula y grafica las ventas totales por cada cliente. Ayuda a identificar los clientes más valiosos y analizar su comportamiento de compra, lo que puede ser útil para estrategias de marketing y retención de clientes.
Productos con Bajas Ventas:
Identificación de Productos con Bajas Ventas: Generaliza los productos con ventas por debajo del décimo percentil.Permite identificar productos que no están vendiendo bien, lo cual es crucial para la optimización del inventario y las estrategias de producto.
Implicaciones Generales:
Optimización de Estrategias: La visualización y el análisis de datos proporcionan información para la toma de decisiones en áreas como marketing, gestión de clientes y gestión de productos.
Detección de Tendencias: Se pueden identificar patrones de ventas y comportamientos de compra ayuda a prever la demanda futura y a planificar.
Mejora de la Eficiencia: Detectar productos con bajas ventas permite reducir costos de almacenamiento y enfocar recursos en productos más rentables.

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
5.3 Generación de visualizaciones
Resumen del procedimiento para este requerimiento:
Preparar el Entorno:
Instalar las librerías necesarias: matplotlib, seaborn, pandas, numpy.
Cargar los Datos:
Leer los archivos CSV en DataFrames: clientes.csv, productos.csv, ventas.csv.
Crear Visualizaciones:
Ventas Totales por Categoría de Producto: Agrupar ventas por categoría de producto y generar un gráfico de barras.
Tendencia de Ventas Diarias: Agrupar ventas por fecha y generar un gráfico de líneas.
Distribución de Ventas por Producto: Generar un histograma con línea para visualizar la distribución de ventas.
Ventas por Cliente:Agrupar ventas por cliente y generar un gráfico de dispersión.
Matriz de Correlación:Generar un mapa de calor para visualizar la correlación entre las variables de ventas.
Nombre del script: 5_3_generacion_visualizaciones_v2.py

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




El resultado de este otro script es el siguiente:








Resumen de Resultados y Contribución al Negocio.

Ventas por Categoría de Producto:
Resultados: Identificación de categorías con mayores ventas.
Contribución: Mejora en la planificación de inventario y marketing.
Tendencia de Ventas Diarias:
Resultados: Identificación de patrones y fluctuaciones en ventas diarias.
Contribución: Mejora en la previsión de demanda y gestión de inventarios.
Distribución de Ventas por Producto:
Resultados: Variabilidad en ventas de productos.
Contribución: Optimización del portafolio de productos.
Ventas por Cliente:
Resultados: Identificación de clientes clave.
Contribución: Personalización de estrategias de marketing y fidelización.
Matriz de Correlación:
Resultados: Relación entre variables de ventas.
Contribución: Optimización de estrategias de marketing y promociones.
Este análisis integral apoya la toma de decisiones estratégicas, mejora la planificación y aumenta la eficiencia operativa.

###################################################################

6 CREACIÓN DE DASHBOARD

6.1 Desarrollo del Dashboard en Power BI

Resumen del Procedimiento:
Importar Datos a Power BI: Cargar los datos procesados para utilizarlos en el dashboard.
Resumen de KPIs Clave: Crear un panel de control con indicadores clave de rendimiento para una visión rápida del negocio.
Gráficos de Tendencias de Ventas: Visualizar las tendencias de ventas a lo largo del tiempo para identificar patrones.

Paso 1: Importar Datos a Power BI
En esta etapa, estamos cargando los datos procesados en Power BI para que podamos usarlos en nuestras visualizaciones.
Lo primero que se realiza es abrir Power BI Desktop para la creación de los Dashboard
Seleccionar en la ventana de inicio, “Obtener datos” para este caso se realiza directamente con la Base de datos de SQLServer.
Se establecen las credenciales definidas en esa base de datos, se buscan las tablas de clientes, productos y ventas cargados anteriormente.
Se finaliza con transformar datos en Power BI.

Paso 2: Desarrollar un Resumen de KPIs Clave
Aquí, estamos creando un panel de control con indicadores clave de rendimiento (KPIs) que proporcionan una visión rápida del rendimiento del negocio.
Se procede a realizar la creación de los KPIs según los requerimientos que se necesitan en el proyecto.
Ventas Totales: Usa una medida que sume la cantidad vendida.
Número de Transacciones: Cuenta el número total de ventas.
Clientes Únicos: Cuenta el número distinto de clientes.
Paso 3: Implementar Gráficos de Tendencias de Ventas
Se realizan gráficos de tendencias, en donde se mostrará las ventas a lo largo del tiempo.
Agrega el campo de fecha al eje x y la cantidad de ventas al eje y.
Segmentar los gráficos por diferentes criterios como producto o región usando filtros.
Visualizaciones de segmentación para permitir a los usuarios filtrar los datos por criterios diferentes.

Explicación: Estos gráficos de líneas nos ayudan a visualizar las tendencias de ventas a lo largo del tiempo, identificando patrones y estacionalidades.

Resumen de Resultados y Análisis de Insights

Descripción de los datos graficados.
KPIs Clave: Proporcionan una visión rápida del rendimiento del negocio, permitiendo a los directivos tomar decisiones informadas basadas en los principales indicadores.
Gráficos de Tendencias: Ayudan a identificar patrones y fluctuaciones en las ventas a lo largo del tiempo, facilitando la planificación de inventarios y estrategias de marketing.
Breve explicación de las visualizaciones.
Gráfico de Líneas: La tendencia de ventas revela patrones estacionales y fluctuaciones en las ventas a lo largo del tiempo.
TreeMap: Muestra una representación visual de las ventas totales por categoría la cual permite identificar patrones y valores atípicos según el tamaño y color de los rectángulos.
Gráfico Circular: Muestra el porcentaje de ingreso por ventas según la región.
Gráfico de Barras: Las ventas totales por categoría de producto agrupadas por año,  muestran qué categorías tienen el mayor volumen de ventas y permiten una rápida comparación visual respecto a los años anteriores y posteriores.
Matriz: Muestra el detalle de las ventas por región y año permitiendo hacer drill down a categoría de producto y producto específico.
Insights Clave
Identificación de Productos y Categorías Populares: Conocer qué productos y categorías tienen mayores ventas permite enfocar esfuerzos en mantener un inventario óptimo y dirigir las promociones hacia esos productos.
Análisis de Tendencias: Identificar patrones estacionales y tendencias en las ventas diarias facilita una mejor planificación y gestión del inventario, así como el diseño de campañas de marketing más efectivas.
Segmentación y Fidelización de Clientes: Entender el comportamiento de compra de los clientes ayuda a segmentarlos eficazmente, permitiendo personalizar estrategias de retención y aumentar la fidelización.
Optimización de Precios y Promociones: Analizar la distribución de ventas por producto y la correlación entre variables puede influir en las decisiones de precios y estrategias promocionales, mejorando la eficiencia y efectividad.
Estos insights proporcionan una base sólida para tomar decisiones estratégicas informadas, optimizar operaciones y mejorar la satisfacción del cliente, impulsando así el rendimiento general del negocio. 
