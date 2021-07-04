from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from db import mysql
from api.auth import auth
from api.address import address
from api.cart import cart
from api.category import category
from api.comment import comment
from api.orders import orders
from api.payment_method import payment_method
from api.product_in_category import product_in_category
from api.product_in_order import product_in_order
from api.product import product
from api.shipping_method import shipping_method
from api.user import user

app = Flask(__name__, static_url_path="")
mysql.init_app(app)
jwt = JWTManager(app)
cors = CORS(app, resources={r"/api/*": {"origins": [
        "http://127.0.0.1:8080", "http://localhost:8080"]}}, supports_credentials=True)

app.url_map.strict_slashes = False # prevents 308 status code for CORS preflight

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "shop"
app.config["JWT_SECRET_KEY"] = "1[as42_^!1251yui"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

app.register_blueprint(auth, url_prefix="/api")
app.register_blueprint(address, url_prefix="/api/address")
app.register_blueprint(cart, url_prefix="/api/cart")
app.register_blueprint(category, url_prefix="/api/category")
app.register_blueprint(comment, url_prefix="/api/comment")
app.register_blueprint(orders, url_prefix="/api/orders")
app.register_blueprint(payment_method, url_prefix="/api/payment-method")
app.register_blueprint(product_in_category, url_prefix="/api/product-in-category")
app.register_blueprint(product_in_order, url_prefix="/api/product-in-order")
app.register_blueprint(product, url_prefix="/api/product")
app.register_blueprint(shipping_method, url_prefix="/api/shipping-method")
app.register_blueprint(user, url_prefix="/api/user")    

if __name__ == "__main__":
    app.run()