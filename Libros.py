from datetime import datetime
year=datetime.now().year
class Libro:                        # constructor de la clase libro
                                 #         |  
                      # ___________________V______________________            
    def __init__(self, isbn: int, titulo: str, autor: str, anio: int, genero: str, paginas: int):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.paginas = paginas

        self.__disponible=True 
        # Indica si el libro está disponible para préstamo
        self.__cantidad_prestamos=0 
        # Indica cuantas veces se presto el libro

# METODOS

    def __str__(self):

        return f'isbn: {self.isbn} Titulo: {self.titulo} Autor: {self.autor} anio: {self.anio} Disponible: {'Si' if self.__disponible else 'No'} Genero:{self.genero} Paginas: {self.paginas}'

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            self.__cantidad_prestamos += 1
            return True
        else:
            return False

    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            return True
        else:
            return False

    def esta_disponible(self):
        if self.__disponible == True:
            return True
        else:
            return False

    def cantidad_prestamos(self):
        if self.__cantidad_prestamos >0:
            return self.cantidad_prestamos
        else:
            return 0

    def mostrar_informacion(self):
        print(f"ISBN: {self.isbn}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")
        print(f"Género: {self.genero}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponible: {'Sí' if self.__disponible else 'No'}")
        print(f"Cantidad de préstamos: {self.cantidad_prestamos}")

    def validar_isbn(self):
        if self.isbn==None:
            raise Exception('El campo ISBN no puede estar vacio')
    
    def validar_titulo(self):
        if self.titulo==None:
            raise Exception('El campo titulo no puede estar vacio')

    def validar_autor(self):
        if self.autor==None:
            raise Exception('El campo autor no puede estar vacio')
    
    def validar_anio(self):
        if self.anio==None or self.anio<0 or self.anio>year:
            raise Exception('El campo anio no puede estar vacio, ser negativo o ser mayor a 2026 ')

    def validar_paginas(self):
        if self.paginas<0 or self.paginas==None:
            raise Exception('El campo paginas no puede ser negativo ni estar vacio')


    def validar_genero(self):
        if self.genero==None:
            raise Exception('El campo genero no puede estar vacio')

    
    

