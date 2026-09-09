# Trabajo Práctico 1: Introducción a la Programación Orientada a Objetos



## 1. Integrantes del Grupo:
 
                Diego Antinao 

                Robetino Klug



## 2. Descripción Breve del Problema

Una biblioteca requiere un sistema informático que funcione en memoria y se ejecute por consola para gestionar su stock de libros. El sistema permite:
- Registrar libros y consultar su información.
- Realizar búsquedas por ISBN y por coincidencia de título.
- Filtrar libros por género y consultar cuáles están disponibles.
- Gestionar préstamos y devoluciones controlando la disponibilidad.
- Obtener estadísticas globales de libros prestados y disponibles.
- Identificar el libro con más préstamos, el más antiguo y el promedio de páginas de todos los libros.




## 3. Descripción de la Clase Desarrollada (`Libro`)

La clase `Libro` esta en el archivo `Libro.py` con los siguientes atributos y métodos:

### Atributos:
- `isbn` (str): Identificador único del libro.
- `titulo` (str): Nombre del libro.
- `autor` (str): Escritor del libro.
- `anio` (int): Año de publicación.
- `genero` (str): Género literario.
- `paginas` (int): Cantidad de páginas.
- `__disponible` (bool, **encapsulado**): Indica si el libro está en la biblioteca. Inicia siempre en `True`.
- `__cantidad_prestamos` (int, **encapsulado**): Contador de veces prestado. Inicia en `0`.

### Métodos:

- `__init__(isbn, titulo, autor, anio, genero, paginas)`: Constructor que valida e inicializa el libro.
- `_validar(...)`: Valida que los datos de entrada cumplan las reglas de integridad de la biblioteca.
- `devolver()`: Si está prestado, pasa a disponible (`__disponible = True`) y retorna msje de éxito. Si ya estaba disponible, rechaza la operación.
- `esta_disponible() -> bool`: Método consultor (getter) para conocer el estado sin alterar el atributo privado.
- `cantidad_prestamos() -> int`: Retorna la cantidad total de préstamos.
- `mostrar_informacion()`: Imprime en consola la ficha formateada del libro.

---

## 4. Explicación de cómo se aplicó la Abstracción

En un libro físico real existen infinitos atributos: color de la tapa, peso en gramos, tipo de encuadernación, editorial, tipografía, estado de desgaste físico del papel, estantería física, etc. Para el sistema de préstamos de la biblioteca solo abstrajimos los mas elementales:
- Para identificarlo: `isbn`.
- Para describirlo al lector: `titulo`, `autor`, `anio`, `genero`, `paginas`.
- Para operar los préstamos: `__disponible` y `__cantidad_prestamos`.

---

## 5. Explicación de cómo se aplicó el Encapsulamiento

El encapsulamiento se aplicó:
1. Prefijando los atributos críticos con doble guion bajo: `self.__disponible` y `self.__cantidad_prestamos`. Esto activa el *name mangling* de Python, impidiendo que desde `main.py` se pueda hacer libremente `libro.disponible = False`.
2. Obligando a que las transiciones de estado ocurran únicamente a través de los métodos `prestar()` y `devolver()`.
3. Esto garantiza que nadie pueda prestar un libro sin incrementar la cantidad de préstamos, o prestar un libro que ya está prestado, preservando la coherencia del objeto.

---

## 6. Descripción de los Principales Algoritmos Implementados

Todos los algoritmos en `main.py` se implementaron mediante **recorridos manuales de la lista `libros`** (sin funciones mágicas que resuelvan la búsqueda de forma oculta):
- **Búsqueda por ISBN:** Bucle `for` que compara uno a uno los libros. Al hallar coincidencia, detiene la búsqueda y muestra la ficha.
- **Búsqueda por título:** Bucle `for` con evaluación de coincidencia.
- **Libros disponibles:** Recorrido manual filtrando con la llamada al método `libro.esta_disponible()`.
- **Estadísticas:** Recorrido con contadores (`disponibles` y `prestados`), calculando luego los porcentajes sobre el total.
- **Libro más prestado:** Algoritmo clásico de búsqueda de máximo lineal.
- **Libro más antiguo:** Algoritmo de búsqueda de mínimo lineal con un bucle `for` evaluando `libro.anio < libro_antiguo.anio`.
- **Promedio de páginas:** Recorrido acumulando `libro.paginas` en una suma, dividiendo al final por la cantidad de libros.

---

## 7. Respuestas a las Preguntas Conceptuales

