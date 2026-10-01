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
            Biblioteca.mostrar_informacion()
            
            
        elif op==2:
            isbn1=int(input('Ingrese el ISBN del libro que desee buscar: '))
            Biblioteca.buscar_isbn(isbn1)
                
            
        elif op==3:
             titulo1=input(str('Ingrese el titulo o un fragmento del mismo para buscar un libro de nuestra biblioteca: ')).capitalize()
             Biblioteca.buscar_titulo(libros,titulo1)
                
            
        elif op==4:
            dni4=input(str('Ingrese el DNI del usuario que quiere buscar'))
            Biblioteca.buscar_usuario(libros, dni4)
            
        elif op==5:
            Biblioteca.mostrar_disponibles(libros)
            
        elif op==6: 
             dni3=int(input('Ingrese el DNI del usuario que va a solicitar el prestamo'))
             libro2=int(input('Ingrese el ISBN del libro que quiere solicitar'))
             Biblioteca.registrar_prestamo(dni3, libro2)
            
        elif op==7:
            id1=input(int('Ingrese el ID del prestamo realizado previamente '))
            Biblioteca.devolver(id1)
            
        elif op==8: 
             DNI1=int(input('Ingrese su DNI'))
             name=str(input('Ingrese su nombre'))
             apellido1=str(input('Ingrese su apellido'))
             Biblioteca.registrar_usuario(name,apellido1, DNI1)
            
        elif op==9:
            Biblioteca.prestamos_activos()
        
        elif op==10:
            Biblioteca.prestamo_usuario()
           
            

    

    
if __name__ == '__main__':
    __main__()
