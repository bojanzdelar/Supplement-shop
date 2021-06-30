import flask
from flask import Blueprint
from app import mysql

shipping_method = Blueprint('shipping_method', __name__)

@shipping_method.route("/", methods=["GET"])
def get_all_shipping_method():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM shipping_method")
    return flask.jsonify(cursor.fetchall())

@shipping_method.route("/<int:id>", methods=["GET"])
def get_shipping_method(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM shipping_method WHERE id=%s", (id,))
    shipping_method = cursor.fetchone()
    return flask.jsonify(shipping_method) if shipping_method else ("", 404)

@shipping_method.route("/", methods=["POST"])
def create_shipping_method():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO shipping_method(name, price) "
            "VALUES(%(name)s, %(price)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@shipping_method.route("/<int:id>", methods=["PUT"])
def update_shipping_method(id):
    shipping_method = flask.request.json
    shipping_method["id"] = id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE shipping_method SET name=%(name)s, price=%(price)s "
            "WHERE id=%(id)s", shipping_method)
    db.commit()
    cursor.execute("SELECT * FROM shipping_method WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@shipping_method.route("/<int:id>", methods=["DELETE"])
def delete_shipping_method(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM shipping_method WHERE id=%s", (id,))
    db.commit()
    return ""