import flask
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity   
from app import mysql

orders = Blueprint('orders', __name__)

@orders.route("/", methods=["GET"])
def get_all_order():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM order")
    return flask.jsonify(cursor.fetchall())

@orders.route("/<int:id>", methods=["GET"])
def get_order(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM orders WHERE id=%s", (id,))
    order = cursor.fetchone()
    return flask.jsonify(order) if order else ("", 404)

@orders.route("/", methods=["POST"])
@jwt_required(optional=True)
def create_order():
    order = flask.request.json
    order["user_id"] = get_jwt_identity()
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO orders(user_id, email, shipping_address_id, billing_address_id, shipping_method_id, payment_method_id, sent, delivered) "
            "VALUES(%(user_id)s, %(email)s, %(shipping_address_id)s, %(billing_address_id)s, %(shipping_method_id)s, %(payment_method_id)s, %(sent)s, %(delivered)s)", order)
    db.commit()
    cursor.execute("SELECT last_insert_id() AS id")
    return flask.jsonify(cursor.fetchone()), 201

@orders.route("/<int:id>", methods=["PUT"])
def update_order(id):
    order = flask.request.json
    order["id"] = id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE orders SET user_id=%(user_id)s, email=%(email)s, shipping_address_id=%(shipping_address_id)s, billing_address_id=%(billing_address_id)s, "
            "shipping_method_id=%(shipping_method_id)s, payment_method_id=%(payment_method_id)s, sent=%(sent)s, delivered=%(delivered)s "
            "WHERE id=%(id)s", order)
    db.commit()
    cursor.execute("SELECT * FROM order WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@orders.route("/<int:id>", methods=["DELETE"])
def delete_order(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM orders WHERE id=%s", (id,))
    db.commit()
    return ""