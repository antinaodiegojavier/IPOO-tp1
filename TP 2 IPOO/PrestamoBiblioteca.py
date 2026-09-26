from UsuariosBiblioteca import Usuario
from datetime import datetime
day=datetime.now().day
class Prestamo:
    def __init__(self,usuario,libro,fechaPrestamo,estadoPrestamo):
        self.usuario= usuario
        self.libro= libro
        self.fechaPrestamo= fechaPrestamo
        self.estadoPrestamo= "activo"
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
                            #ALMACENAR EN ATRIBUTO COLEC PRESTAMO DE BIBLIOTECA
                            
                    else:
                        print('No tenemos ese libro en nuestra biblioteca') 
            else:
                print('No se encontro ningun usuario registrado con ese DNI')        





    def devolver (self):
        self.estadoPrestamo = "devuelto"

    def es_activo(self):
        return self.estadoPrestamo == "activo"

    def mostrar_info(self):
        return f"usuario: {self.usuario} , Libro: {self.libro.titulo}, Fecha: {self.fechaPrestamo}, Estado: {self.estadoPrestamo}"  

