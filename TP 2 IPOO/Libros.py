from datetime import datetime
year=datetime.now().year
class Libro: 

    # METODOS                                                             
                                  
    def __init__(self, isbn: int, titulo: str, autor: str, anio: int, genero: str, paginas: int):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.paginas = paginas

        self.__disponible = True        
        self.__cantidad_prestamos = 0

    def __str__(self):

        return f'isbn: {self.isbn} Titulo: {self.titulo} Autor: {self.autor} anio: {self.anio} Disponible: {'Si' if self.__disponible else 'No'} Genero:{self.genero} Paginas: {self.paginas}'


    @property
    def get_disponible(self):
            return self.__esta_disponible

    @property
    def get_prestar(self):
        if self.__disponible:
            self.__disponible = False
            self.__cantidad_prestamos += 1
    return self.__cantidad_prestamos

    def objetos(libros)->list:

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

        

    

    def prestar(self):
        print (f"Disponible: {'Sí' if self.__disponible else 'No'}")

    def devolver(self):
    
        print(f"Cantidad de préstamos: {self.__cantidad_prestamos}")

    def esta_disponible(self):
        if self.__disponible == True:
            return True
        else:
            return False

    def cantidad_prestamos(self):
       print (f"Cantidad de préstamos: {self.__cantidad_prestamos}")


def validar_isbn(isbn):
        if isbn==None:
            return True
        else:
            return False
            
    
def validar_titulo(titulo):
        if titulo==None:
            return True
        else:
            return False
            
def validar_autor(autor):
        if autor==None:
            return True
        else:
            return False
            
def validar_anio(anio):
        if anio==None or anio<0 or anio>year:
            return True
        else:
            return False
           
def validar_paginas(pag):
        if pag<0 or pag ==None:
            return True
        else:
            return False
            


def validar_genero(gen):
        if gen==None:
            return True
        else:
            return False
            

    
    

