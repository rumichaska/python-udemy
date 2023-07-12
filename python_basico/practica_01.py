# INTRODUCCION Y PRIMEROS PASOS -------------------------------------------

# Primera linea de codigo
print("Hola mundo")

# Condicional con indentación
if 5 > 3:
    print("5 es mayor a 3")

# Condicional que no se cumple
if 5 < 4:
    print("Esto no se imprime")

# Declarando variables
x = 5
y = "Este es un string"
print(x, y)

nombre = "Diego"
apellido  = "Castro"
email = "castrogda@gmail.com"
edad = 33
sexo = "MASCULINO"
print(nombre, apellido, edad, sexo, email)

# Usualmente se usan variables con nombres en mayúscula cuando son constantes
# que no van a cambiar de valor. Otro punto importantes es que la variables no
# pueden empezar con numeros.

# Podemos nombrar mas de una variable en una misma línea
a, b , c = "Diego", 33, "años"
print(a, b, c)

# Otra forma de asignar un valor a multiples variables
valor1 = valor2 = valor3 = "la encarnación RA"
print(valor1, valor2, valor3)

# Concatenando variables
inicio = "Hola"
fin = "mundo"
print(inicio + " " + fin + ", Un texto aleatorio, funciona como paste0() de R")
