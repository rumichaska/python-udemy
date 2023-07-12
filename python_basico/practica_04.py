# EJERCICIO ---------------------------------------------------------------

# input, solicitando información al usuario

dato = input("Ingrese dato: ")
print(dato)

# Calculadora 1

print("ESTA INICIANDO LA PRIMERA CALCULADORA")

valor1 = input("Ingrese primer número: ")
valor2 = input("Ingrese segundo número: ")

# Importante transformar los número a enteros, sino se consideran cadena de
# texto y al utilizar + se combina el texo pero no se realiza el cálculo
suma = int(valor1) + int(valor2)

print(suma)

# Es importante considerar una validación de información para no convertir a
# entero una cadena de texto, esto nos puede traer un error luego

# Calculadora 2

print("ESTA INICIANDO LA SEGUNDA CALCULADORA")

primerValor = input("Ingrese primer número: ")
# Para validar el valor númerico
try:
    primerValor = int(primerValor)
except:
    primerValor = "no es un valor númerico"

segundoValor = input("Ingrese segundo número: ")
# Para validar el valor númerico
try:
    segundoValor = int(segundoValor)
except:
    segundoValor = "no es un valor númerico" 

# Condicional para sumar
if primerValor == "no es un valor númerico" or segundoValor == "no es un valor númerico":
    print("Ingresaste mal un dato, prueba de nuevo con solo números")
else:
    # En la sección de try ya se hizo la conversión
    print(primerValor + segundoValor)

# Calculadora 3

print("ESTA INICIANDO LA TERCERA CALCULADORA")

# Para validar el valor númerico
primerValor = input("Ingrese primer número: ")

try:
    primerValor = int(primerValor)
except:
    primerValor = "no es numero"

# Terminar sesión cuando no se cumpla la condición
if primerValor == "no es numero":
    print("El valor ingresado no es un número")
    exit()

# Para validar el valor númerico
segundoValor = input("Ingrese segundo número: ")

try:
    segundoValor = int(segundoValor)
except:
    segundoValor = "no es numero" 

# Terminar sesión cuando no se cumpla la condición
if segundoValor == "no es numero":
    print("El valor ingresado no es un número")
    exit()

print(primerValor + segundoValor)

# Calculadora 4

print("ESTA INICIANDO LA CUARTA CALCULADORA")

# Para validar el valor númerico
primerValor = input("Ingrese primer número: ")

try:
    primerValor = int(primerValor)
except:
    primerValor = "no es numero"

# Terminar sesión cuando no se cumpla la condición
if primerValor == "no es numero":
    print("El valor ingresado no es un número")
    exit()

# Para validar el valor númerico
segundoValor = input("Ingrese segundo número: ")

try:
    segundoValor = int(segundoValor)
except:
    segundoValor = "no es numero" 

# Terminar sesión cuando no se cumpla la condición
if segundoValor == "no es numero":
    print("El valor ingresado no es un número")
    exit()

# Vamos a considera el operador para realizar lo cálculos

simbolo = input("Ingrese la operación: ")

if simbolo == "+":
    print("Suma: ", primerValor + segundoValor)
elif simbolo == "-":
    print("Resta: ", primerValor - segundoValor)
elif simbolo == "*":
    print("Producto: ", primerValor * segundoValor)
elif simbolo == "/":
    print("División: ", primerValor / segundoValor)
else:
    print("El simbolo ingresado no es válido")
