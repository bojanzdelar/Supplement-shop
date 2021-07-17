import flask
from flask import Blueprint
from api.auth import admin_required
from db import mysql

product_in_order = Blueprint('product_in_order', __name__)

@product_in_order.route("/", methods=["GET"])
@admin_required()
def get_all_product_in_order():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product_in_order")
    return flask.jsonify(cursor.fetchall())

@product_in_order.route("/<string:product_id>/<int:order_id>", methods=["GET"])
def get_product_in_order(product_id, order_id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product_in_order ", 
            "WHERE product_id=%s AND order_id=%s", (product_id, order_id))
    product_in_order = cursor.fetchone()
    return flask.jsonify(product_in_order) if product_in_order else ("", 404)

@product_in_order.route("/", methods=["POST"])
def create_product_in_order():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO product_in_order(product_id, order_id, quantity) "
            "VALUES(%(product_id)s, %(order_id)s, %(quantity)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@product_in_order.route("/<string:product_id>/<int:order_id>", methods=["PUT"])
@admin_required()
def update_product_in_order(product_id, order_id):
    product_in_order = flask.request.json
    product_in_order["product_id"] = product_id
    product_in_order["order_id"] = order_id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE product_in_order SET quantity=%(quantity)s "
            "WHERE product_id=%(product_id)s AND order_id=%(order_id)s", product_in_order)
    db.commit()
    cursor.execute("SELECT * FROM product_in_order" 
            "WHERE product_id=%(product_id)s AND order_id=%(order_id)s", product_in_order)
    return flask.jsonify(cursor.fetchone()), 200

@product_in_order.route("/<string:product_id>/<int:order_id>", methods=["DELETE"])
@admin_required()
def delete_product_in_order(product_id, order_id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM product_in_order " 
            "WHERE product_id=%s AND order_id=%s", (product_id, order_id))
    db.commit()
    return ""