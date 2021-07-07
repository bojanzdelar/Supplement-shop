import flask
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity   
from app import mysql

orders = Blueprint('orders', __name__)

@orders.route("/", methods=["GET"])
def get_all_order():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT orders.*, shipping_method.name AS shipping_method_name, payment_method.name AS payment_method_name "
        "FROM orders "
        "LEFT JOIN shipping_method ON orders.shipping_method_id = shipping_method.id "
        "LEFT JOIN payment_method ON orders.payment_method_id = payment_method.id")
    return flask.jsonify(cursor.fetchall())

@orders.route("/<int:id>", methods=["GET"])
def get_order(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT orders.*, shipping_method.name AS shipping_method_name, payment_method.name AS payment_method_name "
        "FROM orders "
        "LEFT JOIN shipping_method ON orders.shipping_method_id = shipping_method.id "
        "LEFT JOIN payment_method ON orders.payment_method_id = payment_method.id "
        "WHERE orders.id=%s", (id,))    
    order = cursor.fetchone()
    return flask.jsonify(order) if order else ("", 404)

@orders.route("/user", methods=["GET"])
@jwt_required()
def get_user_orders():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT orders.*, shipping_method.name AS shipping_method_name, payment_method.name AS payment_method_name "
        "FROM orders "
        "LEFT JOIN shipping_method ON orders.shipping_method_id = shipping_method.id "
        "LEFT JOIN payment_method ON orders.payment_method_id = payment_method.id "
        "WHERE orders.user_id=%s", (get_jwt_identity(),)) 
    return flask.jsonify(cursor.fetchall())

@orders.route("/<int:id>/price", methods=["GET"])
@jwt_required()
def get_order_price(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT shipping_method.price AS shipping_price, "
            "SUM(product_in_order.quantity*product.price) AS total_product_price FROM orders "
            "LEFT JOIN shipping_method ON orders.shipping_method_id = shipping_method.id "
            "LEFT JOIN product_in_order ON orders.id = product_in_order.order_id "
            "LEFT JOIN product ON product_in_order.product_id = product.id "
            "WHERE orders.id=%s "
            "GROUP BY orders.id", (id,))
    return flask.jsonify(cursor.fetchone())

@orders.route("/<int:id>/products", methods=["GET"])
def get_order_products(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product_in_order "
            "LEFT JOIN product ON product_in_order.product_id = product.id "
            "WHERE order_id=%s", (id, ))
    return flask.jsonify(cursor.fetchall())

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