from model.model import Model
from view.view import View
from datetime import date
import string
from datetime import date
import time

#import sys
#import os



class Controller:
    """
    *******************************
    * A controller for a store DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.id_user = 0
        self.Filas = string.ascii_uppercase


    def start(self):
        #self.view.start()
        # aca debe de estar el login
        self.start_menu()
        #self.main_menu_admin()

    """
    ***********************
    * General controllers *
    ***********************
    """

    def start_menu(self):
        o = '0'
        while o != '3':
            #os.system('clear')
            self.view.start()
            self.view.start_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.login()
            elif o == '2':
                self.view.signin()
                self.create_client()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    """
    ************************************
    *  Inicio sesion  y registro       *
    ************************************
    """

    def ask_login(self):
        self.view.ask('\nCorreo: ')
        email = input()
        self.view.ask('Contraseña ')
        password = input()
        return [email, password]

    def login(self):
        answer = 0
        self.view.login()
        print('\n1.- Soy cliente')
        print('2.- Soy administrador')
        print('3.- Regresar')
        self.view.option('3')
        answer = input()
        
        if answer == '3':
            return
        elif answer != '1' and answer != '2':
            self.view.error('Opcion no valida')
            return
        
        self.view.login()
        email, password = self.ask_login()
        user = self.model.user_validation(email, password, answer)
        
        if type(user) == tuple:
            self.id_user = user[0]
            self.view.welcome_user(user[1]);
        else:
            if user == None:
                self.view.error('El correo o la contraseña son incorrectos')
            else: 
                self.view.error('Problema al leer el usuario. Revisa.')
            return
        
        if answer == '1':
            self.main_menu_client()
        elif answer == '2':
            self.main_menu_admin()
        return user


    def main_menu_admin(self):
        o = '0'
        while o != '6':
            self.view.main_menu_admin()
            self.view.option('6')
            o = input()
            if o == '1':
                self.halls_menu()
            elif o == '2':
                self.seats_menu()
            elif o == '3':
                self.movies_menu()
            elif o == '4':
                self.functions_menu()
            elif o == '5':
                self.admins_menu()
            elif o == '6':
                self.view.signoff()
            else:
                self.view.not_valid_option()
        return

    def main_menu_client(self):
        o = '0'
        while o != '4':
            self.view.main_menu_client()
            self.view.option('4')
            o = input()
            if o == '1':
                self.tickets_menu()
            elif o == '2':
                self.functions_cmenu()
            elif o == '3':
                self.client_menu()
            elif o == '4':
                self.view.signoff()
                return
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals

    """
    ****************************
    * Controllers for Salas *
    ****************************
    """

    def halls_menu(self):
        o = '0'
        while o != '7':
            self.view.halls_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_hall()
            elif o == '2':
                self.read_a_hall()
            elif o == '3':
                self.read_all_halls()
            elif o == '4':
                self.read_halls_type()
            elif o == '5':
                self.update_hall()
            elif o == '6':
                self.delete_hall()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_hall(self):
        self.view.ask('Num. de asientos: ')
        num_asientos = input()
        self.view.ask('Tipo de Sala: ')
        tipo_sala = input()
        return [num_asientos,tipo_sala]

    def create_hall(self):
        self.view.ask('ID Sala: ')
        id_sala = input()
        self.view.ask('Numero de asientos: ')
        num_asientos = input()
        self.view.ask('Tipo de sala: ')
        tipo_sala = input()
        out = self.model.create_hall(id_sala, num_asientos, tipo_sala)
        if out == True:
            self.view.ok('La sala', 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('La sala ya esta registrada')
            else:
                self.view.error('No se pudo agregar la sala.')
        return

    def read_a_hall(self):
        self.view.ask('ID Sala: ')
        id_sala = input()
        sala = self.model.read_a_hall(id_sala)
        if type(sala) == tuple:
            self.view.show_hall_header(' Datos de la sala '+id_sala+' ')
            self.view.show_a_hall(sala)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if sala == None:
                self.view.error('La sala NO existe')
            else:
                self.view.error('Problema para leer la sala')
        return

    def read_all_halls(self):
        salas = self.model.read_all_halls()
        if type(salas) == list:
            self.view.show_hall_header(' Salas ')
            for sala in salas:
                self.view.show_a_hall(sala)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            self.view.error('Error al leer todas los salas')
        return

    def read_halls_type(self):
        self.view.ask('Tipo de sala: ')
        tipo_sala = input()
        salas = self.model.read_halls_type(tipo_sala)
        if type(salas) == list:
            self.view.show_hall_header(' Salas de tipo: '+tipo_sala+' ')
            for sala in salas:
                self.view.show_a_hall(sala)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            self.view.error('Error al leer las salas')
        return

    def update_hall(self):
        self.view.ask('ID Sala a modificar: ')
        id_sala = input()
        sala = self.model.read_a_hall(id_sala)
        if type(sala) == tuple:
            self.view.show_hall_header(' Datos de la sala '+id_sala+' ')
            self.view.show_a_hall(sala)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if sala == None:
                self.view.error('La sala NO existe')
            else:
                self.view.error('Error al leer la sala.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_hall()
        fields, vals = self.update_lists(['num_asientos','tipo_sala'], whole_vals)
        vals.append(id_sala)
        vals = tuple(vals)
        out = self.model.update_hall(fields, vals)
        if out == True:
            self.view.ok('La sala '+str(id_sala), 'actualizo')
        else:
            self.view.error('No se pudo actualizar la sala')
        return

    def delete_hall(self):
        self.view.ask('ID Sala: ')
        id_sala = input()
        count = self.model.delete_hall(id_sala)
        if count != 0:
            self.view.ok('La sala '+ str(id_sala), 'borro')
        else:
            if count == 0:
                self.view.error('La sala NO existe')
            else:
                self.view.error('Error al borrar la sala.')
        return

    """
    ****************************
    * Controllers for Asientos *
    ****************************
    """

    def seats_menu(self):
        o = '0'
        while o != '7':
            self.view.seats_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_seat()
            elif o == '2':
                self.read_a_seat()
            elif o == '3':
                self.read_all_seats()
            elif o == '4':
                self.read_seats_row()
            elif o == '5':
                self.update_seat()
            elif o == '6':
                self.delete_seat()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_seat(self):

        self.view.ask('ID Funcion: ')
        id_funcion = input()
        self.view.ask('ID Asiento: ')
        id_asiento = input()
        self.view.ask('¿Disponible? (S/N): ')
        disponible = input()
        if disponible == 'S':
            disponible = '1'
        else: 
            disponible = '0'
        return [id_funcion, id_asiento, disponible]

    def create_seat(self):
        id_funcion, id_asiento, disponible = self.ask_seat()

        out = self.model.create_function_seat(id_funcion, id_asiento, disponible)
        if out == True:
            self.view.ok('El asiento', 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('El asiento ya esta registrada')
            else:
                self.view.error('No se pudo agregar el asiento.')
        return

    def read_a_seat(self):
        self.view.ask('ID Funcion: ')
        id_funcion = input()
        self.view.ask('ID Asiento: ')
        id_asiento = input()

        asiento = self.model.read_a_function_seat(id_funcion, id_asiento)
        if type(asiento) == tuple:
            self.view.show_seat_header(' Datos del asiento '+id_asiento+' ')
            self.view.show_a_seat(asiento)
            self.view.show_seat_midder()
            self.view.show_seat_footer()
        else:
            if asiento == None:
                self.view.error('El asiento NO existe')
            else:
                self.view.error('Problema para leer el asiento')
        return

    def read_all_seats(self):
        self.view.ask('ID Funcion: ')
        id_funcion = input()
        asientos = self.model.read_all_function_seats(id_funcion)
        #print('Tamanio: ' + str(len(asientos) ) )
        if type(asientos) == list:
            self.view.show_all_seats_header(' Asientos de la funcion '+str(id_funcion)+' ')
            for asiento in asientos:
                self.view.show_all_seats(asiento)
            self.view.show_all_seats_midder()
            self.view.show_all_seats_footer()
        else:
            self.view.error('Error al leer todos los asientos')
        return

    def read_all_seats_input(self, id_funcion):
        #self.view.ask('ID Funcion: ')
        #id_funcion = input()
        asientos = self.model.read_all_function_seats(id_funcion)
        #print('Tamanio: ' + str(len(asientos) ) )
        if type(asientos) == list:
            self.view.show_all_seats_header_input(' Asientos de la funcion '+str(id_funcion)+' ')
            cont = 1
            self.view.print_screen_cinema()
            for asiento in asientos:
                self.view.show_all_seats_map(asiento)
                #cont = cont + 1
                if cont == 10:
                    print('\n')
                    cont = 0
                cont = cont + 1
            self.view.show_all_seats_midder()
            self.view.show_all_seats_footer()
        else:
            self.view.error('Error al leer todos los asientos')
        return

    def read_seats_row(self):
        self.view.ask('Funcion: ')
        id_funcion = input()
        self.view.ask('Fila: ')
        fila = input()
        asientos = self.model.read_seats_row(id_funcion, fila)
        if type(asientos) == list:
            self.view.show_all_seats_header(' Fila: '+fila+' en Funcion: '+id_funcion)
            for asiento in asientos:
                self.view.show_all_seats(asiento)
            self.view.show_all_seats_midder()
            self.view.show_all_seats_footer()
        else:
            self.view.error('Error al leer los asientos')
        return

    def update_seat(self):
        self.view.ask('ID Funcion: ')
        id_funcion = input()
        self.view.ask('ID Asiento a modificar: ')
        id_asiento = input()
        asiento = self.model.read_a_function_seat(id_funcion, id_asiento)
        if type(asiento) == tuple:
            self.view.show_seat_header(' Datos del asiento '+id_asiento+' ')
            self.view.show_a_seat(asiento)
            self.view.show_seat_midder()
            self.view.show_seat_footer()
        else:
            if asiento == None:
                self.view.error('El asiento NO existe')
            else:
                self.view.error('Error al leer el asiento.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        #whole_vals = self.ask_seat()

        self.view.ask('¿Disponible? (S/N): ')
        disponible = input()
        if disponible == 'S':
            disponible = '1'
        else: 
            disponible = '0'
        whole_vals = disponible

        fields, vals = self.update_lists(['disponible = %s'], whole_vals)
        vals.append(id_asiento)
        vals.append(id_funcion)
        vals = tuple(vals)
        out = self.model.update_function_seat(fields, vals)
        if out == True:
            self.view.ok('El asiento '+id_asiento+' de la funcion '+id_funcion, 'actualizo')
        else:
            self.view.error('No se pudo actualizar el asiento')
        return




    def delete_seat(self):

        self.view.ask('ID Funcion: ')
        id_funcion = input()
        self.view.ask('ID Asiento: ')
        id_asiento = input()
        count = self.model.delete_function_seat(id_funcion, id_asiento)
        if count != 0:
            self.view.ok('El asiento '+id_asiento+' de la funcion '+id_funcion, 'borro')
        else:
            if count == 0:
                self.view.error('El asiento NO existe')
            else:
                self.view.error('Error al borrar el asiento.')
        return

    """
    ****************************
    * Controllers for peliculas *
    ****************************
    """

    def movies_menu(self):
        o = '0'
        while o != '10':
            self.view.movies_menu()
            self.view.option('10')
            o = input()
            if o == '1':
                self.create_movie()
            elif o == '2':
                self.read_a_movie()
            elif o == '3':
                self.read_movie_name()
            elif o == '4':
                self.read_all_movies()
            elif o == '5':
                self.read_movies_genre()
            elif o == '6':
                self.read_movies_language()
            elif o == '7':
                self.read_movies_rating()
            elif o == '8':
                self.update_movie()
            elif o == '9':
                self.delete_movie()
            elif o == '10':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_movie(self):
        self.view.ask('Titulo: ')
        titulo = input()
        self.view.ask('Nombre del director: ')
        nombre_director = input()
        self.view.ask('Genero: ')
        genero = input()
        self.view.ask('Fecha de estreno AAAA/MM/DD: ')
        fecha = input()
        self.view.ask('Idioma: ')
        idioma = input()
        self.view.ask('Clasificacion: ')
        clasificacion = input()
        self.view.ask('Descripcion: ')
        descripcion = input()
        return [titulo, nombre_director, genero, fecha, idioma, clasificacion, descripcion]

    def create_movie(self):
        titulo, director, genero, fecha, idioma, clasif, descr = self.ask_movie()
        out = self.model.create_movie(titulo, director, genero, fecha, idioma, clasif, descr)
        if out == True:
            self.view.ok(titulo, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('El asiento ya esta registrada')
            else:
                self.view.error('No se pudo agregar la pelicula. Revisa.')
        return

    def read_a_movie(self):
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        pelicula = self.model.read_a_movie(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_movie_header(' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_movie(pelicula)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if pelicula == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer la informacion de la pelicula. Revisa.')
        return



    def read_movie_name(self):
        self.view.ask('Titulo de Pelicula: ')
        titulo = input()
        pelicula = self.model.read_movie_title(titulo)
        if type(pelicula) == tuple:
            self.view.show_movie_header(' Datos de la pelicula: '+titulo+' ')
            self.view.show_a_movie(pelicula)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if pelicula == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer la informacion de la pelicula. Revisa.')
        return



    def read_all_movies(self):
        peliculas = self.model.read_all_movies()
        if type(peliculas) == list:
            self.view.show_movie_header(' Todas las peliculas ')
            for pelicula in peliculas:
                self.view.show_a_movie(pelicula)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Problema al leer la informacion de las peliculas. Revisa.')
        return

    def read_movies_genre(self):
        self.view.ask('Genero: ')
        genero = input()
        peliculas = self.model.read_movies_genre(genero)
        if type(peliculas) == list:
            self.view.show_movie_header(' Peliculas del genero '+genero+' ')
            for pelicula in peliculas:
                self.view.show_a_movie(pelicula)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Problema al leer la informacion de las peliculas. Revisa.')
        return

    def read_movies_language(self):
        self.view.ask('Idioma: ')
        language = input()
        peliculas = self.model.read_movies_language(language)
        if type(peliculas) == list:
            self.view.show_movie_header(' Peliculas en: '+language+' ')
            for pelicula in peliculas:
                self.view.show_a_movie(pelicula)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Probema al leer la informacion de las peliculas. Revisa.')
        return

    def read_movies_rating(self):
        self.view.ask('Clasificacion: ')
        clasif = input()
        peliculas = self.model.read_movies_rating(clasif)
        if type(peliculas) == list:
            self.view.show_movie_header(' Peliculas con clasificacion: '+clasif+' ')
            for pelicula in peliculas:
                self.view.show_a_movie(pelicula)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Problema al leer la informacion de las peliculas. Revisa.')
        return

    def update_movie(self):
        self.view.ask('ID de pelicula a modificar: ')
        id_pelicula = input()
        pelicula = self.model.read_a_movie(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_movie_header(' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_movie(pelicula)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if pelicula == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer la pelicula. Revisa.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_movie()
        fields, vals = self.update_lists(['titulo','nombre_director','genero','fecha_estreno', 'idioma', 'clasificacion', 'descripcion'], whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_movie(fields, vals)
        if out == True:
            self.view.ok(id_pelicula, 'actualizo')
        else:
            self.view.error('No se pudo actualizar la informacion de la pelicula. Revisa.')
        return

    def delete_movie(self):
        self.view.ask('Id Pelicula a borrar: ')
        id_pelicula = input()
        count = self.model.delete_movie(id_pelicula)
        if count != 0:
            self.view.ok(id_pelicula, 'borro')
        else:
            if count == 0:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al eliminar la pelicula. Revisa.')
        return

    """
    ****************************
    * Controllers for funciones *
    ****************************
    """

    def functions_menu(self):
        o = '0'
        while o != '8':
            self.view.functions_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_function()
            elif o == '2':
                self.read_a_function('admin')
            elif o == '3':
                self.read_all_functions('admin')
            elif o == '4':
                self.read_functions_movie('admin')
            elif o == '5':
                self.read_functions_date('admin')
            elif o == '6':
                self.update_function()
            elif o == '7':
                self.delete_function()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    def functions_cmenu(self):
        o = '0'
        while o != '4':
            self.view.functions_cmenu()
            self.view.option('4')
            o = input()
            if o == '1':
                self.read_today_functions('client')
            elif o == '2':
                self.read_functions_movie('client')
            elif o == '3':
                self.read_functions_date('client')
            elif o == '4':
                return
            else:
                self.view.not_valid_option()
        return


    def ask_function(self):
        self.read_all_movies()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        self.view.ask('Fecha AAAA/MM/DD: ')
        fecha = input()
        self.view.ask('Hora HH:MM:SS: ')
        hora = input()
        self.view.ask('ID Sala: ')
        id_sala = input()
        self.view.ask('Precio: ')
        precio = input()
        return [id_pelicula, fecha, hora, id_sala, precio]

    def create_function(self):
        id_pelicula, fecha, hora, id_sala, precio = self.ask_function()
        out, lastid_funcion = self.model.create_function(id_pelicula, fecha, hora, id_sala, precio)
        
        #print('El ultimo id_funcion fue: ' + str(lastid_funcion) )
        if out == True:
            self.view.ok('La funcion '+str(lastid_funcion)+' asociada a la pelicula '+str(id_pelicula), 'agrego')
            
            # Se obtienen el numero de asientos de la sala seleccionada
            # en my_hall[1] esta el numero de asientos
            my_hall = self.model.read_a_hall(id_sala)
            num_asientos = my_hall[1]
            #print('El numero de asientos es: '+ str(my_hall[1]) )
            num_filas = int(my_hall[1]) / 10; # por defecto cada fila tiene 10 asientos
            num_filas = int(num_filas)
            #print('El numero de filas es: '+ str(num_filas) )

            # Se asignan los asientos disponibles a dicha sala pertenenciente a la funcion recien creada
            for i in range(0, num_filas):
                letter = self.Filas[i]
                for j in range(1, 11):
                    if j == 10:
                        id_asiento = letter + str(j)
                    else:
                        id_asiento = letter + '0' +str(j)
                    self.model.create_function_seat(int(lastid_funcion), id_asiento, True) # True = asiento disponible

        else:
            if out.errno == 1062:
                self.view.error('La funcion ya esta registrada')
            else:
                self.view.error('No se pudo agregar la funcion. Revisa.')
        return

    def read_a_function(self, tipo_usuario):
        self.view.ask('ID Funcion: ')
        id_funcion = input()
        funcion = self.model.read_a_function(id_funcion)
        if type(funcion) == tuple:
            if tipo_usuario == 'admin':
                self.view.show_function_header(' Datos de la funcion '+id_funcion+' ')
                self.view.show_a_function(funcion)
                self.view.show_function_midder()
                self.view.show_function_footer()
            else:
                self.view.show_function_cheader(' Datos de la funcion '+id_funcion+' ')
                self.view.show_a_cfunction(funcion)
                self.view.show_function_cmidder()
                self.view.show_function_cfooter()
        else:
            if funcion == None:
                self.view.error('La funcion no existe')
            else:
                self.view.error('Problema al leer la informacion de la funcion. Intente nuevamente.')
        return

    def read_all_functions(self, tipo_usuario):
        funciones = self.model.read_all_functions()
        if type(funciones) == list:
            if tipo_usuario == 'admin':
                self.view.show_function_header(' Todas las funciones ')
            else:
                self.view.show_function_cheader(' Funciones disponibles ')
            for funcion in funciones:
                if tipo_usuario == 'admin':
                    self.view.show_a_function(funcion)
                    self.view.show_function_midder()
                else:
                    self.view.show_a_cfunction(funcion)
                    self.view.show_function_cmidder()
        else:
            self.view.error('Problema al leer la informacion de las funciones. Intenta nuevamente.')
        return

    def read_functions_movie(self, tipo_usuario):
        self.view.ask('Titulo de pelicula: ')
        titulo = input()

        funciones = self.model.read_function_movie(titulo)
        if type(funciones) == list and len(funciones) > 0:
            #self.view.show_function_header(' Funciones de la pelicula: '+titulo+' ')
            if tipo_usuario == 'admin':
                self.view.show_function_header(' Funciones de la pelicula: '+titulo+' ')
            else:
                self.view.show_function_cheader(' Funciones de la pelicula: '+titulo+' ')            
            
            for funcion in funciones:
                if tipo_usuario == 'admin':
                    self.view.show_a_function(funcion)
                    self.view.show_function_midder()
                else:
                    self.view.show_a_cfunction(funcion)
                    self.view.show_function_cmidder()
        else:
            self.view.error('Problema al leer la informacion de las funciones. Intente nuevamente')
        return

    def read_functions_date(self, tipo_usuario):
        self.view.ask('Fecha AAAA/MM/DD: ')
        fecha = input()
        funciones = self.model.read_function_date(fecha)
        if type(funciones) == list and len(funciones) > 0:
            #self.view.show_function_header(' Funciones disponibles en el dia: ('+fecha+') ')

            if tipo_usuario == 'admin':
                self.view.show_function_header(' Funciones disponibles en el dia: ('+fecha+') ')
            else:
                self.view.show_function_cheader(' Funciones disponibles en el dia: ('+fecha+') ') 

            for funcion in funciones:
                if tipo_usuario == 'admin':
                    self.view.show_a_function(funcion)
                    self.view.show_function_midder()
                else:
                    self.view.show_a_cfunction(funcion)
                    self.view.show_function_cmidder()
        else:
            self.view.error('Problema al leer la informacion de las peliculas. Intente nuevamente.')
        return



    def read_today_functions(self, tipo_usuario):
        hoy = date.today()
        fecha = hoy.strftime('%y-%m-%d')

        funciones = self.model.read_function_date(fecha)
        if type(funciones) == list and len(funciones) > 0:
            if tipo_usuario == 'admin':
                self.view.show_function_header(' Funciones disponibles en el dia: ('+fecha+') ')
            else:
                self.view.show_function_cheader(' Funciones disponibles en el dia: ('+fecha+') ') 

            for funcion in funciones:
                if tipo_usuario == 'admin':
                    self.view.show_a_function(funcion)
                    self.view.show_function_midder()
                else:
                    self.view.show_a_cfunction(funcion)
                    self.view.show_function_cmidder()
        else:
            self.view.error('Problema al leer la informacion de las peliculas. Intente nuevamente.')
        return




    def update_function(self):
        self.view.ask('ID de funcion a modificar: ')
        id_funcion = input()
        funcion = self.model.read_a_function(id_funcion)
        if type(funcion) == tuple:
            self.view.show_function_header(' Datos de la funcion '+id_funcion+' ')
            self.view.show_a_function(funcion)
            self.view.show_function_midder()
            self.view.show_function_footer()
        else:
            if funcion == None:
                self.view.error('La funcion no existe')
            else:
                self.view.error('Problema al leer la funcion. Revisa.')
            return
        whole_vals = self.ask_function()
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        #whole_vals = self.ask_function()
        fields, vals = self.update_lists(['id_pelicula','fecha','hora','id_sala', 'precio'], whole_vals)
        vals.append(id_funcion)
        vals = tuple(vals)
        out = self.model.update_function(fields, vals)
        if out == True:
            self.view.ok(id_funcion, 'actualizo')
        else:
            self.view.error('No se pudo actualizar la informacion de la funcion. Revisa.')
        return

    def delete_function(self):
        self.view.ask('ID de funcion a borrar: ')
        id_funcion = input()
        count = self.model.delete_function(id_funcion)
        if count != 0:
            self.view.ok(id_funcion, 'borro')
        else:
            if count == 0:
                self.view.error('La funcion no existe')
            else:
                self.view.error('Problema al eliminar la funcion. Revisa.')
        return



    """
    ***********************************
    * Controllers for administradores *
    ***********************************
    """

    def admins_menu(self):
        o = '0'
        while o != '6':
            self.view.admin_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_admin()
            elif o == '2':
                self.read_a_admin()
            elif o == '3':
                self.read_all_admins()
            elif o == '4':
                self.update_admin()
            elif o == '5':
                self.delete_admin()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_admin(self):
        self.view.ask('Nombre completo: ')
        nombre = input()
        self.view.ask('Correo electronico: ')
        correo = input()
        self.view.ask('Contraseña: ')
        contrasenia = input()
        self.view.ask('Telefono: ')
        telefono = input()

        return [nombre, correo, contrasenia, telefono]

    def create_admin(self):
        nombre, correo, contrasenia, telefono = self.ask_admin()
        out = self.model.create_admin(nombre, correo, contrasenia, telefono)
        if out == True:
            self.view.ok(nombre, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('El usuario ya esta registrado')
            else:
                self.view.error('No se pudo agregar al usuario. Revisa.')
        return

    def read_a_admin(self):
        self.view.ask('ID Admin: ')
        id_admin = input()
        admin = self.model.read_a_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header(' Datos del administrador '+id_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('El administrador no existe')
            else:
                self.view.error('Problema al leer la informacion del administrador. Revisa.')
        return

    def read_all_admins(self):
        admins = self.model.read_all_admins()
        if type(admins) == list:
            self.view.show_admin_header(' Todos los administradores ')
            for admin in admins:
                self.view.show_a_admin(admin)
                self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('Problema al leer la informacion de los administradores. Revisa.')
        return

    def update_admin(self):
        #self.view.ask('ID de admin a modificar: ')
        id_admin = self.id_user;
        admin = self.model.read_a_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header(' Datos del administrador '+str(id_admin)+' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('El administrador no existe')
            else:
                self.view.error('Problema al leer al administrador. Revisa.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_admin()
        fields, vals = self.update_lists(['nombre','correo','contrasenia','telefono'], whole_vals)
        vals.append(id_admin)
        vals = tuple(vals)
        out = self.model.update_admin(fields, vals)
        if out == True:
            self.view.ok('El admininistrador '+str(id_admin), 'actualizo')
        else:
            self.view.error('No se pudo actualizar la informacion del administrador. Revisa.')
        return

    def delete_admin(self):
        self.view.ask('Id Admin a borrar: ')
        id_administrador = input()
        count = self.model.delete_admin(int(id_administrador))
        if count != 0:
            self.view.ok('El administrador '+id_administrador, 'borro')
        else:
            if count == 0:
                self.view.error('El administrador no existe')
            else:
                self.view.error('Problema al eliminar al administrador. Revisa.')
        return




    """
    ***********************************
    * Controllers for clientes *
    ***********************************
    """

    def client_menu(self):
        o = '0'
        while o != '4':
            if self.id_user == 0:
                self.view.end()
                return

            self.view.client_menu()
            self.view.option('4')
            o = input()
            if o == '1':
                self.read_a_client()
            elif o == '2':
                self.update_client()
            elif o == '3':
                self.delete_client()
            elif o == '4':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_client(self):
        print('\nIngrese los siguientes datos: ')
        self.view.ask('\nNombre completo: ')
        nombre = input()
        self.view.ask('Correo electronico: ')
        correo = input()
        self.view.ask('Contraseña: ')
        contrasenia = input()
        self.view.ask('Telefono: ')
        telefono = input()
        self.view.ask('Fecha de nacimiento AAAA/MM/DD: ')
        fecha_nacimiento = input()

        return [nombre, correo, contrasenia, telefono, fecha_nacimiento]

    def create_client(self):
        nombre, correo, contrasenia, telefono, fecha_nacimiento = self.ask_client()
        out = self.model.create_client(nombre, correo, contrasenia, telefono, fecha_nacimiento)
        if out == True:
            self.view.ok(nombre, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('El usuario ya esta registrado')
            else:
                self.view.error('No se pudo agregar al usuario. Revisa.')
        return

    def read_a_client(self):
        #self.view.ask('ID Cliente: ')
        #id_cliente = input()
        id_cliente = self.id_user
        cliente = self.model.read_a_client(id_cliente)
        if type(cliente) == tuple:
            self.view.show_client_header(' Datos del cliente '+str(id_cliente)+' ')
            self.view.show_a_client(cliente)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if cliente == None:
                self.view.error('El cliente no existe')
            else:
                self.view.error('Problema al leer la informacion del cliente. Intente de nuevo.')
        return

    def read_all_clients(self):
        clientes = self.model.read_all_clients()
        if type(clientes) == list:
            self.view.show_client_header(' Todos los clientes ')
            for cliente in clientes:
                self.view.show_a_client(cliente)
                self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            self.view.error('Problema al leer la informacion de los clientes. Revisa.')
        return

    def update_client(self):
        #self.view.ask('ID de admin a modificar: ')
        id_cliente = self.id_user;
        cliente = self.model.read_a_client(id_cliente)
        if type(cliente) == tuple:
            self.view.show_client_header(' Datos del cliente '+str(id_cliente)+' ')
            self.view.show_a_client(cliente)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if cliente == None:
                self.view.error('El cliente no existe')
            else:
                self.view.error('Problema al leer la informacion del cliente. Intente de nuevo.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_client()
        fields, vals = self.update_lists(['nombre','correo','contrasenia','telefono', 'fecha_nacimiento'], whole_vals)
        vals.append(id_cliente)
        vals = tuple(vals)
        out = self.model.update_client(fields, vals)
        if out == True:
            self.view.ok('El cliente '+str(id_cliente), 'actualizo')
        else:
            self.view.error('No se pudo actualizar la informacion del cliente. Intente de nuevo.')
        return

    def delete_client(self):
        #self.view.ask('ID cliente a borrar: ')
        print('Confirme su identidad: ')
        email, password = self.ask_login()
        user = self.model.user_validation(email, password, '1')

        if user == None:
            self.view.error('El correo o la contraseña son incorrectos')
            return

        id_cliente = self.id_user
        count = self.model.delete_client(id_cliente)
        if count != 0:
            self.view.ok('El cliente '+str(id_cliente), 'borro')
            self.id_user = 0
        else:
            if count == 0:
                self.view.error('El cliente no existe')
            else:
                self.view.error('Problema al eliminar al cliente. Revisa.')
        
        return 









    """
    ************************************
    *      Controllers for ticket      *
    ************************************
    """


    def ask_ticket(self):
        print('\nIngrese los siguientes datos: ')
        self.view.ask('\nNombre completo: ')
        nombre = input()
        self.view.ask('Correo electronico: ')
        correo = input()
        self.view.ask('Contraseña: ')
        contrasenia = input()
        self.view.ask('Telefono: ')
        telefono = input()
        self.view.ask('Fecha de nacimiento AAAA/MM/DD: ')
        fecha_nacimiento = input()

        return [nombre, correo, contrasenia, telefono, fecha_nacimiento]

#    def create_ticket(self, id_funcion):


    def read_a_ticket(self, id_ticket = ' '):
        if id_ticket == ' ':
            self.view.ask('ID Ticket: ')
            id_cliente = input()
        
        boleto = self.model.read_a_ticket(id_ticket)
        if type(boleto) == tuple:
            self.view.show_ticket_header(' ID Ticket '+str(id_ticket)+' ')
            self.view.show_a_ticket(boleto)
        else:
            if boleto == None:
                self.view.error('El ticket no existe')
            else:
                self.view.error('Problema al leer la informacion del ticket. Intente de nuevo.')
        return 

    def read_ticket_table(self, id_ticket = ' '):
        if id_ticket == ' ':
            self.view.ask('ID Ticket: ')
            id_cliente = input()

        boleto = self.model.read_a_ticket(id_ticket)
        
        if type(boleto) == tuple:
            self.view.show_a_ticket_table(boleto)
            #self.view.show_ticket_table_footer()
        else:
            if boleto == None:
                self.view.error('El ticket no existe')
            else:
                self.view.error('Problema al leer la informacion del ticket. Intente de nuevo.')
        return 




    """
    ************************************
    * Controllers for compras (ventas) *
    ************************************
    """

    def tickets_menu(self):
        o = '0'
        while o != '3':
            self.view.tickets_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.create_purchase()
            elif o == '2':
                self.read_a_purchase()
            #elif o == '3':
            #    self.read_purchases_client()
            #elif o == '4':
            #    self.read_purchases_date()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return

    def create_purchase(self):
        # Se obtiene el id del cliente
        id_cliente = self.id_user
        # Se obtiene la fecha y hora actual
        hoy = date.today()
        fecha = hoy.strftime('%y-%m-%d')
        hora = time.strftime("%H:%M:%S")
        total = 0.0
        # Se crea una entidad compra provisional, con el total inicializado en cero
        #id_compra = self.model.create_purchase(id_cliente, fecha, hora, total)
        # Se obtiene el id_funcion
        self.view.functions_cmenu()
        self.view.option('4')
        o = input()
        if o == '1':
                self.read_today_functions('client')
        elif o == '2':
                self.read_functions_movie('client')
        elif o == '3':
                self.read_functions_date('client')
        else:
            return
        # Se crea una entidad compra provisional, con el total inicializado en cero
        id_compra = self.model.create_purchase(id_cliente, fecha, hora, total)

        # Si se creo correctamente la entidad Compra
        if type(id_compra) == int:

            resp = ' '
            while resp != 'N':
                self.view.msg('\n\n\n---- Compra uno o mas tickets (deje el cuadro funcion en vacio para salir) ---\n')
                id_funcion, precio_ticket = self.create_purchase_details(id_compra)
                total = total + precio_ticket
                print('¿Desea comprar mas boletos (S/N)?')
                resp = input()
            self.model.update_purchase(('total = %s',),(total, id_compra))
            self.read_a_purchase(id_compra)
    
        else:
            self.view.error('Lo sentimos, hubo un error en la compra. Intentelo nuevamente.')
        return


    def read_a_purchase(self, id_compra = ' '):
        if id_compra == ' ': 
            print('\n')
            self.view.ask('ID Compra: ')
            id_compra = input()

        compra = self.model.read_a_purchase(id_compra)
        
        if type(compra) == tuple:
            
            purchase_details = self.model.read_purchase_details(id_compra)
            
            if type(purchase_details) != list and purchase_details != None:
                self.view.error('Problema al leer los datos de la compra. Intentelo nuevamente.')
            else:
                self.view.show_purchase_header(' Datos de la compra '+str(id_compra)+' ')
                self.view.show_purchase(compra)
                self.view.show_ticket_table_header(' Tickets de la compra: '+ str(id_compra) + ' ')
                
                for purchase_detail in purchase_details:
                    id_ticket = purchase_detail[1]               
                    self.read_ticket_table(id_ticket)
                    self.view.show_ticket_table_midder()
                
                self.view.show_ticket_table_footer()
                return compra
        else:
            if compra == None:
                self.view.error('La compra no existe')
            else:
                self.view.error('Problema al leer la compra. Intente nuevamente.')
        return


    def read_purchases_client(self):        
        id_cliente = self.id_user
        compras = self.model.read_purchases_client(id_cliente)
     
        if type(compras) == list:
            self.view.show_purchase_header(' Todas las compras ')
            
            for compra in compras:
                id_compra = compra[0]
                self.read_a_purchase(id_compra)
                
        else:
            self.view.error('Problema al leer las compras. Revisa.')
        return


    def read_purchases_date(self):    
        id_cliente = self.id_user

        self.view.ask('Fecha AAAA/MM/DD: ')
        fecha = input()
        
        compras = self.model.read_purchases_date(id_cliente, fecha)
        
        
        if type(compras) == list:
            self.view.show_purchase_header(' Todas las ordenes ')
            
            for compra in compras:
                id_compra = compra[0]
                self.read_a_purchase(id_compra)
                
        else:
            self.view.error('PROBLEMA AL LEER LAS ORDENES. REVISA.')
        return



    """
    **********************************
    * Controllers for DetallesCompra *
    **********************************
    """


    def create_purchase_details(self, id_compra):
        # Se obtiene el id del cliente
        id_cliente = self.id_user
        # Se obtiene el id de la funcion
        self.view.ask('ID Funcion: ')
        id_funcion = input()
        
        precio = 0.0

        if id_funcion != '':
            # Se busca la funcion
            funcion = self.model.read_a_function(id_funcion)
            
            if type(funcion) == tuple:
                # Se leen los asientos de la funcion
                self.read_all_seats_input(id_funcion)
                self.view.ask('Asiento disponible que desee ocupar: ')
                id_asiento = input()
                # Se recibe el resultado de la lectura del asiento
                asiento = self.model.read_a_function_seat(id_funcion, id_asiento)

                # En caso de que se haya equivocado o haya elegido uno ya ocupado
                if asiento[2] == False or asiento == None:
                    while asiento[2] == False or asiento == None:
                        if asiento[2] == False:
                            self.view.error('El asiento esta ocupado. Elija otro.')
                        if asiento == None:
                            self.view.error('El asiento NO existe')
                        self.read_all_seats_input(id_funcion)
                        self.view.ask('Asiento disponible que desee ocupar: ')
                        id_asiento = input()
                        asiento = self.model.read_a_function_seat(id_funcion, id_asiento)

                # Se cambia el estado del asiento
                self.model.update_seat(('disponible = %s',),(False, id_funcion, id_asiento))
                # Se crea el ticket
                id_ticket = self.model.create_ticket(id_cliente, id_funcion, id_asiento)
                # Se obtiene el precio de la funcion
                precio = funcion[8]
                # Se crea la tabla que relaciona el ticket con la compra
                out = self.model.create_purchase_details(id_compra, id_ticket)
                
                if out == True:
                    self.view.ok('El ticket con ID: '+str(id_ticket), 'registro')
                else:
                    if out.errno == 1062:
                        self.view.error('El ticket ya esta registrado.')
                    else:
                        self.view.error('NO se pudo completar la transaccion. Intente nuevamente.')            
            else:
                if funcion == None:
                    self.view.error('La funcion seleccionada no existe')
                else:
                    self.view.error('Problema al leer la funcion. Revise.')
        
        return id_funcion, precio

