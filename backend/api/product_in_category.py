import flask
from flask import Blueprint
from api.auth import admin_required
from db import mysql

product_in_category = Blueprint('product_in_category', __name__)

@product_in_category.route("/", methods=["GET"])
def get_all_product_in_category():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product_in_category")
    return flask.jsonify(cursor.fetchall())

@product_in_category.route("/<string:product_id>/<string:category_id>", methods=["GET"])
def get_product_in_category(product_id, category_id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product_in_category "
            "WHERE product_id=%s AND category_id=%s", (product_id, category_id))
    product_in_category = cursor.fetchone()
    return flask.jsonify(product_in_category) if product_in_category else ("", 404)

@product_in_category.route("/", methods=["POST"])
@admin_required()
def create_product_in_category():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO product_in_category(product_id, category_id) "
            "VALUES(%(product_id)s, %(category_id)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

# @product_in_category.route("/<string:product_id>/<string:category_id>", methods=["PUT"])
# @admin_required()
# def update_product_in_category(product_id, category_id):
#     product_in_category = flask.request.json
#     product_in_category["product_id"] = product_id
#     product_in_category["category_id"] = category_id
#     db = mysql.get_db()
#     cursor = db.cursor()
#     cursor.execute("UPDATE product_in_category SET "
#             "WHERE product_id=%(product_id)s AND order_id=%(order_id)s", product_in_category)
#     db.commit()
#     cursor.execute("SELECT * FROM product_in_category" 
#             "WHERE product_id=%(product_id)s AND category_id=%(category_id)s", product_in_category)
#     return flask.jsonify(cursor.fetchone()), 200

@product_in_category.route("/<string:product_id>/<string:category_id>", methods=["DELETE"])
@admin_required()
def delete_product_in_category(product_id, category_id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM product_in_category " 
        "WHERE product_id=%(product_id)s AND category_id=%(category_id)s", (product_id, category_id))
    db.commit()
    return ""

@product_in_category.route("/<string:product_id>", methods=["DELETE"])
@admin_required()
def delete_product_categories(product_id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM product_in_category WHERE product_id=%s", (product_id,))
    db.commit()
    return ""