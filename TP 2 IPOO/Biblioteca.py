from Libros import Libro
from UsuariosBiblioteca import Usuario
from datetime import datetime
from Libros import validar_anio, validar_isbn, validar_autor, validar_genero,validar_paginas, validar_titulo
from PrestamoBiblioteca import Prestamo
day=datetime.now().day
class Biblioteca:
    def __init__(self,nombre,colecUsuar,colecLibros,colecPrestamos):
        self.nombre = nombre
        self.colecUsuar = colecUsuar 
        self.colecLibros = colecLibros
        self.colecPrestamos = colecPrestamos

    def __str__(self):
        return (f'Nombre: {self.nombre}, Coleccion usuarios: {self.colecUsuar}, Coleccion libros: {self.colecLibros}, coleccion prestamos: {self.colecPrestamos}')


    def objetos_creados (self)->list:

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


    def buscar_titulo (self,titulo): 
        print ('-----BUSQUEDA POR TITULO-----')
        encontrado=False
        for libro in self.colecLibros:
            if titulo==libro.titulo:  
                print (f'Libro encontrado: {libro.titulo}')
                print (f'Autor: {libro.autor}')
                encontrado=True
            if not encontrado:
                print ('En nuestra biblioteca, no hay libros relacionados a ese titulo.')

    def buscar_isbn(self,isbn): 
        print ('-----BUSQUEDA POR ISBN-----')
        encontrado=False
        for libro in self.colecLibros:
            if isbn==libro.isbn:
                print ('Libro encontrado')
                print(libro)
                encontrado=True 
            if not encontrado: 
                print ('No se encontro ningun libro con ese ISBN')

    def mostrar_informacion(self):
        print(f"ISBN: {self.colecLibros.isbn}")
        print(f"Título: {self.colecLibros.titulo}")
        print(f"Autor: {self.colecLibros.autor}")
        print(f"Año: {self.colecLibros.anio}")
        print(f"Género: {self.colecLibros.genero}")
        print(f"Páginas: {self.colecLibros.paginas}")
        print(f"Disponible: {'Sí' if self.colecLibros.__disponible else 'No'}")
        print(f"Cantidad de préstamos: {self.colecLibros.cantidad_prestamos}")

    def agregar_libro(self, libros:list):   #relacion:agregacion
        self.colecLibros.append(libros)



    def registrar_usuario(self,dni2,name1,apellido2):    #relacion:agregacion
        
        usuario=Usuario(dni=dni2, nombre=name1, apellido=apellido2)
        self.colecUsuar.append(usuario)


    def registrar_prestamo(self,dni, libro): #relacion:agregacion
        print ('---REGISTRO DE PRESTAMO---')
        for dni in self.colecUsuar:
            if dni in self.colecUsuar:
                for libro in self.colecLibros:
                    if libro in Libro:
                        if libro.get_disponible == True:
                            print (f'''Prestamo realizado con exito!
                            Datos del prestamo:
                            DNI del usuario: {self.colecUsuar.dni}
                            Nombre del usuario: {self.colecUsuar.nombre}
                            ID del prestamo: {self.colecUsuar.id}
                            
                            ''')
                            prestamo1 = self.prestamo_usuario
                            return self.colecPrestamos.append(prestamo1)
                        else:
                            print ('Ese libro no esta disponible en nuestra biblioteca.')
                            
                    else:
                        print('No tenemos ese libro en nuestra biblioteca') 
            else:
                print('No se encontro ningun usuario registrado con ese DNI') 
        


    def crear_libro(self):
    
        isbnNEW=int(input('Ingrese el isbn del nuevo libro que quiere agregar '))
        while len(str(isbnNEW)) >0 and len(str(isbnNEW)) <4:
            isbnNEW=int(input('El campo ISBN debe tener 4 dígitos. Porfavor, ingrese un ISBN valido ')) 
    
    
        titleNEW=str(input('Ingrese el titulo del nuevo libro que quiere agregar '))
        while len(titleNEW) == 0:
            titleNEW=str(input('El campo titulo no puede estar vacio. Porfavor, ingrese un titulo '))
            if validar_titulo(titleNEW)==True:
                self.colecLibros.append(titleNEW)

        autorNEW=str(input('Ingrese el autor del nuevo libro que quiere agregar '))

        while len(autorNEW) == 0:
            autorNEW=str(input('El campo autor no puede estar vacio. Porfavor, ingrese un autor '))
        if validar_autor(autorNEW)==True:
            self.colecLibros.libros.append(autorNEW)

        pags=int(input('Ingrese la cantidad de paginas del nuevo libro que quiere agregar '))
        while len(str(pags)) == 0 or pags <= 0:
            pags=int(input('El campo paginas no puede ser negativo ni estar vacio. Porfavor, ingrese un numero valido '))
        if validar_paginas(pags)==True:
            self.colecLibros.libros.append(pags)

        anioNEW=int(input('Ingrese el año del nuevo libro que quiere agregar (Mayor a 0, y no mayor al anio corriente) '))
        while len(str(anioNEW)) == 0 or anioNEW <= 0 or anioNEW > 2026:
            
            anioNEW=int(input('El campo año no puede estar vacio, ser negativo o ser mayor a 2026. Porfavor, vuelva a ingresar un año valido '))
        if validar_anio(anioNEW)==True: 
            self.colecLibros.libros.append(anioNEW)

        generoNEW=str(input('Ingrese el genero del nuevo libro que quiere agregar '))
        while len(generoNEW) == 0:
            generoNEW=str(input('El campo genero no puede estar vacio. Porfavor, ingrese un genero '))
        if validar_genero(generoNEW)==True:
            self.colecLibros.libros.append(generoNEW)
        libronuevo=Libro(isbn=isbnNEW, titulo=titleNEW, autor=autorNEW,anio=anioNEW, paginas=pags, genero=generoNEW)
        self.colecLibros.libros.append (libronuevo)

        print (f'''Libro nuevo:
            Titulo: {libronuevo.titulo}
            Autor: {libronuevo.autor}
    
        ''')


    def mostrar_disponibles(self): 
        encontrados = False
        print ('\nLibros disponibles de hoy: \n')
        for libro in self.colecLibros:
            if libro.esta_disponible:
                print (libro)
                encontrados = True
        if not encontrados:
            print ('No hay libros disponibles en este momento ')


    def prestamos_activos(self):
        for i in self.colecPrestamos:
            if i.estadoPrestamo is False:
                print ('Prestamos no devueltos: ') 
                print (f'Usuario: {i.usuario}')
                print (f'Libro: {i.libro}')
                print (f'Fecha: {i.day}')
                print (f'Estado del prestamo: {i.estadoPrestamo}')
            else: 
                print ('No hay prestamos activos aun.')

    def prestamo_usuario(self,dni):
            for dni in self.colecUsuar:
                if dni==self.colecUsuar.dni:
                    print ('Prestamos realizados por ese usuario: ')
                    print (f'Usuario: {self.prestamo_usuario}')
                    print (f'Libro: {self.colecLibros}')
                    print (f'Fecha: {day}')
                    print (f'Estado del prestamo: {Prestamo.estadoPrestamo}')
                else:
                    print ('No se encontraron usuarios con ese dni. ')

    def devolver(self, id):
        for i in self.colecPrestamos:
            if i.colecPrestamos.id==id:
                if self.colecPrestamos== False:
                    print (f'''Prestamo identificado
                     Usuario: {self.colecPrestamos, Usuario}
                     Libro prestado: {self.colecPrestamos, Libro}
                     Fecha de prestamo: {self.colecPrestamos, datetime}
                     Prestamo descontinuado. GRACIAS!''')
        else: 
            print ('Prestamo no identificado, revise el ID!')

    def buscar_usuario(self, dni):
            if dni in self.colecUsuar:
                print (f'''Usuario encontrado
                        Nombre: {self.colecUsuar.nombre}
                        Apellido: {self.colecUsuar.apellido}
                        DNI: {self.colecUsuar.dni}
                ''')
            else:
                print ('Usuario no encontrado.')
        








