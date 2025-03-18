"""Conexión a base de datos
Importación de paquetes y módulos
"""
import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext

from .schema import instructions


def get_db():
    """Conectar a servidor MySQL"""
    if "db" not in g:
        g.db = mysql.connector.connect(
            host=current_app.config["DATABASE_HOST"],
            port=current_app.config["DATABASE_PORT"],
            user=current_app.config["DATABASE_USER"],
            password=current_app.config["DATABASE_PASSWORD"],
            database=current_app.config["DATABASE"]
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c


def close_db(e=None):
    """Cerrar conexión a la base de datos"""
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Crear base de datos"""
    db, c = get_db()

    for i in instructions:
        c.execute(i)

    db.commit()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Ejecutar inicialización de la base de datos desde linea de comandos"""
    init_db()
    click.echo("Base de datos inicializada")


def init_app(app):
    """Iniciar app con base de datos"""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
