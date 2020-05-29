import string
from mysql import connector

class Model:
    """
    *********************************************
    * A data model with MYSQL for a Cine DB *
    *********************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
    
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor() #Para consultas u operaciones en MySQL

    def close_db(self):
        self.cnx.close()

    """
    ********************
    *   Login methods  *
    ********************
    """

    def user_validation (self, correo, contrasenia, es_admin):
        try:
            if es_admin == '1':
                sql = 'SELECT * FROM Cliente WHERE correo = %s and contrasenia = %s'
            
            elif es_admin == '2':
                sql = 'SELECT * FROM Administrador WHERE correo = %s and contrasenia = %s'
            
            vals = (correo, contrasenia)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)


    """
    **************************
    * Administrador methods  *
    **************************
    """

    def create_admin(self, nombre, correo, contrasenia, telefono):
        try:
            sql = 'INSERT INTO Administrador (`nombre`, `correo`, `contrasenia`, `telefono`) VALUES (%s, %s, %s, %s)'
            vals = (nombre, correo, contrasenia, telefono)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_admin(self, id_admin):
        try:
            sql = 'SELECT ad.id_admin, ad.nombre, ad.correo, ad.telefono FROM Administrador ad WHERE ad.id_admin = %s'
            vals = (id_admin,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_admins(self): #Caution with large amount of data
        try:
            sql = 'SELECT ad.id_admin, ad.nombre, ad.correo, ad.telefono FROM Administrador ad'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_admin(self, fields, vals):
        try:
            sql = 'UPDATE Administrador SET '+','.join(fields)+' WHERE id_admin = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_admin(self, id_admin):
        try:
            sql = 'DELETE FROM Administrador WHERE id_admin = %s'
            vals = (id_admin,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ********************
    * Clientes methods  *
    ********************
    """

    def create_client(self, nombre, correo, contrasenia, telefono, fecha_nacimiento):
        try:
            sql = 'INSERT INTO Cliente (`nombre`, `correo`, `contrasenia`, `telefono`, `fecha_nacimiento`) VALUES (%s, %s, %s, %s, %s)'
            vals = (nombre, correo, contrasenia, telefono, fecha_nacimiento)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_client(self, id_cliente):
        try:
            sql = 'SELECT cl.id_cliente, cl.nombre, cl.correo, cl.telefono, cl.fecha_nacimiento FROM Cliente cl WHERE cl.id_cliente = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_clients(self): #Caution with large amount of data
        try:
            sql = 'SELECT cl.id_cliente, cl.nombre, cl.correo, cl.telefono, cl.fecha_nacimiento FROM Cliente cl'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def update_client(self, fields, vals):
        try:
            sql = 'UPDATE Cliente SET '+','.join(fields)+' WHERE id_cliente = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err


    def delete_client(self, id_cliente):
        try:
            sql = 'DELETE FROM Cliente WHERE id_cliente = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ********************
    * Pelicula methods  *
    ********************
    """

    def create_movie(self, titulo, nombre_director, genero, fecha_estreno, idioma, clasificacion, descripcion):
        try: 
            sql = 'INSERT INTO Pelicula (`titulo`,`nombre_director`,`genero`,`fecha_estreno`,`idioma`,`clasificacion`,`descripcion`) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            vals = (titulo, nombre_director, genero, fecha_estreno, idioma, clasificacion, descripcion)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_movie(self, id_pelicula):
        try:
            sql = 'SELECT * FROM Pelicula WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_movies(self):
        try:
            sql = 'SELECT * FROM Pelicula'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_movies_genre(self, genero):
        try:
            sql = 'SELECT * FROM Pelicula WHERE genero = %s'
            vals = (genero,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_movies_language(self, language):
        try:
            sql = 'SELECT * FROM Pelicula WHERE idioma = %s'
            vals = (language,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_movies_rating(self, rating):
        try:
            sql = 'SELECT * FROM Pelicula WHERE clasificacion = %s'
            vals = (rating,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_movie_title(self, titulo):
        try:
            sql = 'SELECT * FROM Pelicula WHERE titulo = %s'
            vals = (titulo,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def update_movie(self, fields, vals):
        try:
            sql = 'UPDATE Pelicula SET '+','.join(fields)+' WHERE id_pelicula = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_movie(self, id_pelicula):
        try:
            sql = 'DELETE FROM Pelicula WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***************************
    *      Salas methods      *
    ***************************
    """

    def create_hall(self, id_sala, num_asientos, tipo_sala):
        try: 
            sql = 'INSERT INTO Sala (`id_sala`, `num_asientos`, `tipo_sala`) VALUES (%s, %s, %s)'
            vals = (id_sala, num_asientos, tipo_sala)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_hall(self, id_sala):
        try:
            sql = 'SELECT * FROM Sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_halls(self):
        try:
            sql = 'SELECT * FROM Sala'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_halls_type(self, tipo_sala):
        try:
            sql = 'SELECT * FROM Sala WHERE tipo_sala = %s'
            vals = (tipo_sala,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_hall(self, fields, vals):
        try:
            sql = 'UPDATE Sala SET '+','.join(fields)+' WHERE id_sala = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_hall(self, id_sala):
        try:
            sql = 'DELETE FROM Sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***************************
    *     Asientos methods    *
    ***************************
    """

    def create_seat(self, denominacion):
        try: 
            sql = 'INSERT INTO Asiento (`denominacion`) VALUES (%s)'
            vals = (denominacion,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_seat(self, id_asiento):
        try:
            sql = 'SELECT * FROM Asiento WHERE id_asiento = %s'
            vals = (id_asiento,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_seats_denomination(self, denominacion):
        try:
            #sql = 'SELECT * FROM Asiento WHERE denominacion = %s'
            sql = 'SELECT * FROM Asiento WHERE denominacion LIKE %s'
            vals = (str(denominacion)+'%',)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_seats(self):
        try:
            sql = 'SELECT * FROM Asiento'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_seat(self, fields, vals):
        try:
            sql = 'UPDATE AsientosDisponibles SET '+','.join(fields)+' WHERE id_funcion = %s and id_asiento = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def change_seat_status(self, id_funcion, id_asiento, disponible):
        try:
            sql = 'UPDATE Asiento SET disponible = %s WHERE id_funcion = %s and id_asiento = %s'
            values = (disponible, id_funcion, id_asiento)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err


    def delete_seat(self, id_asiento):
        try:
            sql = 'DELETE FROM Asiento WHERE id_asiento = %s'
            vals = (id_asiento,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ***************************
    *     Funcion methods    *
    ***************************
    """
    def create_function(self, id_pelicula, fecha, hora, id_sala, precio):
        try:
            sql = 'INSERT INTO Funcion(`id_pelicula`, `fecha`, `hora`, `id_sala`, `precio`) VALUES(%s,%s,%s,%s,%s);'
            values = (id_pelicula, fecha, hora, id_sala, precio)
            #print(sql,values)
            self.cursor.execute(sql, values)
            lastid = self.cursor.lastrowid;
            #lastid = 12
            self.cnx.commit()
            return True, lastid
        except connector.Error as err:
            self.cnx.rollback()
            return(err, 0)  

    def read_a_function(self, id_funcion):
        try:
            sql = 'SELECT Funcion.id_funcion, Funcion.id_pelicula, Pelicula.titulo, Pelicula.idioma, Funcion.fecha, Funcion.hora, Funcion.id_sala, Sala.tipo_sala, Funcion.precio FROM Funcion JOIN Pelicula ON Pelicula.id_pelicula = Funcion.id_pelicula JOIN Sala ON Sala.id_sala = Funcion.id_sala and Funcion.id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_function_movie(self, pelicula_titulo):
        try:
            sql = 'SELECT Funcion.id_funcion, Funcion.id_pelicula, Pelicula.titulo, Pelicula.idioma, Funcion.fecha, Funcion.hora, Funcion.id_sala, Sala.tipo_sala, Funcion.precio FROM Funcion JOIN Pelicula ON Pelicula.id_pelicula = Funcion.id_pelicula JOIN Sala ON Sala.id_sala = Funcion.id_sala and Pelicula.titulo = %s'
            vals = (pelicula_titulo,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_function_date(self, fecha):
        try:
            sql = 'SELECT Funcion.id_funcion, Funcion.id_pelicula, Pelicula.titulo, Pelicula.idioma, Funcion.fecha, Funcion.hora, Funcion.id_sala, Sala.tipo_sala, Funcion.precio FROM Funcion JOIN Pelicula ON Pelicula.id_pelicula = Funcion.id_pelicula JOIN Sala ON Sala.id_sala = Funcion.id_sala and Funcion.fecha = %s'
            vals = (fecha,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err







    def read_all_functions(self):
        try:
            sql = 'SELECT Funcion.id_funcion, Funcion.id_pelicula, Pelicula.titulo, Pelicula.idioma, Funcion.fecha, Funcion.hora, Funcion.id_sala, Sala.tipo_sala, Funcion.precio FROM Funcion JOIN Pelicula ON Pelicula.id_pelicula = Funcion.id_pelicula JOIN Sala ON Sala.id_sala = Funcion.id_sala'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return (err)  

    def update_function(self, fields, vals):
        try:
            sql = 'UPDATE Funcion SET '+','.join(fields)+' WHERE id_funcion = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_function(self, id_funcion):
        try:
            sql = 'DELETE FROM Funcion WHERE id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ********************************
    * Asientos Disponibles methods *
    ********************************
    """

    def create_function_seat(self, id_funcion, id_asiento, disponible):
        try: 
            sql = 'INSERT INTO AsientosDisponibles (id_funcion, id_asiento, disponible) VALUES (%s, %s, %s)'
            vals = (int(id_funcion), id_asiento, disponible)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_function_seat(self, id_funcion, id_asiento):
        try:
            sql = 'SELECT * FROM AsientosDisponibles WHERE id_funcion = %s and id_asiento = %s'
            vals = (id_funcion, id_asiento)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_function_seats(self, id_funcion):
        try:
            sql = 'SELECT * FROM AsientosDisponibles WHERE id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def read_seats_row(self, id_funcion, fila):
        try:
            #sql = 'SELECT * FROM Asiento WHERE denominacion = %s'
            sql = 'SELECT * FROM AsientosDisponibles WHERE id_funcion = %s and id_asiento LIKE %s'
            vals = (id_funcion, str(fila)+'%')
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_function_seat(self, fields, vals):
        try:
            sql = 'UPDATE AsientosDisponibles SET '+','.join(fields)+' WHERE id_funcion = %s and id_asiento = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_function_seat(self, id_funcion, id_asiento):
        try:
            sql = 'DELETE FROM AsientosDisponibles WHERE id_funcion = %s and id_asiento = %s'
            vals = (id_funcion, id_asiento)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ***************************
    *      Ticket methods     *
    ***************************
    """

    def create_ticket(self, id_cliente, id_funcion, id_asiento):
        try: 
            sql = 'INSERT INTO Ticket (`id_cliente`, `id_funcion`, `id_asiento`) VALUES (%s, %s, %s)'
            vals = (id_cliente, id_funcion, id_asiento)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_ticket = self.cursor.lastrowid
            return id_ticket
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def create_purchase(self, id_cliente, fecha, hora, total):
        try:
            sql = 'INSERT INTO Compra (`id_cliente`, `fecha`, `hora`, `total`) VALUES (%s, %s, %s, %s)'
            vals = (id_cliente, fecha, hora, total)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_compra = self.cursor.lastrowid
            return id_compra
        except connector.Error as err:
            self.cnx.rollback()
            return err


    def read_a_ticket(self, id_ticket):
        try:
            sql = 'SELECT Ticket.id_ticket, Ticket.id_cliente, Ticket.id_funcion, Ticket.id_asiento, Pelicula.titulo, Funcion.Fecha, Funcion.Hora, Funcion.id_sala, Funcion.precio FROM Ticket JOIN Funcion ON Funcion.id_funcion = Ticket.id_funcion JOIN Pelicula ON Pelicula.id_pelicula = Funcion.id_pelicula JOIN AsientosDisponibles ON AsientosDisponibles.id_asiento = Ticket.id_asiento and Ticket.id_ticket = %s';
            vals = (id_ticket,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err

    def read_ticket_client(self, id_cliente):
        try:
            sql = 'SELECT Ticket.*, Asiento.denominacion, Pelicula.titulo, Funcion.Fecha, Funcion.Hora, Funcion.id_sala, Funcion.precio FROM Ticket JOIN Funcion ON Funcion.id_funcion = Ticket.id_funcion JOIN Pelicula ON Pelicula.id_pelicula = Funcion.id_pelicula JOIN Asiento ON Asiento.id_asiento = Ticket.id_asiento and Ticket.id_cliente = %s';
            vals = (id_cliente,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_tickets(self):
        try:
            sql = 'SELECT Ticket.*, Asiento.denominacion, Pelicula.titulo, Funcion.Fecha, Funcion.Hora, Funcion.id_sala, Funcion.precio FROM Ticket JOIN Funcion ON Funcion.id_funcion = Ticket.id_funcion JOIN Pelicula ON Pelicula.id_pelicula = Funcion.id_pelicula JOIN Asiento ON Asiento.id_asiento = Ticket.id_asiento';
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_ticket(self, fields, vals):
        try:
            sql = 'UPDATE Ticket SET '+','.join(fields)+' WHERE id_ticket = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_ticket(self, id_ticket):
        try:
            sql = 'DELETE FROM Ticket WHERE id_ticket = %s'
            vals = (id_ticket,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***************************
    *      Venta methods      *
    ***************************
    """

    def create_purchase(self, id_cliente, fecha, hora, total):
        try:
            sql = 'INSERT INTO Compra (`id_cliente`, `fecha`, `hora`, `total`) VALUES (%s, %s, %s, %s)'
            vals = (id_cliente, fecha, hora, total)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_compra = self.cursor.lastrowid
            return id_compra
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_purchase(self, id_compra):
        try:
            sql = 'SELECT * FROM Compra WHERE id_compra = %s'
            #sql = 'SELECT Compra.* FROM Compra JOIN DetallesCompra ON DetallesCompra.id_compra = Compra.id_compra JOIN Ticket ON DetallesCompra.id_ticket = Ticket.id_ticket and Compra.id_compra = %s'
            vals = (id_compra,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_purchases_client(self, id_cliente):
        try:
            sql = 'SELECT * FROM Compra WHERE id_cliente = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def read_purchases_date(self, id_cliente, fecha):
        try:
            sql = 'SELECT * FROM Compra WHERE id_cliente = %s and fecha = %s'
            vals = (id_cliente,fecha)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_purchases(self): #Caution with large amount of data
        try:
            sql = 'SELECT * FROM Compra'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_purchase(self, fields, vals):
        try:
            sql = 'UPDATE Compra SET '+','.join(fields)+' WHERE id_compra = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_purchase(self, id_compra):
        try:
            sql = 'DELETE FROM Compra WHERE id_compra = %s'
            vals = (id_compra,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ***************************
    *  DetallesCompra methods *
    ***************************
    """

    def create_purchase_details(self, id_compra, id_ticket):
        try: 
            sql = 'INSERT INTO DetallesCompra (`id_compra`, `id_ticket`) VALUES (%s, %s)'
            vals = (id_compra, id_ticket)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_purchase_details(self, id_compra, id_ticket):
        try:
            #sql = 'SELECT DetallesCompra.*, Ticket.id_cliente, Cliente.nombre, Ticket.id_funcion, Ticket.id_asiento, AsientoDisponibles.id_asiento FROM DetallesCompra JOIN Ticket ON Ticket.id_ticket = DetallesCompra.id_ticket JOIN Cliente ON Cliente.id_cliente = Ticket.id_cliente and DetallesCompra.id_compra = %s and DetallesCompra.id_ticket = %s'
            sql = 'SELECT * FROM DetallesCompra WHERE id_compra = %s and id_ticket = %s'
            #sql = 'SELECT * FROM DetallesCompra WHERE '
            vals = (id_compra, id_ticket)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_purchase_details(self, id_compra):
        try:
            #sql = 'SELECT DetallesCompra.*, Ticket.id_cliente, Cliente.nombre FROM DetallesCompra JOIN Ticket ON Ticket.id_ticket = DetallesCompra.id_ticket JOIN Cliente ON Cliente.id_cliente = Ticket.id_cliente and DetallesCompra.id_compra = %s'
            sql = 'SELECT * FROM DetallesCompra WHERE id_compra = %s'
            vals = (id_compra,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_purchase_details(self, fields, vals):
        try:
            sql = 'UPDATE DetallesCompra SET '+','.join(fields)+' WHERE id_compra = %s and id_ticket = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_purchase_details(self, id_compra, id_ticket):
        try:
            sql = 'DELETE FROM DetallesCompra WHERE id_compra = %s and id_ticket = %s'
            vals = (id_compra, id_ticket)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

