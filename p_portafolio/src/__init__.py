"""Proyecto de portafolio
Impotación de paquetes y módulos
"""
import os
from flask import Flask

from . import portfolio


def create_app():
    """Función para iniciar app"""
    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get("SENDGRID_KEY")
    )

    app.register_blueprint(portfolio.bp)

    return app
