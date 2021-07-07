import flask
from flask import Blueprint
from api.auth import admin_required
from app import mysql

product = Blueprint('product', __name__)

@product.route("/", methods=["GET"])
def get_all_product():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product")
    return flask.jsonify(cursor.fetchall())

@product.route("/<string:id>", methods=["GET"])
def get_product(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product WHERE id=%s", (id,))
    product = cursor.fetchone()
    return flask.jsonify(product) if product else ("", 404)

@product.route("/<string:id>/quantity", methods=["GET"])
def get_product_quantity(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT quantity FROM product WHERE id=%s", (id,))
    quantity = cursor.fetchone()
    return flask.jsonify(quantity) if quantity else ("", 404)

@product.route("/search/<string:query>", methods=["GET"])
def search_product(query):
    query = f"%{query}%"
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product WHERE name LIKE %s OR description LIKE %s", (query, query))
    return flask.jsonify(cursor.fetchall())

@product.route("/", methods=["POST"])
@admin_required()
def create_product():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO product(name, description, price, quantity, image, category_id) "
            "VALUES(%(name)s, %(description)s, %(price)s, %(quantity)s, %(image)s, %(category_id)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@product.route("/<string:id>", methods=["PUT"])
@admin_required()
def update_product(id):
    product = flask.request.json
    product["id"] = id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE product SET name=%(name)s, description=%(description)s, price=%(price)s, quantity=%(quantity)s, image=%(image)s, category_id=%(category_id)s "
            "WHERE id=%(id)s", product)
    db.commit()
    cursor.execute("SELECT * FROM product WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@product.route("/<string:id>", methods=["DELETE"])
@admin_required()
def delete_product(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM product WHERE id=%s", (id,))
    db.commit()
    return ""