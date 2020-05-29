class View:
    """
    *************************
    * A view for a cine DB *
    *************************
    """
    def start(self):
        print('\n============================================')
        print('=               Bienvenido(a)              =')
        print('============================================')
    
    def end(self):
        print('\n============================================')
        print('=                Hasta luego               =')
        print('============================================\n\n\n')

    def login(self):
        print('\n============================================')
        print('=             Inicio de sesion             =')
        print('============================================')

    def signoff(self):
        print('\n============================================')
        print('=             Ha cerrado sesion            =')
        print('============================================\n\n\n')

    def signin(self):
        print('\n============================================')
        print('=                 Registro                 =')
        print('============================================')

    def welcome_user(self, header):
        print('\n')
        print(' Bienvenido(a) '.center(100,'='))
        print(header.center(100,' '))
        print('='*100)

    def start_menu(self):
        print('\n1. Iniciar sesion')
        print('2. Registrarse como cliente')
        print('3. Salir')

    def main_menu_admin(self):
        print('\n************************')
        print('* -- Menu Principal -- *')
        print('************************')
        print('\n1. Salas')
        print('2. Asientos')
        print('3. Peliculas')
        print('4. Funciones')
        print('5. Administradores')
        print('6. Cerrar sesion')


    def main_menu_client(self):
        print('\n************************')
        print('* -- Menu Principal -- *')
        print('************************')
        print('\n1. Tickets')
        print('2. Funciones')
        print('3. Mi informacion')
        print('4. Cerrar sesion')

    def option(self, last):
        print('\nSelecciona una opcion (1-'+last+'): ', end = '')

    
    def not_valid_option(self):
        print('\n¡Opcion no valida!\nIntenta de nuevo')
    
    def ask(self, output):
        print(output, end = '')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('\n'+'+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))
        print('\n')

    def error(self, err):
        print('\n'+' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))
        print('\n')


    """
    **********************
    * Views for Salas *
    **********************
    """

    def halls_menu(self):
        print('\n*****************************************')
        print('****         Submenu Salas           ****')
        print('*****************************************')
        print('\n1. Agregar sala')
        print('2. Mostrar sala')
        print('3. Mostrar todas las salas')
        print('4. Mostrar salas por tipo de sala')
        print('5. Actualizar sala')
        print('6. Borrar sala')
        print('7. Regresar')

    def show_a_hall(self, record):
        print(f'{record[0]:<8}|{record[1]:<18}|{record[2]:<12}')

    def show_hall_header(self, header):
        print('\n')
        print(header.center(100,'*'))
        print( 'id_sala'.ljust(8)+'|'+'Num. de asientos'.ljust(18)+'|'+'Tipo'.ljust(12))
        print('-'*100)

    def show_hall_midder(self):
        print('-'*100)

    def show_hall_footer(self):
        print('*'*100)

    """
    ************************
    * Vistas para Asientos *
    ************************
    """

    def seats_menu(self):
        print('\n******************************************')
        print('****  Submenu asientos de una funcion ****')
        print('******************************************')
        print('\n1. Agregar asiento disponible')
        print('2. Mostrar asiento disponible')
        print('3. Mostrar todos los asientos disponibles')
        print('4. Mostrar asientos disponibles por fila')
        print('5. Actualizar asiento')
        print('6. Borrar asiento')
        print('7. Regresar')

    def show_a_seat(self, record):
        if record[2] == True:
            aux = 'DISPONIBLE'
        else:
            aux = 'OCUPADO'
        print(f'{record[0]:<11}|{record[1]:<11}|{aux:<11}')

    def show_seat_header(self, header):
        print('\n')
        print(header.center(100,'*'))
        print( 'id_funcion'.ljust(11)+'|'+ 'id_asiento'.ljust(11)+'|'+'Disponible'.ljust(11))
        print('-'*100)

    def show_seat_midder(self):
        print('-'*100)

    def show_seat_footer(self):
        print('*'*100)

    def show_all_seats(self, record):
        if record[2] == True:
            aux = 'DISPONIBLE'
        else:
            aux = 'OCUPADO'
        print(f'{record[1]:<15}|{aux:<11}')
        print('-'*30)

    def show_all_seats_map(self, record):
        if record[2] == False:
            aux = '   '
        else:
            aux = record[1]

        print(f'{aux:<4}', end ='')
        #print('-'*30)

    def show_all_seats_header(self, header):
        print('\n')
        print(header.center(30,'*'))
        print('ID Asiento'.ljust(15)+'|'+'Estado'.ljust(11))
        print('-'*30)


    def print_screen_cinema(self):
        print('-'*39)
        print('|'+' PANTALLA '.center(37,' ')+'|')
        print('-'*39)

    def show_all_seats_header_input(self, header):
        print('\n')
        print(header.center(39,'*'))
        print('\n')        





    def show_all_seats_midder(self):
        print('-'*39)

    def show_all_seats_footer(self):
        print('*'*39)


    """
    ************************
    * Vistas para Peliculas *
    ************************
    """

    def movies_menu(self):
        print('\n***************************************')
        print('*       -- Submenu Peliculas --       *')
        print('***************************************')
        print('\n1. Agregar pelicula')
        print('2. Mostrar pelicula')
        print('3. Mostrar pelicula por nombre')
        print('4. Mostrar todos las peliculas')
        print('5. Mostrar peliculas por genero')
        print('6. Mostrar peliculas por idioma')
        print('7. Mostrar peliculas por clasificacion')
        print('8. Actualizar pelicula')
        print('9. Borrar pelicula')
        print('10. Regresar')

    def show_a_movie(self, record):
        print('ID:', record[0])
        print('Titulo:', record[1])
        print('Director:', record[2])
        print('Genero:', record[3])
        print('Fecha de estreno:', record[4])
        print('Idioma:', record[5])
        print('Clasificacion:', record[6])
        print('Descripcion:', record[7])

    def show_movie_header(self, header):
        print('\n')
        print(header.center(88,'*'))
        print('-'*88)

    def show_movie_midder(self):
        print('-'*88)

    def show_movie_footer(self):
        print('*'*88)


    """
    *************************
    * Vistas para Funciones *
    *************************
    """
    def functions_menu(self):
        print('\n******************************************')
        print('*         -- Submenu Funciones --        *')
        print('******************************************')
        print('\n1. Agregar funcion')
        print('2. Mostrar funcion')
        print('3. Mostrar todas las funciones')
        print('4. Mostrar funciones por pelicula')
        print('5. Mostrar funciones por fecha especifica')
        print('6. Actualizar informacion de funcion')
        print('7. Borrar funcion')
        print('8. Regresar')

    def functions_cmenu(self):
        print('\n******************************************')
        print('*        -- Submenu Funciones --         *')
        print('******************************************')
        print('\n1. Mostrar funciones hoy disponibles')
        print('2. Mostrar funciones por pelicula')
        print('3. Mostrar funciones por fecha especifica')
        print('4. Regresar')

    def show_a_function(self, record):
        print(f'{record[0]:<3}|{record[1]:<12}|{record[2]:<35}|{record[3]:<23}|{str(record[4]):<11}|{str(record[5]):<9}|{record[6]:<8}|{record[7]:<13}|${record[8]:<7}')

    def show_function_header(self, header):
        print('\n')
        print(header.center(130,'*'))
        print( 'ID'.ljust(3)+'|'+'ID Pelicula'.ljust(12)+'|'+'Nombre de Pelicula'.ljust(35)+'|'+'Idioma'.ljust(23)+'|'+'Fecha'.ljust(11)+'|'+'Hora'.ljust(9)+'|'+'ID Sala'.ljust(8)+'|'+'Tipo de Sala'.ljust(13)+'|'+'Precio'.ljust(8))
        print('-'*130)

    def show_function_midder(self):
        print('-'*130)

    def show_function_footer(self):
        print('*'*130)
        print('\n')



    def show_a_cfunction(self, record):
        print(f'{record[0]:<8}|{record[2]:<35}|{record[3]:<23}|{str(record[4]):<11}|{str(record[5]):<9}|{record[6]:<8}|{record[7]:<13}|${record[8]:<7}')

    def show_function_cheader(self, header):
        print('\n')
        print(header.center(130,'*'))
        print( 'Funcion'.ljust(8)+'|'+'Nombre de la pelicula'.ljust(35)+'|'+'Idioma'.ljust(23)+'|'+'Fecha'.ljust(11)+'|'+'Hora'.ljust(9)+'|'+'Sala'.ljust(8)+'|'+'Tipo de Sala'.ljust(13)+'|'+'Precio'.ljust(8))
        print('-'*130)

    def show_function_cmidder(self):
        print('-'*130)

    def show_function_cfooter(self):
        print('*'*130)





    """
    ****************************
    * Vistas para Administador *
    ****************************
    """

    def admin_menu(self):
        print('\n*********************************************')
        print('*      -- Submenu Administradores --        *')
        print('*********************************************')
        print('\n1. Agregar un nuevo administrador')
        print('2. Mostrar informacion de un administrador')
        print('3. Mostrar todos los administradores')
        print('4. Actualizar mi informacion')
        print('5. Borrar a un administrador')
        print('6. Regresar')

    def show_a_admin(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Correo:', record[2])
        print('Telefono:', record[3])

    def show_admin_header(self, header):
        print('\n')
        print(header.center(88,'*'))
        print('-'*88)

    def show_admin_midder(self):
        print('-'*88)

    def show_admin_footer(self):
        print('*'*88)


    """
    ****************************
    * Vistas para Cliente *
    ****************************
    """

    def client_menu(self):
        print('\n*********************************************')
        print('*       -- Submenu Mi Informacion --        *')
        print('*********************************************')
        print('\n1. Mostrar mis datos')
        print('2. Actualizar mi informacion')
        print('3. Eliminar mi cuenta')
        print('4. Regresar')

    def show_a_client(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Correo:', record[2])
        print('Telefono:', record[3])
        print('Fecha de nacimiento:', record[4])

    def show_client_header(self, header):
        print('\n')
        print(header.center(88,'*'))
        print('-'*88)

    def show_client_midder(self):
        print('-'*88)

    def show_client_footer(self):
        print('*'*88)




    """
    *************************
    * Vistas para Tickets *
    *************************
    """

    def tickets_menu(self):
        print('\n********************************')
        print('*     -- Submenu Boletos --    *')
        print('********************************')
        print('\n1. Comprar boletos')
        print('2. Consultar una compra')
        print('3. Regresar')

    def show_a_ticket(self, record):
        print('ID Cliente: '+str(record[1]))
        print('Funcion: ', record[2])
        print('Pelicula: ', record[4])
        print('Fecha y hora: ', record[5], record[6])
        print('Sala: ', record[7])
        print('Asiento: ', record[3])
        print('/'*81)
        print('Precio: ', record[8])


    def show_a_ticket_table(self, record):
        print(f'{record[0]:<4}|{record[2]:<8}|{record[4]:<35}|{str(record[5]):<11}|{str(record[6]):<9}|{record[7]:<5}|{record[3]:<8}|${record[8]:<6}')

    def show_ticket_table_header(self, header):
        print('\n')
        print(header.center(93,'*'))
        print( 'ID'.ljust(4)+'|'+'Funcion'.ljust(8)+'|'+'Pelicula'.ljust(35)+'|'+'Fecha'.ljust(11)+'|'+'Hora'.ljust(9)+'|'+'Sala'.ljust(5)+'|'+'Asiento'.ljust(8)+'|'+'Precio'.ljust(6))
        print('-'*93)

    def show_ticket_table_midder(self):
        print('-'*93)

    def show_ticket_table_footer(self):
        print('*'*93)




    def show_ticket_header(self, header):
        print(header.center(81,'+'))

    def show_ticket_midder(self):
        print('/'*81)

    def show_ticket_footer(self):
        print('+'*81)




    """
    *************************
    * Vistas para Compras *
    *************************
    """

    def sales_menu(self):
        print('\n*************************')
        print('* -- Submenu Compras -- *')
        print('*************************')
        print('1. Comprar boletos')
        print('2. Consultar una compra')
        print('3. Leer todas mis compras')
        print('4. Leer mis compras de una fecha')
        print('5. Regresar')

    def show_purchase(self, record):
        print('\nID Venta:', record[0])
        print('ID Cliente:', record[1])
        print('Fecha:', record[2])
        print('Hora:', record[3])
        print('Total de la compra:', record[4])


    def show_purchase_header(self, header):
        print('\n')
        print(header.center(90,'*'))

    def show_purchase_midder(self):
        print('/'*90)

    def show_purchase_footer(self):
        print('+'*90)


