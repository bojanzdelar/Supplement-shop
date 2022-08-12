from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from config import db
from utils.security_utils import admin_required, is_admin
from schemas.product_in_order_schema import ProductInOrderSchema
from models.product_in_order import ProductInOrder
from models.product import Product

product_in_order = Blueprint('product_in_order', __name__)
schema = ProductInOrderSchema()

@product_in_order.route("/", methods=["GET"])
@admin_required()
def get_all_products_in_order():
    products_in_order = ProductInOrder.query.all()
    return schema.jsonify(products_in_order, many=True)

@product_in_order.route("/<string:product_id>/<int:order_id>", methods=["GET"])
@jwt_required()
def get_product_in_order(product_id, order_id):
    product_in_order = ProductInOrder.query.filter_by(product_id=product_id, order_id=order_id).first()
    if not product_in_order:
        return "Product in order not found!", 404

    user_id = product_in_order.order.user_order.id
    if user_id != get_jwt_identity() and not is_admin():
        return "You can't access this product in order!", 403

    return schema.jsonify(product_in_order)

@product_in_order.route("/", methods=["POST"])
@admin_required()
def create_product_in_order():
    try:
        product_in_order = ProductInOrder(request.json)
        product = Product.query.filter_by(id=product_in_order.product_id).first()
        if not product or product.deleted:
            return "You can't add this product to order!", 400
        
        db.session.add(product_in_order)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(product_in_order), 201

@product_in_order.route("/<string:product_id>/<int:order_id>", methods=["PATCH"])
@admin_required()
def update_product_in_order(product_id, order_id):
    product_in_order = ProductInOrder.query.filter_by(product_id=product_id, order_id=order_id).first()
    if not product_in_order:
        return "Product in order not found!", 404

    product = Product.query.filter_by(id=product_in_order.product_id).first()
    if not product or product.deleted:
        return "You can't add this product to order!", 400
    
    new_product_in_order = request.json
    try:
        ProductInOrder.query.filter_by(product_id=product_id, order_id=order_id).update(new_product_in_order)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(product_in_order)

@product_in_order.route("/<string:product_id>/<int:order_id>", methods=["DELETE"])
@admin_required()
def delete_product_in_order(product_id, order_id):
    product_in_order = ProductInOrder.query.filter_by(product_id=product_id, order_id=order_id).first()
    if not product_in_order:
        return "Product in order not found!", 404
    
    db.session.delete(product_in_order)
    db.session.commit()
    return "", 204