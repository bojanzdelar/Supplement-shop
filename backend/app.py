from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from db import mysql
from api.auth import auth
from api.cart import cart
from api.category import category
from api.comment import comment
from api.product import product
from api.user import user

app = Flask(__name__, static_url_path="")
mysql.init_app(app)
jwt = JWTManager(app)
cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:8080"}},
        supports_credentials=True)

app.url_map.strict_slashes = False # prevents 308 status code for CORS preflight

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "shop"
app.config["JWT_SECRET_KEY"] = "1[as42_^!1251yui"

app.register_blueprint(auth, url_prefix="/api")
app.register_blueprint(cart, url_prefix="/api/cart")
app.register_blueprint(category, url_prefix="/api/category")
app.register_blueprint(comment, url_prefix="/api/comment")
app.register_blueprint(product, url_prefix="/api/product")
app.register_blueprint(user, url_prefix="/api/user")    

if __name__ == "__main__":
    app.run()