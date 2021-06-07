import flask
from flask import Blueprint
from app import mysql

category = Blueprint('category', __name__)

@category.route("/", methods=["GET"])
def get_all_category():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM category")
    return flask.jsonify(cursor.fetchall())

@category.route("/<int:id>", methods=["GET"])
def get_category(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM category WHERE id=%s", (id,))
    category = cursor.fetchone()
    return flask.jsonify(category) if category else ("", 404)

@category.route("/", methods=["POST"])
def create_category():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO category(name) "
            "VALUES(%(name)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@category.route("/<int:id>", methods=["PUT"])
def update_category(id):
    category = flask.request.json
    category["id"] = id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE category SET name=%(name)s "
            "WHERE id=%(id)s", category)
    db.commit()
    cursor.execute("SELECT * FROM category WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@category.route("/<int:id>", methods=["DELETE"])
def delete_category(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM category WHERE id=%s", (id,))
    db.commit()
    return ""