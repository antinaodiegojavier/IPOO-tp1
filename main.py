from Libros import Libro


def crear_objetos()->list:
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








def __main__():
        pass
    
        if __name__ ==__main__:
            __main__()

libros = crear_objetos()
    for libro in libros:
        print(str(libro))




