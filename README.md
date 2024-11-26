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

El resultado de estos querys han sido exitosos, los que representan estos resultados seran esstudiados en fases posteriores.

