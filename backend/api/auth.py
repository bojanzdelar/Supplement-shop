from functools import wraps
import flask
from flask import Blueprint
from flaskext.mysql import pymysql
from flask_jwt_extended import verify_jwt_in_request, get_jwt, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from db import mysql

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    db = mysql.get_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO user(email, password, first_name, last_name) "
                "VALUES(%(email)s, %(password)s, %(first_name)s, %(last_name)s)", flask.request.json)
        db.commit()
        return flask.jsonify(flask.request.json), 201
    except pymysql.err.IntegrityError:
        return "Username already exists", 409

@auth.route("/login", methods=["POST"])
def login():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM user WHERE email=%(email)s AND password=%(password)s", flask.request.json)
    user = cursor.fetchone()
    if not user:
        return "User doesn't exist", 401
    additional_claims = {
        "name": f"{user['first_name']} {user['last_name']}",
        "email": user["email"],
        "admin": user["user_type_id"] == 1
    }
    access_token = create_access_token(identity=user["id"], additional_claims=additional_claims)
    refresh_token = create_refresh_token(identity=user["id"], additional_claims=additional_claims)
    return flask.jsonify(access_token=access_token, refresh_token=refresh_token), 200   

# We are using the `refresh=True` options in jwt_required to only allow
# refresh tokens to access this route.
@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    old_claims = get_jwt()
    additional_claims = {
        "name": old_claims["name"],
        "email": old_claims["email"],
        "admin": old_claims["admin"]
    }
    access_token = create_access_token(identity=identity, additional_claims=additional_claims)
    return flask.jsonify(access_token=access_token)

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_administrator"]:
                return fn(*args, **kwargs)
            else:
                return flask.jsonify(msg="Admins only!"), 403

        return decorator

    return wrapper
