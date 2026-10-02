# Trabajo Práctico N.º 2 – Sistema de Biblioteca

## Integrantes
- Diego Antinao
- Robertino Klug

---

##  Descripción de las nuevas clases
### Clase 'Prestamo'
- Representa la relación entre un **Usuario** y un **Libro**.
- Atributos principales:
  - 'usuario': objeto de la clase 'Usuario'.
  - `libro`: objeto de la clase `Libro`.
  - `fechaPrestamo`: fecha y hora en que se realiza el préstamo.
  - `estadoPrestamo`: indica si el préstamo está activo o devuelto.
  - `id`: identificador aleatorio generado con `random.randint(000, 999)`.
- Métodos:
  - `__str__`: devuelve una representación legible del préstamo.
  - `devolver()`: marca el préstamo como devuelto y libera el libro.

### Clase `Biblioteca`
- Administra las colecciones de **usuarios**, **libros** y **préstamos**.
- Métodos principales:
  - `registrar_usuario(usuario)`: agrega un usuario a la biblioteca.
  - `registrar_libro(libro)`: agrega un libro a la biblioteca.
  - `registrar_prestamo(dni, isbn)`: crea un préstamo si el usuario y el libro existen y el libro está disponible.
  - `devolucion(id_prestamo)`: permite devolver un libro y cerrar el préstamo.

---

##  Explicación de las relaciones identificadas
- **Usuario – Prestamo**: relación **1 a muchos**. Un usuario puede tener varios préstamos.
- **Libro – Prestamo**: relación **1 a muchos**. Un libro puede estar en varios préstamos, pero solo uno activo a la vez.
- **Biblioteca – Usuario/Libro/Prestamo**: relación de **composición**. La biblioteca contiene y administra las colecciones de usuarios, libros y préstamos.

---

##  Justificación de cada relación
- **Usuario–Prestamo**: necesaria para saber qué usuario solicitó cada libro.
- **Libro–Prestamo**: permite controlar disponibilidad y trazabilidad de cada ejemplar.
- **Biblioteca–Colecciones**: la biblioteca es el núcleo del sistema, por lo que debe centralizar la gestión.

---

##  Respuestas a las preguntas conceptuales
1. **¿Qué es una clave primaria?**  
   Es un atributo único que identifica de manera inequívoca cada registro en una tabla. Ejemplo: DNI en `Usuario`, ISBN en `Libro`.

2. **¿Qué es una clave foránea?**  
   Es un atributo que referencia la clave primaria de otra tabla, estableciendo relaciones entre ellas. Ejemplo: `dni_usuario` en `Prestamo` referencia a `Usuario`.

3. **¿Qué es integridad referencial?**  
   Es la regla que asegura que las claves foráneas siempre correspondan a registros existentes en la tabla referenciada.

---

##  Principales cambios respecto del TP N.º 1
- Se agregó la clase `Prestamo` para modelar la relación entre usuarios y libros.
- Se incorporó el uso de `random.randint` para generar identificadores aleatorios de préstamos.
- Se trasladó la lógica de registro de préstamos a la clase `Biblioteca`, evitando mezclar responsabilidades.
- Se implementó el método `devolucion` para cerrar préstamos y liberar libros.
- Se mejoró la representación de objetos con `__str__` para mayor claridad en la salida.

---

## Actividad 2 — Relaciones entre objetos

  ### Biblioteca — Libro 

  Objetos que participan: Objeto libro y objeto biblioteca 
 
- Un objeto necesita conocer a otro?  
  Si, biblioteca necesita conocer objeto libro 

- Los objetos pueden existir independientemente?
    Si, ya que si la biblioteca deja de existir, los libros siguen estando físicamente. En la relación de agregación, cada objeto puede desvincularse tranquilamente.  

- ¿Uno de los objetos administra una colección del otro?
    Si, biblioteca administra la colección de libros 

-¿Qué tipo de relación consideran que existe?
   La relación que existe es de agregación, uno a muchos.

  ### Biblioteca — Usuario

  Objetos que participan: Objeto biblioteca y objeto usuario 

- Un objeto necesita conocer a otro? 
   Si, biblioteca necesita conocer a los usuarios. 

- Los objetos pueden existir independientemente?
    Si, pueden. 

- ¿Uno de los objetos administra una colección del otro?
  Si, biblioteca administra la colección de usuarios 

- ¿Qué tipo de relación consideran que existe?
    La relación que existe es una relación de Asociacion. Uno a muchos (1:n) 


### Biblioteca — Prestamo 

   Objetos que participan: Objeto Biblioteca y objeto Prestamo 

- Un objeto necesita conocer a otro? 
    Si, biblioteca necesita conocer los prestamos para administrarlos 

- Los objetos pueden existir independientemente?
    En este caso no, por que sin biblioteca no hay prestamos. 

- ¿Uno de los objetos administra una colección del otro?
    Si, biblioteca administra la colección de prestamos 

