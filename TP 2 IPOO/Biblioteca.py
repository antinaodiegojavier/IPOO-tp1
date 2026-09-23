class Biblioteca:
    def __init__(self,nombre,colecUsuar,colecLibros,colecPrestamos):
        self.nombre== nombre
        self.colecUsuar= colecUsuar
        self.colecLibros= colecLibros
        self.colecPrestamos= colecPrestamos

    def __str__(self):
        return (f'Nombre: {self.nombre}, Coleccion usuarios: {self.colecUsuar}, Coleccion libros: {self.colecLibros}, coleccion prestamos: {ColecPrestamos}')

    def registrar_usuario(self):
        user=input(str('Ingrese su nombre de usuario'))
        user=Usuario(       )

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
