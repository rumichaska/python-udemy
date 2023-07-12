# OBJETOS CLASES Y HERENCIAS ----------------------------------------------

# CLASES ------------------------------------------------------------------

# Clases
class Usuario:
    # Propiedades de la clase
    nombre = "Diego"
    apellido = "Castro"

usuario = Usuario()
usuario2 = Usuario()

print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

# Para crear una clase con varias propiedades
class Mascota:
    # definiendo método __init__
    def __init__(self, nombre, dueño):
        # 'self' hace una referencia a sí mismo
        self.nombre = nombre
        self.dueño = dueño

mascota = Mascota("Danton", "Diego")
mascota2 = Mascota("Valentina", "Gladys")

print("La mascota es: " + mascota.nombre + " y el dueño es: " + mascota.dueño)
print(mascota2.nombre, mascota2.dueño)

# Método para crear un saludo con la información del nombre y apellido
class Saludo:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def saludo(self):
        print("Hola! mi nombre es", self.nombre, self.apellido)
    # NOTE: podemos cambiar el valor de 'self' por cualquier otro. 'self' es
    # una convención, de preferencia usarlo siempre.

# Para definir las propiedades del usuario
usuario = Saludo("Diego", "Castro")
usuario2 = Saludo("Carmen", "Pérez")

# Para llamar el método saludo
usuario.saludo()
usuario2.saludo()

# También podemos cambiar los valores
usuario.nombre = "David"
usuario.saludo()

# También podemos eliminar los valores
# del usuario.nombre  # NOTE: sale un error porque no tenemos un valor en la instancia
# usuario.saludo()

# También podemos eliminar un objeto
# del usuario
# print(usuario)

# HERENCIA ----------------------------------------------------------------

class Admin(Saludo):
    def superSaludo(self):
        print("Hola! me llamo,", self.nombre, "y soy administrador")

# NOTE: no vamos a poder llamar a los métodos ni propiedades de las clases
# hijos. Clase padre Admin, clase hijo Saludo. usuario.superSaludo() no se
# puede ejecutar, arroja error
admin = Admin("Super", "administrador")
admin.saludo()
admin.superSaludo()

# EJERCICIOS --------------------------------------------------------------

# PASO 1: creando 2 clase, una para gato y otra para perro

# class Gato:
#     def __init__(self, nombre, onomatopeya):
#         self.nombre = nombre
#         self.onomatopeya = onomatopeya
#
#     def saludo(self):
#         print("Hola, soy un gato y mi sonido es el", self.onomatopeya)
#
# class Perro:
#     def __init__(self, nombre, onomatopeya):
#         self.nombre = nombre
#         self.onomatopeya = onomatopeya
#
#     def saludo(self):
#         print("Hola, soy un perro y mi sonido es el", self.onomatopeya)
#
# gato = Gato("Valentina", "maullido")
# gato.saludo()
#
# perro = Perro("Oddy", "ladrido")
# perro.saludo()

# PASO 2: generalizando los métodos comunes, nombre y onomatopeya

# class Animal:
#     def __init__(self, nombre, onomatopeya):
#         self.nombre = nombre
#         self.onomatopeya = onomatopeya
#
# class Gato(Animal):
#     def saludo(self):
#         print("Hola, soy un gato y mi sonido es el", self.onomatopeya)
#
# class Perro(Animal):
#     def saludo(self):
#         print("Hola, soy un perro y mi sonido es el", self.onomatopeya)
# gato = Gato("Valentina", "maullido")
# gato.saludo()
#
# perro = Perro("Oddy", "ladrido")
# perro.saludo()

# PASO 3: generralizando los métodos para identificar el tipo de animal

class Animal:
    def __init__(self, especie, nombre, onomatopeya):
        self.especie = especie
        self.nombre = nombre
        self.onomatopeya = onomatopeya

class Especie(Animal):
    def saludo(self):
        print("Hola, soy un", self.especie, "y mi sonido es el", self.onomatopeya)

gato = Especie("gato", "Valentina", "maullido")
gato.saludo()

perro = Especie("perro", "Oddy", "ladrido")
perro.saludo()

# PASO 3A: alternativamente (udemy)

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print("Hola, soy un", self.tipo, "y mi sonido es el", self.onomatopeya)

# Extender el método de __init__ de la clase hijo
class Gato(Animal):
    tipo = "gato"
    # Cuando iniciamos un __init__, ignoramos el __init__ de la clase padre
    def __init__(self, nombre, onomatopeya):
        # Para pasar el __init__ de la clase padre, debemos hacer los siguiente:
        Animal.__init__(self, nombre, onomatopeya)
        print("Hola, soy un gato extendido")

# Extender el método __init__ de la clase padre
class Perro(Animal):
    tipo = "perro"
    def __init__(self, nombre, onomatopeya):
        # super() hace referencia a la clase padre
        super().__init__(nombre, onomatopeya)
        print("instanciando un perro")

class Canario(Animal):
    tipo = "canario"

gato = Gato("Valentina", "maullido")
gato.saludo()

perro = Perro("Oddy", "ladrido")
perro.saludo()

canario = Canario("Turtupillin", "silbido")
canario.saludo()
