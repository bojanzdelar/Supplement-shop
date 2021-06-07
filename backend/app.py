import flask
from flask import Flask

from flaskext.mysql import MySQL, pymysql

app = Flask(__name__, static_url_path="")

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "shop"

mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)

import api.comment
import api.user
import api.cart
import api.product
import api.category

if __name__ == "__main__":
    app.run()