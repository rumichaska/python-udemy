"""Module for connecting to MySQL server"""
import mysql.connector
from decouple import config

midb = mysql.connector.connect(
    host=config("MYSQL_HOST"),
    port=config("MYSQL_PORT"),
    user=config("MYSQL_USER"),
    password=config("MYSQL_PASSWORD"),
    database=config("MYSQL_DATABASE")
)

cursor = midb.cursor()

# NOTE: la función execute() permite realizar consultas sql

# Ingresar nueva información a la tabla
sql = "INSERT INTO Usuario (email, username, edad) VALUES (%s, %s, %s)"
values = ("diego.acg@outlook.com", "José", "45")
cursor.execute(sql, values)
midb.commit()
print(cursor.rowcount)

# Actualizar información de la tabla
sql = "UPDATE Usuario SET email = %s WHERE id = %s"
values = ("gaga@correo.com", 1)
cursor.execute(sql, values)
midb.commit()

# Eliminar información de la tabla
sql = "DELETE FROM Usuario WHERE id = %s"
values = (4, )  # NOTE: cuando se use 1 solo elemento, poner ', '
cursor.execute(sql, values)
midb.commit()

# Limitar información que se muestra en la consulta
cursor.execute("SELECT * FROM Usuario LIMIT 1")
resultado = cursor.fetchall()
print(resultado)

# Mostrar definición de tabla
# cursor.execute("SHOW CREATE TABLE Usuario")
# Listar información de la tabla
cursor.execute("SELECT * FROM Usuario")
# Capturar información de consulta
resultado = cursor.fetchall()
# fetchone() solo retorna el primer elemento de la consulta
# resultado = cursor.fetchone()
# Mostrar resultado de consulta
print(resultado)
