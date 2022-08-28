from flask import Blueprint, request
from config import db
from utils.security_utils import admin_required
from schemas.shipping_method_schema import ShippingMethodSchema
from models.shipping_method import ShippingMethod

shipping_method = Blueprint('shipping_method', __name__)
schema = ShippingMethodSchema()

@shipping_method.route("/", methods=["GET"])
def get_all_shipping_methods():
    shipping_methods = ShippingMethod.query.all()
    return schema.jsonify(shipping_methods, many=True)

@shipping_method.route("/<int:id>", methods=["GET"])
def get_shipping_method(id):
    shipping_method = ShippingMethod.query.filter_by(id=id).first()
    if not shipping_method:
        return "Shipping method not found!", 404

    return schema.jsonify(shipping_method)
    
@shipping_method.route("/", methods=["POST"])
@admin_required()
def create_shipping_method():
    try:
        shipping_method = ShippingMethod(**request.json)
        db.session.add(shipping_method)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(shipping_method), 201

@shipping_method.route("/<int:id>", methods=["PATCH"])
@admin_required()
def update_shipping_method(id):
    shipping_method = ShippingMethod.query.filter_by(id=id).first()
    if not shipping_method:
        return "Shipping method not found!", 404
    
    new_shipping_method = request.json
    new_shipping_method["id"] = id
    try:
        ShippingMethod.query.filter_by(id = id).update(new_shipping_method)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(shipping_method)

@shipping_method.route("/<int:id>", methods=["DELETE"])
@admin_required()
def delete_shipping_method(id):
    shipping_method = ShippingMethod.query.filter_by(id = id).first()
    if not shipping_method:
        return "Shipping method not found!", 404

    db.session.delete(shipping_method)
    db.session.commit()
    return "", 204