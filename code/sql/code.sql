DROP DATABASE IF EXISTS cine_db;

CREATE DATABASE IF NOT EXISTS cine_db;

USE cine_db;

# Tabla 1
CREATE TABLE IF NOT EXISTS Administrador(
	id_admin INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(35) NOT NULL,
    correo VARCHAR(35) NOT NULL UNIQUE,
    contrasenia VARCHAR(25) NOT NULL,
    telefono VARCHAR(13),
    PRIMARY KEY (id_admin)
)ENGINE = INNODB;

# Tabla 2
CREATE TABLE IF NOT EXISTS Cliente(
	id_cliente INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(35) NOT NULL,
    correo VARCHAR(35) NOT NULL UNIQUE,
    contrasenia VARCHAR(25) NOT NULL,
    telefono VARCHAR(13),
    fecha_nacimiento DATE NOT NULL,
    PRIMARY KEY (id_cliente)
)ENGINE = INNODB;

# Tabla 3
CREATE TABLE IF NOT EXISTS Pelicula(
	id_pelicula INT NOT NULL AUTO_INCREMENT, 
    titulo VARCHAR(35) NOT NULL,
    nombre_director VARCHAR(45) NOT NULL,
    genero VARCHAR(30) NOT NULL,
    fecha_estreno DATE NOT NULL,
    idioma VARCHAR(30)NOT NULL,
    clasificacion ENUM('AA','A','B','B-15','C','D') NOT NULL,
    descripcion VARCHAR(250),
    PRIMARY KEY (id_pelicula)
)ENGINE = INNODB;

# Tabla 4
CREATE TABLE IF NOT EXISTS Sala(
	id_sala INT NOT NULL,
    num_asientos INT NOT NULL,
    tipo_sala ENUM('Normal', 'Premium', 'IMAX', '3DX', '4DX') NOT NULL,
	PRIMARY KEY (id_sala)
)ENGINE = INNODB;

# Tabla 5
CREATE TABLE IF NOT EXISTS Funcion(
	id_funcion INT NOT NULL AUTO_INCREMENT,
    id_pelicula INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    id_sala INT NOT NULL,
    precio FLOAT NOT NULL,
    PRIMARY KEY(id_funcion),
    CONSTRAINT fkpelicula_funcion FOREIGN KEY(id_pelicula)
		REFERENCES Pelicula(id_pelicula)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fksala_funcion FOREIGN KEY(id_sala)
		REFERENCES Sala(id_sala)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

# Tabla 6
CREATE TABLE IF NOT EXISTS AsientosDisponibles(
	id_funcion INT NOT NULL,
    id_asiento VARCHAR(3) NOT NULL,
    disponible BOOLEAN NOT NULL,
    PRIMARY KEY (id_funcion, id_asiento),
    CONSTRAINT fkfuncion_ad FOREIGN KEY(id_funcion)
		REFERENCES Funcion(id_funcion)
        ON DELETE CASCADE
        ON UPDATE CASCADE

)ENGINE = INNODB ;

# Tabla 7
CREATE TABLE IF NOT EXISTS Ticket(
	id_ticket INT NOT NULL AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_funcion INT NOT NULL,
    id_asiento VARCHAR(4) NOT NULL,
    PRIMARY KEY(id_ticket),
    UNIQUE KEY funcion_asiento (id_funcion, id_asiento),
    CONSTRAINT fkcliente_ticket FOREIGN KEY(id_cliente)
		REFERENCES Cliente(id_cliente)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fkfuncion_ticket FOREIGN KEY(id_funcion)
		REFERENCES Funcion(id_funcion)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

# Tabla 8
CREATE TABLE IF NOT EXISTS Compra( 
	id_compra INT NOT NULL AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL, 
    total FLOAT NOT NULL,
    PRIMARY KEY(id_compra),
    CONSTRAINT fkcliente_venta FOREIGN KEY(id_cliente)
		REFERENCES cliente(id_cliente)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

# Tabla 9
CREATE TABLE IF NOT EXISTS DetallesCompra(
	id_compra INT NOT NULL,
    id_ticket INT NOT NULL,
    #total FLOAT NOT NULL,
    PRIMARY KEY(id_compra, id_ticket),
    CONSTRAINT fkcompra_dt FOREIGN KEY(id_compra)
		REFERENCES Compra(id_compra)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fkticket_dt FOREIGN KEY(id_ticket)
		REFERENCES Ticket(id_ticket)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


#***************** Inserciones ******************
# 1
INSERT INTO Administrador (nombre, correo, contrasenia, telefono) VALUES ('Itachi Uchiha', 'ita@gmail.com', 'itachi12', '4711001909');
INSERT INTO Administrador (nombre, correo, contrasenia, telefono) VALUES ('Kakashi Hatake', 'kh@hotmail.com', 'kakashi12', '4719010909');
INSERT INTO Administrador (nombre, correo, contrasenia, telefono) VALUES ('Naruto Uzumaki', 'nu@gmail.com', 'naruto12', '4811987878');

# 2
INSERT INTO Cliente (nombre, correo, contrasenia, telefono, fecha_nacimiento) VALUES ('Sasuke Uchiha', 'sasuke@gmail.com', 'sasuke12', '4419810909', '1997/10/21');
INSERT INTO Cliente (nombre, correo, contrasenia, telefono, fecha_nacimiento) VALUES ('Shisui Uchiha', 'shisui@hotmail.com', 'shisui12', '4119871011', '1991/06/11');
INSERT INTO Cliente (nombre, correo, contrasenia, telefono, fecha_nacimiento) VALUES ('Shikamaru Nara', 'shikamaru@gmail.com', 'shikamaru12', '4719897777', '1999/02/18');

# 3
INSERT INTO Pelicula (titulo, nombre_director, genero, fecha_estreno, idioma, clasificacion, descripcion) VALUES ('Interstellar', 'Christopher Nolan','Ciencia Ficcion', '2014/10/26', 'Ingles (Subtitulada)', 'B', 'Pelicula de ciencia ficcion de 2014 dirigida por Christopher Nolan.');
INSERT INTO Pelicula (titulo, nombre_director, genero, fecha_estreno, idioma, clasificacion, descripcion) VALUES ('Naruto: Road To Ninja', 'Hayato Date','Anime', '2012/07/28', 'Japones (Subtitulada)', 'B', 'Novena pelicula de la serie Naruto y el sexto filme de Naruto Shippuden. ');
INSERT INTO Pelicula (titulo, nombre_director, genero, fecha_estreno, idioma, clasificacion, descripcion) VALUES ('Frozen 2', 'Jennifer Lee','Animada', '2019/11/07', 'Español', 'AA', 'Pelicula musical animada por computadora producida por Walt Disney');

# 4
INSERT INTO Sala (id_sala, num_asientos, tipo_sala) VALUES (1, 70, 'Normal');
INSERT INTO Sala (id_sala, num_asientos, tipo_sala) VALUES (2, 50, 'Premium');
INSERT INTO Sala (id_sala, num_asientos, tipo_sala) VALUES (3, 50, '3DX');
INSERT INTO Sala (id_sala, num_asientos, tipo_sala) VALUES (4, 50, '4DX');

