# TIPOS DE DATOS ----------------------------------------------------------

# TEXTO

# Datos de tipo string o cadena de texto, se puede usar comillas simples o
# comillas dobles
palabra = "Esta es una variable de tipo string"

# NUMEROS

# Número enteros
entero = 28

# Número tipo float
decimal = 3.45

# Número complejos, se definen agregando una j
complejo = 1j

# Vamos a mostrar los resultados
print(palabra, entero, decimal, complejo)

# LISTAS

# Listas, colección de datos o varios datos agrupados
lista = []  # Lista vacía
print(lista)

# Lista con datos
lista_2 = [1, 2, 3]
print(lista_2)

# Copiar lista
lista_3 = lista_2.copy()

# Agregando valores a lista
lista_2.append(4)  # Método append

# Elimina los elementos de una lista
# lista_2.clear()
print(lista_2, lista_3)

# Para contar cuantas veces se repite un valor
print(lista_2, lista_2.count(2))  # Debemos indicar el valor a contar

# Para contar elementos de un objeto
print(len(lista_3), len(lista_2))  # Longitud, similar a length() de R

# Para acceder a elementos de una lista. Recordar que en python el primer
# elemento es 0
lista = ["hola", "diego", "32", "como", "estas", "guapo", 33]
print(lista[1])  # Similar a R pero contando desde 0

# Eliminando elementos de una lista
lista.pop()  # Elimina el último elemento de una lista
print(lista)

lista.remove("diego")  # Elimina un elemento en una posición
print(lista)

# Ordenar lista
lista.reverse()
print(lista)

lista.sort()  # El ordenamiento solo funciona con valores del mismo tipo
print(lista)

# TUPLAS
# Son parecidas a las listas pero su valores no se pueden modificar, tienen
# menos métodos que las listas, no se puede usar el método de append
tupla = ("Hola", "mundo", "somos", "tupla")
print(tupla)

# Contar elemento y ver la posición
print(tupla.count("tupla"), tupla.index("Hola"))

# Para modificar una tupla se debe convertir a una lista
listaTupla = list(tupla)
listaTupla.append("sol")
print(listaTupla)

# RANGOS
rango = range(8)
print(rango)

# DICCIONARIOS

diccionario = {
    "nombre": "Diego",
    "apellido": "Castro",
    "edad": 33,
    "profesion": "Ing. Foretal",
    "sexo": "Masculino"
}

print(diccionario)

# Formas de acceder a los valores del diccionario
print(diccionario["nombre"])
print(diccionario.get("apellido"))

# Cambiar un valor del diccionario
diccionario["nombre"] = "Dante"
print(diccionario)

# Para conocer la cantidad de elementos del diccionario
print(len(diccionario))

# Para agregar valores
diccionario["estado_civil"] = "Soltero"
print(diccionario)

# Formas para copiar un diccionario
copiaDiccionario = diccionario.copy()
copiaDiccionario2 = dict(diccionario)
print(copiaDiccionario)
print(copiaDiccionario2)

# Formas para eliminar valores
diccionario.pop("apellido")
diccionario.popitem() # Elimina el último valor añadido
del diccionario["profesion"]
print(diccionario)

# Para eliminar todos los elementos
copiaDiccionario.clear()
print(copiaDiccionario)

# Crear diccionario anidados
gatitos = {
    "Valentina": {
        "edad": 3,
        "sexo": "Hembra"
    },
    "Danton": {
        "edad": 3,
        "sexo": "Macho"
    },
    "Pantro": {
        "edad": 2.5,
        "sexo": "Macho"
    },
    "Estrellita": {
        "edad": 2,
        "sexo": "Hembra"
    }
}
print(gatitos)

# Formas para acceder a los valores de diccionarios anidados
print(gatitos.get("Pantro"))
print(gatitos["Valentina"]["edad"])

# Crear diccionarios con la funcion dict()
alumno1 = dict(nombre = "Juan", apellido = "Pastor", edad = 32)
print(alumno1)

# BOOLEANOS

verdadero = True
falso = False
print(verdadero)
print(falso)
