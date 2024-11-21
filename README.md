# PROYECTO_RSM-KODIGO_DAJ10

1. GENERALIDADES DEL PROYECTO Y REQUERIMIENTOS 

Como proyecto final, los alumnos del bootcamp tienen que realizar un proyecto que consiste en optimizar las ventas de una tienda en línea mediante el análisis de datos, se debe diseñar una base de datos y analizar la información de ventas, clientes y productos. 

El proyecto se divide en varias fases, como se indica a continuación.
* Diseño de Base de Datos.
* Extracción y Manipulación de Datos.
* Análisis Exploratorio de Datos.
* Creación de Dashboard.
* Modelo Predictivo (Opcional).
* Reporte y Presentación.

El objetivo final es proporcionar estrategias basadas en datos para mejorar las ventas del cliente.

###################################################################

2. DATOS RELEVANTES, DESCRIPCION Y REVISION DE LOS INSUMOS

A continuación se describen los datos y el contenido de los tres Data Set que han sido proporcionados para proyecto.

2.1 Descripción del contenido
Estos archivos se encuentran en una carpeta llamada DATA-SETS en formato de csv, para su analisis:

Data Set Clientes: Este dataset contiene información sobre los clientes de una empresa.
Data Set Productos: Este dataset incluye información sobre los productos ofrecidos por la empresa.
Data Set Ventas: Este dataset contiene registros de ventas.

2.2 Relevancia de cada Data Set

Clientes: Es la base para cualquier análisis de comportamiento del cliente, segmentación de mercado, y estrategias de marketing personalizadas.
Productos: Es fundamental para el análisis de inventarios, planificación de estrategias de precios, y análisis de ventas por categoría de producto.
Ventas: Este dataset es esencial para el análisis de rendimiento de ventas, tendencias de compra, y evaluación del impacto de las campañas de marketing.

2.3 Hallazgos Clave y Errores a Revisar
Esto lo podemos encontrar el documento de informe del proyecto bajo la seccion 2.3 donde amplian todos esto datos.


###################################################################

3. DISEÑO DE LA BASE DE DATOS
   Se encuentra ubicada en una carpeta llamada 1_DISEÑO_BD
   
3.1 Diagrama Entidad-Relación
Para la creación del diagrama entidad-relación (ERD) con base en los datasets proporcionados ("clientes", "productos" y "ventas"), identificamos las entidades principales, sus atributos, y las relaciones entre ellas. 


Diagrama Visual

Para generar el diagrama se utilizó el lenguaje DBML (Database Markup Language):

https://dbdiagram.io/d/PROYECTO_FINAL-673c1b28e9daa85acaea168c

El codigo DBML se encuentra en la carpeta de 1_DISEÑO_BD para una mayor verificación de la misma.

3.2 Implementación en el DBMS

Previo al análisis y normalización de datos es necesario que se ejecute la creación de la base de datos y tablas, una vez lista esa parte, se procede a cargar la información de los Data Sets en el ambiente habilitado.
Se decidió utilizar como motor de base datos SQLServer 2019 por la facilidad que se tiene en cuanto a disponibilidad y acceso al uso de un ambiente de desarrollo.
Los pasos requeridos en esta fase pueden resumirse así:
Crear la Base de Datos: Crear la base de datos RSMDB.
Crear Usuario y Roles: Crear un usuario rsmuser y asignarle roles de lectura y escritura.
Crear las Tablas: Crear las tablas clientes, productos y ventas con sus respectivas relaciones.
Verificar: Asegurar que las tablas y relaciones se han creado correctamente mediante consultas de verificación.

Para la creación de la creacion de la base de datos se encuentra en la carpeta de 1_DISEÑO_DB

###################################################################

4. EXTRACCION Y MANIPULACION DE DATOS
   
4.1 Importación de datos

SQL Server ofrece un asistente de Importación y Exportación para cargar datos desde archivos CSV a las tablas de SQL Server.
Abrir SQL Server Management Studio (SSMS).
* Conectarse a la instancia de SQL Server.
* Hacer clic derecho en la base de datos RSMDB y seleccionar Tasks -> Import Data.
* Elegir el origen de datos:
      Source: Flat File Source
      File name: Seleccionamos el archivo CSV correspondiente (clientes.csv, productos.csv, o ventas.csv).
      Configuramos los delimitadores y otros parámetros según sea necesario.
* Elegir el destino de datos:
      Destination: SQL Server Native Client
      Server name: SQLSRV.
      Database: RSMDB.
* Configurar las opciones de mapeo de columnas para asegurar que las columnas de los archivos CSV correspondan correctamente a las columnas de las tablas SQL.
* Ejecutar el proceso de importación.

4.2 Consultas SQL para Extracción de Información

La siguientes, son consultas SQL para extraer la información solicitada, basadas en los datos de los datasets y el procedimiento de importación descritos anteriormente.

4.2.1. Ventas Totales por Categoría de Producto (ventas_totales_por_categoria.sql):
   
Esta consulta calcula la suma de las ventas agrupadas por categoría de producto. Este script se encuentra en la carpeta de 2_EXTRACCION_MANIPULACION

4.2.2. Clientes con Mayor Valor de Compra (clientes_mayor_valor_compra.sql):
   
Esta consulta calcula el total gastado por cada cliente y ordena los resultados de mayor a menor. Este script se encuentra en la carpeta de 2_EXTRACCION_MANIPULACION
   
4.2.3. Productos Más Vendidos por Región (productos_mas_vendidos_por_region.sql):
   
Esta consulta determina los productos más populares en cada región, basándose en la cantidad total vendida. Este script se encuentra en la carpeta de 2_EXTRACCION_MANIPULACION
