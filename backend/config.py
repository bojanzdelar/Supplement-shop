from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail, Message

from db import mysql

app = Flask(__name__, static_url_path="")

app.url_map.strict_slashes = False # prevents 308 status code for CORS preflight

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "shop"
app.config["JWT_SECRET_KEY"] = "1[as42_^!1251yui"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'contact.musclepharm@gmail.com'
app.config['MAIL_PASSWORD'] = 'Contact.musclepharm123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mysql.init_app(app)
jwt = JWTManager(app)
cors = CORS(app, resources={r"/api/*": {"origins": [
        "http://127.0.0.1:8080", "http://localhost:8080"]}}, supports_credentials=True)
mail = Mail(app)