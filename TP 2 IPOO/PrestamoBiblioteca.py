from UsuariosBiblioteca import Usuario
from Biblioteca import Biblioteca
from datetime import datetime
day=datetime.now().day
class Prestamo:
    def __init__(self,usuario,libro,fechaPrestamo,estadoPrestamo, id):
        self.usuario= usuario
        self.libro= libro
        self.fechaPrestamo= fechaPrestamo
        self.estadoPrestamo= False
        self.id = id

    def __str__(self):
        return f'Usuario: {self.usuario}, Libro: {self.libro}, Fecha de prestamo: {self.fechaPrestamo}, Estado del prestamo: {self.estadoPrestamo}'

    def registrar_prestamo(self):
        print ('---REGISTRO DE PRESTAMO---')
        dni3=int(input('Ingrese el DNI del usuario que va a solicitar el prestamo'))
        for dni2 in Usuario:
            if dni3==Usuario(self.dni):
                libro2=int(input('Ingrese el ISBN del libro que quiere solicitar'))
                for libro2 in Libros:
                    if libro2 in Libros:
                        if get_disponible==True:
                            prestamo1=Prestamo(usuario=dni3,libro=libro2,fechaPrestamo=day)
                            self.colecPrestamos.append(prestamo1)
                            
                            
                    else:
                        print('No tenemos ese libro en nuestra biblioteca') 
            else:
                print('No se encontro ningun usuario registrado con ese DNI')        





    def devolucion(self):
        pass
        

