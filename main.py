from Libros import Libro


def objetos()->list:
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
    return [libro1,libro2,libro3,libro4,libro5,libro6,libro7,libro8,libro9,libro10]


def mostrar_libros(libros: list):
    print ('-----LIBROS DE LA BIBLIOTECA-----') #Algoritmo 1
    for libro in libros:
       print (libro)



def buscar_isbn(libros:list): #Algoritmo 2
    print ('-----BUSQUEDA POR ISBN-----')
    isbn1=input(str('Ingrese el ISBN del libro que desee buscar'))
    encontrado=False
    for libro in libros:
        if isbn1==libro.isbn:
            print ('Libro encontrado')
            print(libro)
            encontrado=True #ACLARACION: no se si imprime el libro relacionado al isbn o si imprime todos los libros
    if not encontrado: 
            print ('No se encontro ningun libro con ese ISBN')



def buscar_titulo (libros: list): #Algoritmo 3
    print ('-----BUSQUEDA POR TITULO-----')
    titulo1=input(str('Ingrese el titulo o un fragmento del mismo para buscar un libro de nuestra biblioteca')).capitalize
    encontrado=False
    for libro in libros:
        if titulo1==libro.titulo:  #ACLARACION: esta condicion esta mal, ya que si el usuario ingresa "quijote" y el libro es don quijote, no lo mostrara. CAMBIAR CONDICION
            print (f'Libro encontrado: {libro.titulo}')
            encontrado=True
    if not encontrado:
            print ('En nuestra biblioteca, no hay libros relacionados a ese titulo.')



def filtrar_genero (libros:list): #Algoritmo 4
    print ('-----BUSQUEDA POR GENERO-----')
    genero=input(str('Ingrese un genero para buscar un libro de nuestra biblioteca'))
    encontrado=False
    for libro in libros:
            if genero==libro.genero:
                print('Libro encontrado')  
                print (libro) 
                encontrado=True
    if not encontrado:
                print ('No tenemos libros de ese genero en nuestra biblioteca')

    

def mostrar_disponibles(libros:list): #Algoritmo 5
    for libro in libros:
        if libro.esta_disponible==True:
            print (libros)


def registrar_prestamo(libros:list): #algoritmo 6
     print ('-----REGISTRO DE PRESTAMO-----')
     ISBN=input(str('ingrese el ISBN del libro que quiere prestar'))
     encontrado=False
     for libro in libros:
          if ISBN==libro.isbn:
               if libro.esta_disponible==True:
                    libro.esta_disponible=False
                    print('Prestamo registrado con exito')
                    encontrado=True
     if not encontrado:
          print('No se encontro ningun libro con ese ISBN')

def registrar_devolucion(libros:list): #algoritmo 7
     print ('------REGISTRO DE DEVOLUCION------')
     ISBN=input(str('ingrese el isbn del libro que sera devuelto'))
     encontrado = False
     for libro in libros:
          if ISBN==libro.isbn:
               if libro.esta_disponible==False:
                    libro.esta_disponible=True
                    print('Devolucion registrada con exito')
                    encontrado=True
     if not encontrado:
          print('No se encontro ningun libro con ese ISBN')


def mostrar_estadisticas(libros:list):  #algoritmo  8
     print ('----ESTADISTICAS DE LA BIBLIOTECA----')
     total_libros=len(libros)
     libros_disponibles=0
     libros_prestados=0
     for libro in libros :
          if libro.esta_disponible==True:
               libros_disponibles +=1
          else:
               libros_prestados +=1
               print (f'cantidad de libros disponibles: {libros_disponibles}')
     print (f'cantidad de libros prestados: {libros_prestados}')
     print (f'cantidad total de libros: {total_libros}')






def __main__():
    pass
    libros=objetos()
    mostrar_libros(libros)
    if __name__ ==__main__:
            __main__()






