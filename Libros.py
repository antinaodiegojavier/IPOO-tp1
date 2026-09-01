

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

        return f'isbn: {self.isbn} Titulo: {self.titulo} Autor: {self.autor} anio: {self.anio} Disponible: {'Si' if self.disponible else 'No'} Genero:{self.genero} Paginas: {self.paginas}'

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            self.__cantidad_prestamos += 1
            return True
        else:
            return False

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return True
        else:
            return False

    def esta_disponible(self):
        if self.disponible == True:
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
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")
        print(f"Cantidad de préstamos: {self.cantidad_prestamos}")