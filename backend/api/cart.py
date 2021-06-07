import flask
from flask import Blueprint
from app import mysql

cart = Blueprint('cart', __name__)

@cart.route("/", methods=["GET"])
def get_all_cart():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM cart")
    return flask.jsonify(cursor.fetchall())

@cart.route("/<int:id>", methods=["GET"])
def get_cart(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM cart WHERE id=%s", (id,))
    cart = cursor.fetchone()
    return flask.jsonify(cart) if cart else ("", 404)

@cart.route("/", methods=["POST"])
def create_cart():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO cart(username, product_id, quantity, added) "
            "VALUES(%(username)s, %(product_id)s, %(quantity)s, %(added)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@cart.route("/<int:id>", methods=["PUT"])
def update_cart(id):
    cart = flask.request.json
    cart["id"] = id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE cart SET username=%(username)s, product_id=%(product_id)s, quantity=%(quantity)s, added=%(added)s "
            "WHERE id=%(id)s", cart)
    db.commit()
    cursor.execute("SELECT * FROM cart WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@cart.route("/<int:id>", methods=["DELETE"])
def delete_cart(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM cart WHERE id=%s", (id,))
    db.commit()
    return ""