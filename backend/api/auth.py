import flask
from flask import Blueprint
from flaskext.mysql import pymysql
from flask_jwt_extended import create_access_token
from db import mysql

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    db = mysql.get_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO user(username, password, first_name, last_name) "
                "VALUES(%(username)s, %(password)s, %(first_name)s, %(last_name)s)", flask.request.json)
        db.commit()
        return flask.jsonify(flask.request.json), 201
    except pymysql.err.IntegrityError:
        return "Username already exists", 409

@auth.route("/login", methods=["POST"])
def login():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM user WHERE username=%(username)s AND password=%(password)s", flask.request.json)
    user = cursor.fetchone()
    if not user:
        return "User doesn't exist", 401
    token = create_access_token(identity=user["username"])
    return flask.jsonify(token), 200   