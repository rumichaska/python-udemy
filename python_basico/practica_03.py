# CONTROL DE FLUJO --------------------------------------------------------

# Condicionales - if

if 2 < 5:
    print("2 es menor que 5")

# tipos de evaluación
# a == b
# a < b
# a > b
# a != b
# a <= b
# a >= b
# tener en cuenta la indentación para evitar errores

if 2 == 2:
    print("2 es igual a 2")

if 2 == 3:
    print("2 es igual a 3")

if 5 > 2:
    print("5 es mayor que 2")

if 2 > 5:
    print("2 es mayor que 5")

if 2 != 3:
    print("2 es distinto a 3")

if 10 <= 10:
    print("10 es menor o igual a 10")

# Condicionales - elif

if 2 > 5:
    print("2 es menor a 5")
elif 2 < 5:
    print("2 es menor a 5")

# Condicionales - else

if 2 > 5:
    print("2 es menor a 5")
elif 2 > 3:
    print("2 es menor a 3")
else:
    print("solo se imprime si no se han satisfecho ninguna de las condiciones")

# Condicionales - if cortos

if 2 < 5: print("if en una sola línea")

# Operador ternario

print("cuando devuelve true") if 5 > 2 else print("cuando devuelve false")

# and y or

if 2 < 5 and 10 > 5:
    print("se cumplieron ambas condiciones")

if 2 < 5 or 3 > 5:
    print("se cumple una de las condiciones")
