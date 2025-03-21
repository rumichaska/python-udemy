"""
Importación de paquetes y módulos
"""
from flask import Blueprint, render_template, request, redirect, url_for, current_app
import sendgrid
from sendgrid.helpers.mail import Email, To, Mail

bp = Blueprint("portfolio", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def index():
    """Plantilla de portafolio"""
    return render_template("portfolio/index.html")


@bp.route("mail", methods=["GET", "POST"])
def mail():
    """Formulario de contacto"""
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if request.method == "POST":
        send_email(name, email, message)
        return render_template("portfolio/sent_mail.html")

    return redirect(url_for("portfolio.index"))


def send_email(name, email, message):
    """Mandar email según formulario"""
    mi_email = "diego.acg@outlook.com"
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config["SENDGRID_KEY"])

    from_email = Email(mi_email)
    to_email = To(mi_email, substitutions={
        "-name-": name,
        "-email-": email,
        "-message-": message,
    })

    html_content = """
        <p>Hola Diego, tienes un nuevo contacto desde la web:</p>
        <p>Nombre: -name-</p>
        <p>Correo: -email-</p>
        <p>Mensaje: -message-</p>
    """

    mail = Mail(mi_email, to_email, "Nuevo contacto desde la web",
                html_content=html_content)
    response = sg.client.mail.send.post(request_body=mail.get())
