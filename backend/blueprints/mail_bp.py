from flask import Blueprint, request, render_template
from flask_mail import Message
from config import mail

mail_bp = Blueprint("main", __name__)

@mail_bp.route("/", methods=["POST"])
def send_mail():
	data = request.json
	msg = Message(subject="Message via musclepharm.com contact form", sender=data['email'], 
			recipients=["contact.musclepharm@gmail.com"], html=render_template("mail.html", mail=data))
	try:
		mail.send(msg)
	except:
		return "Something went wrong. Please try again", 400
	return "Message sent"