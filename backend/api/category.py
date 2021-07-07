import flask
from flask import Blueprint
from api.auth import admin_required   
from app import mysql

category = Blueprint('category', __name__)

@category.route("/", methods=["GET"])
def get_all_category():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM category")
    return flask.jsonify(cursor.fetchall())

@category.route("/<string:id>", methods=["GET"])
def get_category(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM category WHERE id=%s", (id,))
    category = cursor.fetchone()
    return flask.jsonify(category) if category else ("", 404)

@category.route("/<string:id>/products", methods=["GET"])
def get_category_products(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT product.* FROM product INNER JOiN product_in_category "
            "ON product.id = product_in_category.product_id "
            "WHERE product_in_category.category_id=%s", (id,))
    products = cursor.fetchall()
    return flask.jsonify(products) if products else ""

@category.route("/", methods=["POST"])
@admin_required()
def create_category():
    category = flask.request.json
    category["id"] = category["name"].replace(" ", "-").lower()
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO category(id, name) "
            "VALUES(%(id)s, %(name)s)", category)
    db.commit()
    return flask.jsonify(category), 201

@category.route("/<string:id>", methods=["PUT"])
@admin_required()
def update_category(id):
    category = flask.request.json
    category["old_id"] = id
    category["id"] = category["name"].replace(" ", "-").lower()
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE category SET id=%(id)s, name=%(name)s "
            "WHERE id=%(old_id)s", category)
    db.commit()
    cursor.execute("SELECT * FROM category WHERE id=%s", (category["id"],))
    return flask.jsonify(cursor.fetchone()), 200

@category.route("/<string:id>", methods=["DELETE"])
@admin_required()
def delete_category(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM category WHERE id=%s", (id,))
    db.commit()
    return ""