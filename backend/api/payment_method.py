import flask
from flask import Blueprint
from api.auth import admin_required
from db import mysql

payment_method = Blueprint('payment_method', __name__)

@payment_method.route("/", methods=["GET"])
def get_all_payment_method():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM payment_method")
    return flask.jsonify(cursor.fetchall())

@payment_method.route("/<int:id>", methods=["GET"])
def get_payment_method(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM payment_method WHERE id=%s", (id,))
    payment_method = cursor.fetchone()
    return flask.jsonify(payment_method) if payment_method else ("", 404)

@payment_method.route("/", methods=["POST"])
@admin_required()
def create_payment_method():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO payment_method(name) "
            "VALUES(%(name)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@payment_method.route("/<int:id>", methods=["PUT"])
@admin_required()
def update_payment_method(id):
    payment_method = flask.request.json
    payment_method["id"] = id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE payment_method SET name=%(name)s "
            "WHERE id=%(id)s", payment_method)
    db.commit()
    cursor.execute("SELECT * FROM payment_method WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@payment_method.route("/<int:id>", methods=["DELETE"])
@admin_required()
def delete_payment_method(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM payment_method WHERE id=%s", (id,))
    db.commit()
    return ""