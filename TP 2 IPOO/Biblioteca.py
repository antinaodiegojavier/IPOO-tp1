from Libros import Libro
from UsuariosBiblioteca import Usuario
from datetime import datetime
day=datetime.now().day
class Biblioteca:
    def __init__(self,nombre,colecUsuar,colecLibros,colecPrestamos):
        self.nombre== nombre
        self.colecUsuar= []
        self.colecLibros=[]
        self.colecPrestamos= []

    def __str__(self):
        return (f'Nombre: {self.nombre}, Coleccion usuarios: {self.colecUsuar}, Coleccion libros: {self.colecLibros}, coleccion prestamos: {ColecPrestamos}')


    def objetos_creados(libros)->list:

        libro1=Libro( isbn= 1032, titulo='Emma', autor='Austen', anio= 1815, genero= 'Romance', paginas= 474)
        libro2=Libro(isbn= 6489, titulo='Dune', autor='Herbert', anio= 1965, genero= 'Ciencia ficcion', paginas= 688)
        libro3=Libro(isbn= 5993, titulo='Dracula', autor='Stoker', anio= 1897, genero= 'Terror', paginas= 418)
        libro4=Libro(isbn= 1204, titulo='Hamlet', autor='Shakespeare', anio= 1603, genero= 'Drama', paginas= 200)
        libro5=Libro(isbn= 1244, titulo='Matilda', autor='Dahl', anio= 1988, genero= 'Fantasia', paginas= 240)
        libro6=Libro(isbn= 5869, titulo='Carrie', autor='King', anio= 1974, genero= 'Terror', paginas= 199)
        libro7=Libro(isbn= 2211, titulo='Momo', autor='Ende', anio= 1973, genero= 'Fantasia', paginas= 304)
        libro8=Libro(isbn= 5674, titulo='El Hobbit', autor='Tolkien', anio= 1937, genero= 'Fantasia', paginas= 310)
        libro9=Libro(isbn= 7965, titulo='Pinocho', autor='Collodi', anio= 1883, genero= 'Fantasia', paginas= 188)
        libro10=Libro(isbn= 2357, titulo='Alicia', autor='Carroll', anio= 1865, genero= 'Fantasia', paginas= 128)
    return [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10]


    def buscar_titulo (libros: list): 
        print ('-----BUSQUEDA POR TITULO-----')
        titulo1=input(str('Ingrese el titulo o un fragmento del mismo para buscar un libro de nuestra biblioteca: ')).capitalize()
        encontrado=False
        for libro in libros:
            if titulo1==libro.titulo:  
                print (f'Libro encontrado: {libro.titulo}')
                print (f'Autor: {libro.autor}')
                encontrado=True
            if not encontrado:
                print ('En nuestra biblioteca, no hay libros relacionados a ese titulo.')

    def buscar_isbn(libros:list): 
        print ('-----BUSQUEDA POR ISBN-----')
        isbn1=int(input('Ingrese el ISBN del libro que desee buscar: '))
        encontrado=False
        for libro in libros:
            if isbn1==libro.isbn:
                print ('Libro encontrado')
                print(libro)
                encontrado=True 
            if not encontrado: 
                print ('No se encontro ningun libro con ese ISBN')

    def mostrar_informacion(self):
        print(f"ISBN: {self.isbn}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")
        print(f"Género: {self.genero}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponible: {'Sí' if self.__disponible else 'No'}")
        print(f"Cantidad de préstamos: {self.cantidad_prestamos}")

    def agregar_libro(self, libros:list):   #relacion:agregacion
        self.colecLibros.append(libros)



    def registrar_usuario(self):    #relacion:agregacion
        
        DNI1=int(input('Ingrese su DNI'))
        name=str(input('Ingrese su nombre'))
        apellido1=str(input('Ingrese su apellido'))
        usuario=Usuario(nombre=name, apellido=apellido1,dni=DNI1)
        self.colecUsuar.append(usuario)


    def registrar_prestamo(self): #relacion:agregacion
        print ('---REGISTRO DE PRESTAMO---')
        dni3=int(input('Ingrese el DNI del usuario que va a solicitar el prestamo'))
        for dni3 in Usuario:
            if dni3==Usuario(self.dni):
                libro2=int(input('Ingrese el ISBN del libro que quiere solicitar'))
                for libro2 in Libros:
                    if libro2 in Libros:
                        if get_disponible==True:
                            prestamo1=Prestamo(usuario=dni3,libro=libro2,fechaPrestamo=day, id=id, estadoPrestamo:True)
                            self.ColecPrestamos.append(prestamo1)
                            
                    else:
                        print('No tenemos ese libro en nuestra biblioteca') 
            else:
                print('No se encontro ningun usuario registrado con ese DNI') 
        


    def crear_libro(libros:list):
    
        isbnNEW=int(input('Ingrese el isbn del nuevo libro que quiere agregar '))
        while len(str(isbnNEW)) >0 and len(str(isbnNEW)) <4:
            isbnNEW=int(input('El campo ISBN debe tener 4 dígitos. Porfavor, ingrese un ISBN valido ')) 
    
    
        titleNEW=str(input('Ingrese el titulo del nuevo libro que quiere agregar '))
        while len(titleNEW) == 0:
            titleNEW=str(input('El campo titulo no puede estar vacio. Porfavor, ingrese un titulo '))
        if validar_titulo(titleNEW)==True:
            libros.append(titleNEW)

        autorNEW=str(input('Ingrese el autor del nuevo libro que quiere agregar '))

        while len(autorNEW) == 0:
            autorNEW=str(input('El campo autor no puede estar vacio. Porfavor, ingrese un autor '))
        if validar_autor(autorNEW)==True:
            libros.append(autorNEW)

        pags=int(input('Ingrese la cantidad de paginas del nuevo libro que quiere agregar '))
        while len(str(pags)) == 0 or pags <= 0:
            pags=int(input('El campo paginas no puede ser negativo ni estar vacio. Porfavor, ingrese un numero valido '))
        if validar_paginas(pags)==True:
            libros.append(pags)

        anioNEW=int(input('Ingrese el año del nuevo libro que quiere agregar (Mayor a 0, y no mayor al anio corriente) '))
        while len(str(anioNEW)) == 0 or anioNEW <= 0 or anioNEW > 2026:
            
            anioNEW=int(input('El campo año no puede estar vacio, ser negativo o ser mayor a 2026. Porfavor, vuelva a ingresar un año valido '))
        if validar_anio(anioNEW)==True: 
            libros.append(anioNEW)

        generoNEW=str(input('Ingrese el genero del nuevo libro que quiere agregar '))
        while len(generoNEW) == 0:
            generoNEW=str(input('El campo genero no puede estar vacio. Porfavor, ingrese un genero '))
        if validar_genero(generoNEW)==True:
            libros.append(generoNEW)
        libronuevo=Libro(isbn=isbnNEW, titulo=titleNEW, autor=autorNEW,anio=anioNEW, paginas=pags, genero=generoNEW)
        libros.append (libronuevo)

        print (f'''Libro nuevo:
            Titulo: {libronuevo.titulo}
            Autor: {libronuevo.autor}
    
        ''')


    def mostrar_disponibles(libros:list): 
        encontrados = False
        print ('\nLibros disponibles de hoy: \n')
        for libro in libros:
            if libro.esta_disponible:
                print (libro)
                encontrados = True
        if not encontrados:
            print ('No hay libros disponibles en este momento ')


    def prestamos_activos(self, usuario,libro):
        for i in self.colecPrestamos:
            if i.estadoPrestamo is False:
                print ('Prestamos no devueltos: ') 
                print (f'Usuario: {i.usuario}')
                print (f'Libro: {i.libro}')
                print (f'Fecha: {i.day}')
                print (f'Estado del prestamo: {i.estadoPrestamo}')

    def prestamo_usuario(self,usuario,dni):
        for usuario1 in colecUsuar:
            for dni in usuario1:
                if dni==usuario1.dni:
                    print ('Prestamos realizados por ese usuario: ')
                    print (f'Usuario: {Prestamo.usuario}')
                    print (f'Libro: {Prestamo.libro}')
                    print (f'Fecha: {prestamo.fechaPrestamo}')
                    print (f'Estado del prestamo: {prestamo.estadoPrestamo}')
                else:
                    print ('No se encontraron usuarios con ese dni. ')

    def devolver(self, id):
        for i in colecPrestamos:
            if i.colecPrestamos.id==id:
                    self.colecPrestamos.estadoPrestamo== False
                print (f'''Prestamo identificado
                     Usuario: {self.colecPrestamos.usuario}
                     Libro prestado: {self.colecPrestamos.libro}
                     Fecha de prestamo: {self.colecPrestamos.fechaPrestamo}
                     Prestamo descontinuado. GRACIAS!
                
                ''')
            else: 
                print ('Prestamo no identificado, revise el ID!')

    def buscar_usuario(self, usuario):
            if usuario in self.colecUsuar:
                print (f'''Usuario encontrado
                        Nombre: {self.colecUsuar.nombre}
                        Apellido: {self.colecUsuar.apellido}
                        DNI: {self.colecUsuar.dni}
                ''')
            else:
                print ('Usuario no encontrado.')
        








