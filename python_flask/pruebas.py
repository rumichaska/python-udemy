# pylint: disable=import-error disable=missing-function-docstring disable=missing-module-docstring
from flask import Flask, request, url_for, redirect, abort, render_template

app = Flask(__name__)

import mysql.connector

midb = mysql.connector.connect(
    host="192.168.0.10",
    port="33060",
    user="udemy",
    password="1566sql+",
    database="udemy_db"
)

cursor = midb.cursor(dictionary=True)

@app.route("/")
def index():
    return "hola mundo"


# métodos disponibles: GET, POST, PUT, PATCH, DELETE
# POST y GET se puede separar en métodos separados
@app.route("/post/<post_id>", methods=["GET", "POST"])
def lala(post_id):
    if request.method == "GET":
        return "El id del post es:" + post_id
    else:
        return "Este es otro método y no GET"


@app.route("/lele", methods=["POST", "GET"])
def lele():
    cursor.execute("SELECT * FROM Usuario")
    usuarios = cursor.fetchall()
    print(usuarios)
    # abort(403)
    # return redirect(url_for("lala", post_id=2))
    # print(request.form)
    # print(request.form["llave1"])
    # print(request.form["llave2"])
    # return render_template("lele.html")
    # return {
    #     "username": "Chanchito feliz",
    #     "email": "gaga@gmail.com"
    # }
    return render_template("lele.html", usuarios=usuarios)

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", mensaje="Hola mundo")

@app.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        edad = request.form["edad"]
        sql = "INSERT INTO Usuario (username, email, edad) VALUES (%s, %s, %s)"
        values = (username, email, edad)
        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for("lele"))
    return render_template("crear.html")
