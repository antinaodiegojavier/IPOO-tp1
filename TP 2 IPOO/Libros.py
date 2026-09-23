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
            

    
    

