from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from config import db
from utils.security_utils import admin_required, is_admin
from schemas.order_schema import OrderSchema
from models.order import Order
from models.product_in_order import ProductInOrder

order = Blueprint('order', __name__)
schema = OrderSchema()

@order.route("/", methods=["GET"])
@jwt_required()
def get_all_orders():
    if not is_admin():
        user_id = get_jwt_identity()
        orders = Order.query.filter_by(user_id=user_id).all()
        return schema.jsonify(orders, many=True)

    orders = Order.query.all()
    return schema.jsonify(orders, many=True)

@order.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_order(id):
    order = Order.query.filter_by(id=id).first()
    if not order:
        return "Order not found!", 404

    if order.user_id != get_jwt_identity() and not is_admin():
        return "You can't access this order!", 403

    return schema.jsonify(order)

@order.route("/", methods=["POST"])
@jwt_required(optional=True)
def create_order():
    order = request.json
    if not is_admin():
        order["user_id"] = get_jwt_identity()
    if not get_jwt_identity():
        del order["user_id"]

    try:
        products = order["products"]
        del order["products"]
    
        order = Order(**order)
        db.session.add(order)
        db.session.flush()

        for product in products:
            product["order_id"] = order.id
            product = ProductInOrder(**product)
            db.session.add(product)

        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(order), 201

@order.route("/<int:id>", methods=["PATCH"])
@admin_required()
def update_order(id):
    order = Order.query.filter_by(id=id).first()
    if not order:
        return "Order not found!", 404

    new_order = request.json
    new_order["id"] = id
    try:
        Order.query.filter_by(id=id).update(new_order)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(order)

@order.route("/<int:id>/sent", methods=["PATCH"])
@admin_required()
def send_order(id):
    order = Order.query.filter_by(id=id).first()
    if not order:
        return "Order not found!", 404

    order.sent = not order.sent
    db.session.commit()
    return schema.jsonify(order)

@order.route("/<int:id>/delivered", methods=["PATCH"])
@admin_required()
def deliver_order(id):
    order = Order.query.filter_by(id=id).first()
    if not order:
        return "Order not found!", 404

    order.delivered = not order.delivered
    db.session. commit()
    return schema.jsonify(order)

@order.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_order(id):
    order = Order.query.filter_by(id=id).first()
    if not order:
        return "Order not found!", 404

    if order.user_id != get_jwt_identity() and not is_admin():
        return "You can't modify this order!", 403

    order.deleted = True
    db.session.commit()
    return "", 204