# CONTROL DE FLUJO --------------------------------------------------------

# WHILE LOOP

i = 0
while i < 5:
    print(i)
    # i += 1
    i = i + 1

# while utilizando break
j = 0
while j < 5:
    print(j)
    if j == 3:
        break
    j += 1

# while utilizando continue
k = 0
while k < 5:
    # Forma incorrecta, causa un loop infinito
    # print(k)
    # if k == 3:
    #     break
    # k += 1
    k += 1
    if k == 3:
        continue
    print(k)
    
# FOR LOOP

# Iterando sobre una lista de usuarios
usuarios = ["Juan", "Diego", "José", "Kevin", "Pierre"]
for usuario in usuarios:
    # Mostramos cada uno de los usuarios de la lista
    print(usuario)

# Iterando sobre un string
refran = "camarón que se duerme..."
for c in refran:
    # Mostramos cada caracter del string
    print(c)

# Iterando utilizando break
usuarios = ["Juan", "Diego", "José", "Kevin", "Pierre"]
for usuario in usuarios:
    if usuario == "Kevin":
        # En este caso la iteración termina cuando ocurre Kevin
        break
    # Mostramos cada uno de los usuarios de la lista
    print(usuario)

# Iterando utilizando continue
usuarios = ["Juan", "Diego", "José", "Kevin", "Pierre"]
for usuario in usuarios:
    if usuario == "José":
        # En este caso salta a José
        continue
    # Mostramos cada uno de los usuarios de la lista
    print(usuario)

# Iterando usando range y else
for x in range(2, 10, 2):  # Similar a seq() de R
    print(x)
else:
    print("Hemos terminado!!!")

# for loop anidado
usuarios = ["Juan", "Diego", "José", "Kevin", "Pierre"]
edades = [12, 32, 33, 21, 23]
for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)

# FUNCIONES ---------------------------------------------------------------

# Creando función
def miFuncion():
    print("Mi primera función")
# Llamando función
miFuncion()

# Función para imprimir dato
def imprimeDato(arg1):
    print("Mi argumento es", arg1)
imprimeDato("gaa!!!") 

# Función para sumar 2 números
def sumaDos(numero1, numero2):
    suma = int(numero1) + int(numero2)
    print("La suma es :", suma)
sumaDos(1, 5)

# Función con argumentos variables, se utiliza el símbolo reservado de "*"
def nombresTuplas(*nombre):
    print("Los valores son:", nombre)
    # Para acceder a los elementos
    print("El valor X es:", nombre[0])
# Los parámetros se muestran como una tupla
nombresTuplas("Juan", "José", "Pablo", "Jonás")

# Función utilizando kwargs (key word args), pasando como lista los argumentos
def nombreCompleto(**kwargs):
    print(kwargs["nombre"], kwargs["apellido"])
nombreCompleto(nombre = "Diego", apellido = "Castro")
nombreCompleto(nombre = "Carmen", apellido = "Pérez")

# Función con un argumento con un parámetro por defecto
def nombreCompleto2(nombre, apellido = "sin apellido"):
    print("El nombre completo es:", nombre, apellido)
nombreCompleto2("Diego")
nombreCompleto2("Carmen", "Pérez")

# Función pasando una lista como argumento
def miFuncionLista(lista):
    for el in lista:
        print(el)
miFuncionLista(["Diego", "Juan", "Gil", "Harold"])

# Función concatenando elementos
def concatenaNombres(lista):
    # Creamos un string vacío
    i = ""
    # Creamos un loop para concatenar el string
    for el in lista:
        i = i + el + " "
    return i
resultado = concatenaNombres(["Diego", "Juan", "Gil", "Harold"])
print(resultado)

# RECURSIVIDAD ------------------------------------------------------------

# La recursividad puede funcionar para realizar intentos, por ejemplo el
# llamado a un servidor o el intento de acceso a uno
def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)
recursion(5)
