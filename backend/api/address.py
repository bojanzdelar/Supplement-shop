import flask
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity   
from app import mysql

address = Blueprint('address', __name__)

@address.route("/", methods=["GET"])
def get_all_address():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM address")
    return flask.jsonify(cursor.fetchall())

@address.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_address(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM address WHERE id=%s", (id,))
    address = cursor.fetchone()
    return flask.jsonify(address) if address else ("", 404)

@address.route("/", methods=["POST"])
@jwt_required(optional=True)
def create_address():
    address = flask.request.json
    address["user_id"] = get_jwt_identity()
    address.setdefault("company", None)
    address.setdefault("apartment", None)
    address.setdefault("phone", None)
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO address(user_id, first_name, last_name, company, address, apartment, city, country, state, ZIP_code, phone) "
            "VALUES(%(user_id)s, %(first_name)s, %(last_name)s, %(company)s, %(address)s, %(apartment)s, %(city)s, %(country)s, %(state)s, %(ZIP_code)s, %(phone)s)", address)
    db.commit()
    cursor.execute("SELECT last_insert_id() AS id")
    return flask.jsonify(cursor.fetchone()), 201

@address.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_address(id):
    address = flask.request.json
    address["id"] = id
    address.setdefault("company", None)
    address.setdefault("apartment", None)
    address.setdefault("phone", None)
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE address SET user_id=%(user_id)s, first_name=%(first_name)s, last_name=%(last_name)s, company=%(company)s, "
            "address=%(address)s, apartment=%(apartment)s, city=%(city)s, country=%(country)s, state=%(state)s, ZIP_code=%(ZIP_code)s, phone=%(phone)s "
            "WHERE id=%(id)s", address)
    db.commit()
    cursor.execute("SELECT * FROM address WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@address.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_address(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM address WHERE id=%s", (id,))
    db.commit()
    return ""