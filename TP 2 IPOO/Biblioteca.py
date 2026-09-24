from Libros import Libro
class Biblioteca:
    def __init__(self,nombre,colecUsuar,colecLibros,colecPrestamos):
        self.nombre== nombre
        self.colecUsuar= colecUsuar
        self.colecLibros= colecLibros
        self.colecPrestamos= colecPrestamos

    def __str__(self):
        return (f'Nombre: {self.nombre}, Coleccion usuarios: {self.colecUsuar}, Coleccion libros: {self.colecLibros}, coleccion prestamos: {ColecPrestamos}')


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

    def creacion_libro(libros:list):
    
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

