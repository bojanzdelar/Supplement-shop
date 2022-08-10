from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail

app = Flask(__name__, static_url_path="")

app.url_map.strict_slashes = False # prevents 308 status code for CORS preflight

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:3306/shop"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["JWT_SECRET_KEY"] = "1[as42_^!1251yui"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'contact.musclepharm@gmail.com'
app.config['MAIL_PASSWORD'] = 'Contact.musclepharm123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
cors = CORS(app, resources={r"/api/*": {"origins": [
        "http://127.0.0.1:8080", "http://localhost:8080"]}}, supports_credentials=True)
mail = Mail(app)