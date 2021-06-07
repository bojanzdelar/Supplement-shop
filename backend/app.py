from flask import Flask
from flaskext.mysql import MySQL, pymysql

from api.cart import cart
from api.category import category
from api.comment import comment
from api.product import product
from api.user import user

app = Flask(__name__, static_url_path="")
mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "shop"

app.register_blueprint(cart, url_prefix="/api/cart")
app.register_blueprint(category, url_prefix="/api/category")
app.register_blueprint(comment, url_prefix="/api/comment")
app.register_blueprint(product, url_prefix="/api/product")
app.register_blueprint(user, url_prefix="/api/user")

app.run()