### 1. Abstracción
**¿Por qué no resulta necesario representar absolutamente toda la información que posee un libro real?**
     > Representar datos irrelevantes (como el grosor del lomo o el tipo de papel) aumentaría innecesariamente la complejidad, sin aportar ningún valor funcional a la administración de la biblioteca.

### 2. Modelo
**¿Qué características del libro fueron consideradas relevantes para este sistema? ¿Por qué?**
     > - **ISBN:** Código normalizado que permite identificar a cada libro en la lista.
     > - **Título y Autor:** Datos fundamentales para que los usuarios busquen y reconozcan los libros.
     > - **Año y Género:** Necesarios para categorizar el catálogo y realizar búsquedas temáticas o temporales.
     > - **Páginas:** Requerido para un análisis de promedio de páginas dentro de la biblioteca.
     > - **Disponibilidad y Cantidad de Préstamos:** Indispensables para la información sobre préstamos y devoluciones.

### 3. Encapsulamiento
**¿Qué significa que un atributo esté encapsulado?**
     > Significa que el atributo pertenece al ámbito interno del objeto y no purde ser modificado por una accion externa. Solo los métodos de la propia clase tienen permiso para modificar el atributo.

### 4. Estado Interno
**¿Por qué no debería permitirse modificar directamente la disponibilidad de un libro desde main.py?**
     > Porque si el programa principal hiciera `libro.disponible = False`, se saltaría todas las validaciones:
     > 1. No se comprobaría si el libro ya estaba prestado.
     > 2. No se incrementaría el contador de préstamos.
     > 3. Se generaría una inconsistencia en los datos del sistema. Modificar el estado directamente rompe la integridad del objeto.

### 5. Métodos
**¿Cuál es la ventaja de utilizar: `libro.prestar()` en lugar de modificar directamente el estado del objeto?**
     > La ventaja es que `libro.prestar()` centraliza la lógica en un solo lugar. El método comprueba el estado actual, realiza la transición a prestado. Si en el futuro las reglas de préstamo cambian (por ejemplo, registrar fecha o límite de días), solo se modifica el método de la clase sin tener que reescribir nada en `main.py`.

### 6. Algoritmos
**¿Cuál es el algoritmo utilizado para encontrar el libro con mayor cantidad de préstamos? Explíquenlo con sus palabras.**
     > Se usa un **algoritmo de búsqueda lineal**. 
     > 1. Se toma el primer libro de la lista como referencia inicial.
     > 2. Se recorre la lista elemento por elemento a partir del segundo.
     > 3. Si el libro actual fue prestado más veces, pasa a ser el nuevo "máximo actual".
     > 4. Al terminar el recorrido de la lista, se tendrá al libro más solicitado. Esto evita ordenar toda la lista de forma manual.

### 7. Colecciones
**¿Qué diferencia existe entre tener: `libro1 = Libro(...)` y tener: `libros = []` con varios objetos almacenados dentro?**
     > - `libro1` es una **variable individual** que apunta a una única instancia específica. Trabajar solo con variables sueltas (`libro1`, `libro2`, `libro3`) vuelve imposible la automatización, porque para buscar o calcular algo habría que escribir código repetitivo para cada variable.
     > - `libros = []` es una **lista de objetos**. Permite almacenar una cantidad de libros y tratarlos de forma genérica mediante bucles.

---

##  Pregunta de Diseño
**Supongan que posteriormente la biblioteca necesita almacenar información sobre usuarios. ¿Agregarían esos datos a la clase Libro? Justifiquen su respuesta.**
     > *No porque violaría el **Principio de Responsabilidad Única** y romperia la abstracción. Un libro es un ejemplar bibliográfico; un usuario es un socio de la biblioteca.
     La solución correcta seria crear una clase `Usuario` con sus propios atributos y métodos.

---

## 9. Validaciones
**¿Dónde consideran que deberían realizarse estas validaciones? Expliquen por qué eligieron ese lugar.**
     > Las validaciones deben realizarse por fuera del **constructor (`__init__`) de la clase `Libro`**.
     se las invoca desde **main.py** para validar datos ingreasados en la funcion `creacion_libro` al validar esto, se asegura que **ningún objeto Libro pueda existir en un estado inválido**.

---

## 10. Relación de Conceptos

Abstracción      -> Define qué información y qué acciones son relevantes del libro.
     
Encapsulamiento  -> Oculta y protege el estado (__disponible, __cantidad_prestamos).

Objetos          -> Son las instancias creadas a partir de la clase Libro.
     
Comportamientos  -> Son los métodos prestar(), devolver() que modifican el estado de forma controlada.
     
Algoritmos       -> Operan sobre la colección de objetos (libros = []) para resolver búsquedas y estadísticas.

