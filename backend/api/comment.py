import flask
from flask import Blueprint
from app import mysql

comment = Blueprint('comment', __name__)

@comment.route("/", methods=["GET"])
def get_all_comment():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM comment")
    return flask.jsonify(cursor.fetchall())

@comment.route("/<int:id>", methods=["GET"])
def get_comment(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM comment WHERE id=%s", (id,))
    comment = cursor.fetchone()
    return flask.jsonify(comment) if comment else ("", 404)

@comment.route("/", methods=["POST"])
def create_comment():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO comment(user_id, product_id, title, content, created) "
            "VALUES(%(user_id)s, %(product_id)s, %(title)s, %(content)s, %(created)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@comment.route("/<int:id>", methods=["PUT"])
def update_comment(id):
    comment = flask.request.json
    comment["id"] = id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE comment SET user_id=%(user_id)s, product_id=%(product_id)s, title=%(title)s, content=%(content)s, created=%(created)s "
            "WHERE id=%(id)s", comment)
    db.commit()
    cursor.execute("SELECT * FROM comment WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@comment.route("/<int:id>", methods=["DELETE"])
def delete_comment(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM comment WHERE id=%s", (id,))
    db.commit()
    return ""