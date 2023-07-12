"""Module for connecting to MySQL server
Ejemplo usando variables de entorno y el modulo de virtualenv
"""
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

cursor.execute("SELECT * FROM Usuario")
resultado = cursor.fetchall()
print(resultado)
