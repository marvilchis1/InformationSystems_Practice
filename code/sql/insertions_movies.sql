USE cine_db;

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






