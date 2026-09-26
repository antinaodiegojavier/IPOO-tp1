class Usuario:
    def __init__(self,nombre,apellido,dni, usuarios):
        self.nombre= nombre
        self.apellido= apellido
        self.dni= dni
        self.usuarios = []

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido} DNI: {self.dni}'

    def get_dni(self):
        return self.dni

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def mostrar_info(self):
        return f"DNI: {self.dni} - Nombre: {self.nombre} {self.apellido}"


    def registrar(self):
        datos_usuario=[]
        self.dni = int(input('Ingrese su DNI'))
        self.nombre = str (input('Ingrese su nombre'))
        self.apellido = str(input('Ingrese su apellido'))
        self.usuarios = Usuario
        datos_usuario.append(self.usuarios)
        return datos_usuario
    

    def buscar_usuario(self, dni):
        for usuario in dni:
            if usuario.dni == dni:
                return usuario
        return None
       
        

    def listar_usuarios(self):
        return [self.usuarios]