- ¿Qué tipo de relación consideran que existe?
    La relación que se presenta entre estos objetos es de agregación. Uno a muchos (1:n) 


    ### Prestamo — Usuario 

    Objetos que participan: Objeto préstamo y objeto usuario 

- Un objeto necesita conocer a otro? 
    Si, el préstamo necesita saber que usuario lo solicita. 

- Los objetos pueden existir independientemente?
    No, el Prestamo depende de el usuario y la biblioteca 

- ¿Uno de los objetos administra una colección del otro? 
    No.  

- ¿Qué tipo de relación consideran que existe?
    La relación es de agregación. 1 a 1 


    ### Prestamo — Libro 

    Objetos que participan: objeto Prestamo y objeto Libro 

- Un objeto necesita conocer a otro? 
    Si, préstamo necesita conocer a Libro. 

- Los objetos pueden existir independientemente?
    No, préstamo depende de las demás clases. 

- ¿Uno de los objetos administra una colección del otro?
    Si, préstamo administra la colección de Libros 

- ¿Qué tipo de relación consideran que existe?
    Existe una relación de agregación


## Actividad 8 tp 2 IPOO 

- ¿Una biblioteca puede tener varios libros? 
    Si. Relacion: uno a muchos (1:n) 

●¿Una biblioteca puede tener varios usuarios?
  Si. Relacion: uno a muchos (1:n) 

● ¿Una biblioteca puede registrar varios préstamos?     
  Si, ya que una biblioteca tiene mas de un libro. Relacion: uno a muchos (1:n) 

● ¿Un usuario puede realizar varios préstamos? 
  Si. Relacion: uno a muchos (1:n) 

● ¿Un libro puede aparecer en varios préstamos a lo largo del tiempo?
  Si. Ya que un libro puede ser prestado y devuelvo, lo que su disponibilidad cambiaria a lo largo del tiempo. Relacion: uno a muchos (1:n) 

● ¿Cuántos usuarios y libros intervienen en un préstamo determinado?
  Por cada préstamo, interviene un libro y un usuario, ya que un libro no puede ser prestado a mas de un usuario. Relacion  uno a uno (1:1) 


## Preguntas conceptuales 

1. Relaciones 
¿Qué significa que dos objetos estén relacionados?  

  Que dos objetos estén relacionados significa que tienen una interaccion entre si, con la intención de poder lograr hacer una tarea especifica. 

2. Biblioteca y Libro 
¿Qué tipo de relación consideran que existe entre Biblioteca y Libro? 

  La relación que considero que hay entre libro y biblioteca es de agregación ya que la biblioteca dispone de objetos libros para realizar las tareas definidas, y esta relación es la que mas identifica a estos dos objetos en este caso 

3. Biblioteca y Usuario 
¿Qué relación existe entre Biblioteca y Usuario? ¿Puede existir un usuario independientemente de la biblioteca? 

  La relación que existe entre Biblioteca y Usuario es de asociación, ya que Usuarios no participa temporalmente en Biblioteca. Si, puede existir, por que sigue siendo persona, y en todo caso, se relacionaría con otra biblioteca, pero no en nuestro sistema.  

4. Prestamo 
¿Por qué Prestamo necesita relacionarse con un objeto Usuario y un objeto Libro?  

  Prestamo necesita relacionarse con Usuario y Libro por que necesitamos saber a que usuario le pertenece el préstamo, y además que libro solicita el usuario. 

5. Multiplicidad 
¿Qué diferencia existe entre la relación: Prestamo — Libro y Usuario — Prestamo? Consideren la cantidad de objetos involucrados.  

  La principal diferencia que se observa entre estas dos relaciones es que en Usuario — Prestamo se mantiene una referencia de usuario en préstamo, mientras que en Prestamo — Libro también se mantiene una referencia, pero es bi direccional ya que en préstamo tenemos la refencia a libros, y en libros tenemos al atributo encapsulado cant_prestamos, lo cual hace esta relación una relación bi direccional.  Se puede identificar solo esa diferencia, por que en multiplicidad ambas relaciones son 1:N. 

6. Responsabilidades 
¿Por qué la colección de libros debería encontrarse ahora dentro de Biblioteca y no directamente en main.py?  

  Ahora es necesario que los objetos estén definidos en biblioteca ya que es la clase encargada de gestionar los mismos, en cambio el main debe encargarse de ejecutar todo el código que hay detrás y solicitar datos al usuario tal y como dice el tp. 

7. Evolución del diseño 
¿Qué diferencias encuentran entre la solución desarrollada en el TP N.º 1 y la desarrollada en este trabajo? 

  Las principales diferencias de este tp y el anterior, son la agregación de nuevas clases y atributos, implementacion de relaciones entre obejtos, nuevas funciones para registrar usuarios, prestamos, devoluciones teniendo en cuenta cada usuario registrado, uso superficial de cardinalidades, etc…



