"""Aplicativo de todo-list
Paquetes y modulos
"""
import os
from tkinter import Button
from flask import Flask


def create_app():
    """Inicializar app"""
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY="mikey",
        DATABASE_HOST=os.environ.get("FLASK_DATABASE_HOST"),
        DATABASE_PORT=os.environ.get("FLASK_DATABASE_PORT"),
        DATABASE_PASSWORD=os.environ.get("FLASK_DATABASE_PASSWORD"),
        DATABASE_USER=os.environ.get("FLASK_DATABASE_USER"),
        DATABASE=os.environ.get("FLASK_DATABASE"),
    )

    from . import db

    db.init_app(app)

    from . import auth
    from . import todo

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route("/hola")
    def hola():
        return "Chanchito feliz"

    return app
