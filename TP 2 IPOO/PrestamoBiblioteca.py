class Prestamo:
    def __init__(self,usuario,libro,fechaPrestamo,estadoPrestamo):
        self.usuario= usuario
        self.libro= libro
        self.fechaPrestamo= fechaPrestamo
        self.estadoPrestamo= estadoPrestamo

    def __str__(self):
        return f'Usuario: {self.usuario}, Libro: {self.libro}, Fecha de prestamo: {self.fechaPrestamo}, Estado del prestamo: {self.estadoPrestamo}'

    def devolucion(self):
        

