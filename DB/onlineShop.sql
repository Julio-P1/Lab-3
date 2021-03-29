CREATE DATABASE onlineShop;
USE onlineShop;

CREATE TABLE IF NOT EXISTS Usuarios (
    idUsuario INT PRIMARY KEY AUTO_INCREMENT,
    username  VARCHAR(50) NOT NULL ,
    password VARCHAR(60) NOT NULL ,
    email VARCHAR(50),
    creationDate DATETIME
);

INSERT INTO Usuarios (username, password, email, creationDate)
VALUES ('julioP', md5(md5('julioP') + md5('paizjulio1')), 'juliopaiz@galileo.edu', now());

INSERT INTO Usuarios (username, password, email, creationDate)
VALUES ('ramiroJ', md5(md5('ramiroJ') + md5('juarezramiro2')), 'ramiroJ@mail.com', now());

INSERT INTO Usuarios (username, password, email, creationDate)
VALUES ('gersonS', md5(md5('gersonS') + md5('sotogerson3')), 'gersonsoto@minedu.gov', now());

DROP TABLE Usuarios;

SELECT * FROM Usuarios;

UPDATE Usuarios as u SET u.username = 'Progra56', u.password = md5(md5('Progra5') + md5('ttttt333'))
WHERE idUsuario = 4;

CREATE TABLE IF NOT EXISTS Compras (
    idCompra INT PRIMARY KEY AUTO_INCREMENT,
    userID INT NOT NULL ,
    fechaHoraCompra DATETIME NOT NULL ,
    totalCompra DECIMAL(6, 2) ,

    CONSTRAINT fk_userID FOREIGN KEY (userID)
        REFERENCES Usuarios (idUsuario)
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

SELECT * FROM compras WHERE fechaHoraCompra BETWEEN '2019-11-12 17:21:02' AND '2020-10-09 17:41:48';

DROP TABLE Compras;

SELECT * FROM Compras;

CREATE TABLE IF NOT EXISTS Productos (
    idProducto INT PRIMARY KEY AUTO_INCREMENT,
    nombreProducto VARCHAR(50) NOT NULL ,
    fechaIngreso DATETIME,
    precioUnitario DECIMAL(6, 2)

);

SELECT * FROM Productos;

DROP TABLE Productos;

CREATE TABLE IF NOT EXISTS detalleCompras (
    idDetalleCompra INT PRIMARY KEY AUTO_INCREMENT,
    compraID INT NOT NULL ,
    productoId INT NOT NULL ,
    cantidad INT NOT NULL ,
    precio DECIMAL (6, 2) ,
    subTotal DECIMAL(10, 2) AS (cantidad * precio) NOT NULL ,

    CONSTRAINT fk_compraID FOREIGN KEY (compraID)
        REFERENCES Compras (idCompra)
            ON UPDATE NO ACTION
            ON DELETE NO ACTION ,

    CONSTRAINT fk_productID FOREIGN KEY (productoId)
        REFERENCES Productos (idProducto)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);
DROP TABLE detalleCompras;

SELECT * FROM detalleCompras;