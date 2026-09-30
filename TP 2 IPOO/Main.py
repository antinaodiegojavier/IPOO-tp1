from Main import tp1ipoo
from Biblioteca import Biblioteca
from Libros import Libro
from PrestamoBiblioteca import Prestamo
from UsuariosBiblioteca import Usuario
def menu():
    print ('\n=============================================================\n')
    print ('''
    *----¡BIENVENIDO/A A LA BIBLIOTECA "MENTES BRILLANTES"!----*

        Que desea hacer hoy?

        1) Mostrar todos nuestros libros 
        2) Buscar un libro por ISBN
        3) Buscar un libro por su titulo
        4) Buscar Usuario
        5) Mostrar nuestros libros disponibles
        6) Registrar un prestamo
        7) Registrar una devolucion 
        8) Registrar usuario
        9) Mostrar prestamos activos
        10) Mostrar prestamos solicitados de un usuario
        0) Salir ''')
    
    print ('\n=============================================================\n') 
    



def __main__():
    
    while True:
        menu()
        op=int(input('Elija una opcion: '))

        if op>12:
            print ('Ingrese una opcion valida: ')
            continue
     
        if op==0:
            print (' Gracias por participar. Saliendo del programa...')
            break  
        

        if op==1:
            return
            
            
        elif op==2:
            return 
                
            
        elif op==3:
            print (f'self.buscar_titulo(libros)')
                
            
        elif op==4:
            print (f'buscar_usuario(libros)')
            
        elif op==5:
            print (f'mostrar_disponibles(libros)')
            
        elif op==6: 
            print (f'registrar_prestamo(libros)')
            
        elif op==7:
            print(f'registrar_devolucion(libros)')
            
        elif op==8: 
            print(f'Biblioteca.registrar_usuario()')
            
        elif op==9:
            print(f'Biblioteca.prestamos_activos()')
        
        elif op==10:
            print (f'Biblioteca.prestamo_usuario()')
           
            

    

    
if __name__ == '__main__':
    __main__()
