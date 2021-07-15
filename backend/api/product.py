import flask
from flask import Blueprint
from api.auth import admin_required
from db import mysql

product = Blueprint('product', __name__)

@product.route("/", methods=["GET"])
def get_all_product():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product")
    return flask.jsonify(cursor.fetchall())

@product.route("/popular/<int:limit>", methods=["GET"])
def get_popular_product(limit):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product ORDER BY views DESC LIMIT %s", (limit,))
    return flask.jsonify(cursor.fetchall())

@product.route("/<string:id>", methods=["GET"])
def get_product(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM product WHERE id=%s", (id,))
    product = cursor.fetchone()
    if not product:
        return "", 404
    cursor.execute("UPDATE product SET views=%s WHERE id=%s", (product["views"] + 1, id))
    db.commit()
    return flask.jsonify(product)

@product.route("/<string:id>/quantity", methods=["GET"])
def get_product_quantity(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT quantity FROM product WHERE id=%s", (id,))
    quantity = cursor.fetchone()
    return flask.jsonify(quantity) if quantity else ("", 404)

@product.route("/<string:id>/categories", methods=["GET"])
def get_products_categories(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT category_id FROM product_in_category WHERE product_id=%s", (id,))
    categories = cursor.fetchall()
    return flask.jsonify(categories) if categories else ("", 404)

@product.route("/search/<string:query>", methods=["GET"])
def search_product(query):
    query = f"%{query}%"
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product WHERE name LIKE %s OR description LIKE %s", (query, query))
    return flask.jsonify(cursor.fetchall())

@product.route("/", methods=["POST"])
@admin_required()
def create_product():
    product = flask.request.json
    product["id"] = product["name"].replace(" ", "-").lower()
    product.setdefault("description", None)
    product.setdefault("thumbnail", None)
    product.setdefault("image", None)
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO product(id, name, description, price, quantity, image) "
            "VALUES(%(id)s, %(name)s, %(description)s, %(price)s, %(quantity)s, %(image)s)", product)
    db.commit()
    return flask.jsonify(product), 201

@product.route("/<string:id>", methods=["PUT"])
@admin_required()
def update_product(id):
    product = flask.request.json
    product["old_id"] = id
    product["id"] = product["name"].replace(" ", "-").lower()
    product.setdefault("description", None)
    product.setdefault("thumbnail", None)
    product.setdefault("image", None)
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE product SET id=%(id)s, name=%(name)s, description=%(description)s, price=%(price)s, quantity=%(quantity)s, image=%(image)s "
            "WHERE id=%(old_id)s", product)
    db.commit()
    cursor.execute("SELECT * FROM product WHERE id=%s", (product["id"],))
    return flask.jsonify(cursor.fetchone()), 200

@product.route("/<string:id>", methods=["DELETE"])
@admin_required()
def delete_product(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM product WHERE id=%s", (id,))
    db.commit()
    return ""