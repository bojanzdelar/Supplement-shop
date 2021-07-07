import flask
from flask import Blueprint
from api.auth import admin_required
from app import mysql

user = Blueprint('user', __name__)

@user.route("/", methods=["GET"])
@admin_required()
def get_all_user():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM user")
    return flask.jsonify(cursor.fetchall())

@user.route("/<int:id>", methods=["GET"])
@admin_required()
def get_user(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM user WHERE id=%s", (id,))
    user = cursor.fetchone()
    return flask.jsonify(user) if user else ("", 404)

@user.route("/", methods=["POST"])
@admin_required()
def add_user():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO user(email, password, first_name, last_name, user_type_id) "
            "VALUES(%(email)s, %(password)s, %(first_name)s, %(last_name)s, %(user_type_id))", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@user.route("/<int:id>", methods=["PUT"])
@admin_required()
def update_user(id):
    user = flask.request.json
    user["id"] = id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE user SET email=%(email)s, password=%(password)s, first_name=%(first_name)s, last_name=%(last_name)s, user_type_id=%(user_type_id)s "
            "WHERE id=%(id)s", user)
    db.commit()
    cursor.execute("SELECT * FROM user WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@user.route("/<int:id>", methods=["DELETE"])
@admin_required()
def delete_user(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM user WHERE id=%s", (id,))
    db.commit()
    return ""