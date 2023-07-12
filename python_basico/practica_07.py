# MODULOS -----------------------------------------------------------------

# Para utilizar el módulo creado en modulos.py
import modulos

# Para acceder a la lista de nombres
print(modulos.mascotas)

# Para acceder a la función saludo()
modulos.saludo("Juan")

# Para cambiar el nombre al módulo podemos hacerlo de la siguiente manera:
import modulos as xs

print(xs.mascotas)
xs.saludo("José")

# Para acceder solo a un componente del módulo
# from modulos import saludo
from modulos import saludo, mascotas  # NOTE: para mas de un objeto

print(mascotas)
saludo("María")

# NOTE: pip es un gestor de módulos de python. El simil de pip install con R es
# install.packages("paquete"), sin embargo este gestor se ejecuta desde
# terminal y no desde la consola de python. Podría decirse que pip install es
# un 'wraper' equivalente a R -e "install.packages('paquete')" ejecutado en
# terminal

# Comandos útiles para usar pip install:
# pypi.org tiene un listado de los módulos de python
# en caso de no contar con pip, instalarlo con sudo apt install python3-pip

from camelcase import CamelCase

c = CamelCase()
s = "esta frase necesita camelcase"

camelcased = c.hump(s)
print(camelcased)

# pip list nos listará todos los módulos instalados
# para quitar un modulo pip uninstall modulo
