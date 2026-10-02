from UsuariosBiblioteca import Usuario
from datetime import datetime
import random

day=datetime.now().day
class Prestamo:
    def __init__(self, usuario, libro, id):
        self.usuario = usuario        
        self.libro = libro            
        self.fechaPrestamo = datetime.now()
        self.estadoPrestamo = True    # True = activo, False = devuelto
        self.id = random.randint(000,999)

    def __str__(self):
        return f'Usuario: {self.usuario}, Libro: {self.libro}, Fecha de prestamo: {self.fechaPrestamo}, Estado del prestamo: {self.estadoPrestamo}'

   
    def devolver(self):
        if self.estadoPrestamo:
            self.estadoPrestamo = False
            self.libro.get_disponible = True
            print(f'El libro "{self.libro.titulo}" ha sido devuelto por {self.usuario.nombre}.')
        else:
            print('Este préstamo ya esta activo.')
        

