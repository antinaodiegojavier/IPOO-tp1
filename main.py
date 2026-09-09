from Libros import Libro, validar_anio,validar_autor,validar_genero,validar_isbn,validar_paginas,validar_titulo


def objetos(libros)->list:
    objetos = list[0]

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


def mostrar_libros(libros: list):
    print ('-----LIBROS DE LA BIBLIOTECA-----') #Algoritmo 1
    for libro in libros:
       print (libro)



def buscar_isbn(libros:list): #Algoritmo 2
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



def buscar_titulo (libros: list): #Algoritmo 3
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



def filtrar_genero (libros:list): #Algoritmo 4
    print ('-----BUSQUEDA POR GENERO-----')
    genero=str(input('Ingrese un genero para buscar un libro de nuestra biblioteca: ')).capitalize()
    encontrado=False
    for libro in libros:
            if genero==libro.genero:
                print('Libro encontrado')  
                print (libro) 
                encontrado=True
    if not encontrado:
                print ('No tenemos libros de ese genero en nuestra biblioteca')

    

def mostrar_disponibles(libros:list): #Algoritmo 5
    encontrados = False
    print ('\nLibros disponibles de hoy: \n')
    for libro in libros:
        if libro.esta_disponible:
            print (libro)
            encontrados = True
    if not encontrados:
         print ('No hay libros disponibles en este momento ')


def registrar_prestamo(libros:list): #algoritmo 6
        print ('-----REGISTRO DE PRESTAMO-----')
        encontrado=False
        ISBN=input(('ingrese el ISBN del libro que quiere prestar: '))
        for libro in libros:
            if libro.isbn==ISBN:
                libro.esta_disponible=False
                libro.prestar()
                print('Prestamo registrado con exito')
        for libro in libros:
            if libro.isbn==ISBN and libro.esta_disponible==False:
                print('Ese libro no esta disponible en este momento nuestra biblioteca')
   



def registrar_devolucion(libros:list): #algoritmo 7
     print ('------REGISTRO DE DEVOLUCION------')
     ISBN=input(('ingrese el isbn del libro que sera devuelto: '))
     encontrado = False
     for libro in libros:
          if ISBN==libro.isbn and libro.esta_disponible==False:
            libro.devolver()
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

     porc_disponibles=libros_disponibles*100/total_libros
     porc_prestados=libros_prestados*100/total_libros

     print (f'cantidad de libros disponibles: {libros_disponibles}')
     print (f'cantidad de libros prestados: {libros_prestados}')
     print (f'cantidad total de libros: {total_libros}')
     print (f'Porcentaje de libros disponibles: {porc_disponibles}')
     print (f'Porcentaje de libros prestados: {porc_prestados}')


def libro_mas_prestado(libros:list): 
    for libro in libros:
        if  (f'cantidad_prestamos(libro)') > (f'cantidad_prestamos(libro)'):
            print( 'libro.mostrar_informacion()')
            print (f'Cantidad de prestamos: {libro.cantidad_prestamos}')
            print ('-----LIBRO MAS PRESTADO DE NUESTRA BIBLIOTECA: -----')
            print (f'Titulo: {libro.titulo}')
            print (f'Autor: {libro.autor}')
            print (f'Veces prestado: {libro.cantidad_prestamos}')
    else:
         print ('No se han registrado prestamos de ningun libro en nuestra biblioteca')


def libro_mas_antiguo(libros:list):  

    libro_antiguo = libros [0]     
    for libro in libros:
        if libro.anio < libro_antiguo.anio:
            libro_antiguo=libro 
            print ('-----LIBRO MAS ANTIGUO DE NUESTRA BIBLIOTECA: -----')
            print (f'Titulo: {libro_antiguo.titulo}')
            print (f'Anio: {libro_antiguo.anio}')
            

def promedio_paginas (libros: list):
    cant_libros = len(libros)
    tot_pags = 0

    for libro in libros:
        tot_pags += libro.paginas

    prom_pags = tot_pags / cant_libros

    print (f'cantidad de libros: {cant_libros}')
    print (f'total de paginas: {tot_pags}')
    print (f'promedio de paginas: {prom_pags}')



def menu():
    print ('\n=============================================================\n')
    print ('''
    *----¡BIENVENIDO/A A LA BIBLIOTECA "MENTES BRILLANTES"!----*

        Que desea hacer hoy?

        1) Mostrar todos nuestros libros 
        2) Buscar un libro por ISBN
        3) Buscar un libro por su titulo
        4) Filtrar libros por genero
        5) Mostrar nuestros libros disponibles
        6) Registrar un prestamo
        7) Registrar una devolucion 
        8) Mostrar estadisticas de nuestros libros
        9) Mostrar nuestro libro mas solicitado 
        10) Mostrar nuestro libro mas antiguo
        11) Calcular promedio de paginas 
        12) Crear y agregar un nuevo libro a nuestra lista de libros
        0) Salir ''')
    
    print ('\n=============================================================\n') 
    


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


     

    



def __main__():
    libros=objetos(list())
    while True:
        menu()
        op=int(input('Elija una opcion: '))

        if op>12:
            print ('Ingrese una opcion valida: ')
            continue
     
        if op==0:
            print (' Gracias por participar. Saliendo del programa...')
            break  
        

        if op==1:
            mostrar_libros(libros)
            
            
        elif op==2:
            buscar_isbn(libros)
                
            
        elif op==3:
            buscar_titulo(libros)
                
            
        elif op==4:
            filtrar_genero(libros)
            
        elif op==5:
            mostrar_disponibles(libros)
            
        elif op==6: 
            registrar_prestamo(libros)
            
        elif op==7:
            registrar_devolucion(libros)
            
        elif op==8: 
            mostrar_estadisticas(libros)
            
        elif op==9:
            libro_mas_prestado(libros)
        
        elif op==10:
            libro_mas_antiguo(libros)
           
        elif op==11:
            promedio_paginas(libros)
        elif op==12:
            creacion_libro(libros)
            

    

    
if __name__ == '__main__':
    __main__()
