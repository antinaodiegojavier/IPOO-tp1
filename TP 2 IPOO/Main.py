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
    libros=objetos_creados(list())
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
            mostrar_libros(libros)
            
            
        elif op==2:
            buscar_isbn(libros)
                
            
        elif op==3:
            buscar_titulo(libros)
                
            
        elif op==4:
            #buscar usuario
            
        elif op==5:
            mostrar_disponibles(libros)
            
        elif op==6: 
            registrar_prestamo(libros)
            
        elif op==7:
            registrar_devolucion(libros)
            
        elif op==8: 
            #registrar usuario
            
        elif op==9:
            #mostrar prestamos activos
        
        elif op==10:
            #mostrar prestamos de un usuario
           
            

    

    
if __name__ == '__main__':
    __main__()
