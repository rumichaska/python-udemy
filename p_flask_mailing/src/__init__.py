"""Aplicativo para mailing
Importación de paquetes y módulos
"""
import os
from flask import Flask

from . import db
from . import mail


def create_app():
    """Inicializar app"""
    app = Flask(__name__)

    app.config.from_mapping(
        FROM_EMAIL=os.environ.get("FROM_EMAIL"),
        FLASK_DEBUG=os.environ.get("FLASK_DEBUG"),
        SENDGRID_API_KEY=os.environ.get("SENDGRID_API_KEY"),
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        DATABASE_HOST=os.environ.get("FLASK_DATABASE_HOST"),
        DATABASE_PORT=os.environ.get("FLASK_DATABASE_PORT"),
        DATABASE_USER=os.environ.get("FLASK_DATABASE_USER"),
        DATABASE_PASSWORD=os.environ.get("FLASK_DATABASE_PASSWORD"),
        DATABASE=os.environ.get("FLASK_DATABASE")
    )

    db.init_app(app)

    app.register_blueprint(mail.bp)

    return app
