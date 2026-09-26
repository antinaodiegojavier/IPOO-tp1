class Usuario:
    def __init__(self,nombre,apellido,dni):
        self.nombre= nombre
        self.apellido= apellido
        self.dni= dni

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido} DNI: {self.dni}'
    
    def buscar_X_DNI(self):
        dni2=int(input('Ingrese el DNI del usuario que quiere buscar'))
        for dni2 in Usuario:
            if dni2==self.dni:
                print (f'''Usuario encontrado:
                           Nombre: {self.nombre}
                           Apellido: {self.apellido}
                           DNI: {self.dni}             ''')  
            else:
                print ('Usuario no encontrado')
        

