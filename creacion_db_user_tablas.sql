-- 1. Creación de la Base de Datos
CREATE DATABASE RSMDB;
GO

-- 2. Creación del Usuario y Asignación de Permisos
USE RSMDB;
GO

-- Crear usuario
CREATE USER rsmuser WITH PASSWORD = 'cipitio2024';
GO

-- Crear roles
CREATE ROLE db_datareader;
CREATE ROLE db_datawriter;
GO

-- Asignar permisos al usuario
ALTER ROLE db_datareader ADD MEMBER rsmuser;
ALTER ROLE db_datawriter ADD MEMBER rsmuser;
GO

-- 3. Creación de las Tablas
CREATE TABLE clientes (
  ClienteID int PRIMARY KEY NOT NULL,
  NombreCliente varchar(255),
  Email varchar(255),
  Telefono varchar(50),
  Direccion varchar(255)
);
GO

CREATE TABLE productos (
  ProductoID int PRIMARY KEY NOT NULL,
  NombreProducto varchar(255),
  Categoria varchar(255),
  PrecioUnitario decimal(10, 2)
);
GO

CREATE TABLE ventas (
  VentaID int PRIMARY KEY NOT NULL,
  ClienteID int,
  ProductoID int,
  Cantidad int,
  FechaVenta date,
  Region varchar(50),
  FOREIGN KEY (ClienteID) REFERENCES clientes (ClienteID),
  FOREIGN KEY (ProductoID) REFERENCES productos (ProductoID)
);
GO
