import flask
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity   
from api.auth import admin_required   
from db import mysql

cart = Blueprint('cart', __name__)

@cart.route("/", methods=["GET"])
@admin_required()
def get_all_cart():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM cart")
    return flask.jsonify(cursor.fetchall())

@cart.route("/<string:product_id>", methods=["GET"])
@jwt_required()
def get_cart(product_id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM cart WHERE user_id=%s AND product_id=%s", (get_jwt_identity(), product_id))
    cart = cursor.fetchone()
    return flask.jsonify(cart) if cart else ("", 404)

@cart.route("/user", methods=["GET"])
@jwt_required()
def get_user_cart():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT cart.*, product.name, product.price, product.thumbnail FROM cart "
            "LEFT JOIN product ON cart.product_id=product.id WHERE user_id=%s", (get_jwt_identity(), ))
    return flask.jsonify(cursor.fetchall())

@cart.route("/", methods=["POST"])
@jwt_required()
def add_to_cart():
    item = flask.request.json
    item["user_id"] = get_jwt_identity()
    db = mysql.get_db()
    cursor = db.cursor()

    cursor.execute("SELECT deleted FROM product WHERE id=%s", (item["product_id"]))
    product = cursor.fetchone()
    if product["deleted"]:
        return "You can't add deleted products to cart", 405

    cursor.execute("SELECT * FROM cart WHERE user_id=%(user_id)s AND product_id=%(product_id)s", item)
    item_in_cart = cursor.fetchone()

    if item_in_cart:
        item_in_cart["quantity"] += item["quantity"]
        cursor.execute("UPDATE cart SET quantity=%(quantity)s WHERE id=%(id)s", item_in_cart)
    else:
        cursor.execute("INSERT INTO cart(user_id, product_id, quantity) "
                "VALUES(%(user_id)s, %(product_id)s, %(quantity)s)", item)

    db.commit()
    cursor.execute("SELECT * FROM cart WHERE user_id=%(user_id)s AND product_id=%(product_id)s", item)
    return flask.jsonify(cursor.fetchone()), 201

@cart.route("/<string:product_id>", methods=["PUT"])
@jwt_required()
def update_cart(product_id):
    cart = flask.request.json
    cart["user_id"] = get_jwt_identity()
    cart["product_id"] = product_id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE cart SET user_id=%(user_id)s, product_id=%(product_id)s, quantity=%(quantity)s "
            "WHERE id=%(id)s", cart)
    db.commit()
    cursor.execute("SELECT * FROM cart WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@cart.route("/<string:product_id>", methods=["DELETE"])
@jwt_required()
def delete_cart(product_id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM cart WHERE user_id=%s AND product_id=%s", (get_jwt_identity(), product_id))
    db.commit()
    return ""

@cart.route("/user", methods=["DELETE"])
@jwt_required()
def delete_user_cart():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM cart WHERE user_id=%s", (get_jwt_identity(), ))
    db.commit()
    return ""