import flask
from flask import Blueprint
from app import mysql

order = Blueprint('order', __name__)

@order.route("/", methods=["GET"])
def get_all_order():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM order")
    return flask.jsonify(cursor.fetchall())

@order.route("/<int:id>", methods=["GET"])
def get_order(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM order WHERE id=%s", (id,))
    order = cursor.fetchone()
    return flask.jsonify(order) if order else ("", 404)

@order.route("/", methods=["POST"])
def create_order():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO order(user_id, shipping_address, billing_address, shipping_method, payment_method, sent, delivered) "
            "VALUES(%(user_id)s, %(shipping_address)s, %(billing_address)s, %(shipping_method)s, %(payment_method)s, %(sent)s, %(delivered)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@order.route("/<int:id>", methods=["PUT"])
def update_order(id):
    order = flask.request.json
    order["id"] = id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE order SET user_id=%(user_id)s, shipping_address=%(shipping_address)s, billing_address=%(billing_address)s, shipping_method=%(shipping_method)s, payment_method=%(payment_method)s, sent=%(sent)s, delivered=%(delivered)s "
            "WHERE id=%(id)s", order)
    db.commit()
    cursor.execute("SELECT * FROM order WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@order.route("/<int:id>", methods=["DELETE"])
def delete_order(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM order WHERE id=%s", (id,))
    db.commit()
    return ""