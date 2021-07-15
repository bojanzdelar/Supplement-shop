import flask
from flask import Blueprint
from flask_mail import Message
from config import mail

mail_bp = Blueprint("main", __name__)

@mail_bp.route("/", methods=["POST"])
def send_mail():
	data = flask.request.json
	msg = Message(subject="Message via musclepharm.com contact form", sender=data['email'], 
			recipients=["contact.musclepharm@gmail.com"], html=flask.render_template("mail.html", mail=data))
	mail.send(msg)
	return "Message sent"