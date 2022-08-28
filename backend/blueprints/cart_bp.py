from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity   
from config import db
from utils.security_utils import is_admin
from schemas.cart_schema import CartSchema
from models.cart import Cart
from models.product import Product
from models.user import User

cart = Blueprint('cart', __name__)
schema = CartSchema()

@cart.route("/", methods=["GET"])
@jwt_required()
def get_all_carts():
    if not is_admin():
        user_id = get_jwt_identity()
        carts = Cart.query.filter_by(user_id=user_id).all()
        return schema.jsonify(carts, many=True)

    carts = Cart.query.all()
    return schema.jsonify(carts, many=True)

@cart.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user_cart(user_id):
    if user_id != get_jwt_identity() and not is_admin():
        return "You can't access this cart!", 403

    user = User.query.filter_by(id=user_id).first()
    if not user:
        return "User not found!", 404

    carts = Cart.query.filter_by(user_id=user_id).all()
    return schema.jsonify(carts, many=True)

@cart.route("/<int:user_id>/<string:product_id>", methods=["GET"])
@jwt_required()
def get_cart(user_id, product_id):
    if user_id != get_jwt_identity() and not is_admin():
        return "You can't modify this cart!", 403

    cart = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
    if not cart:
        return "Cart not found!", 404

    return schema.jsonify(cart)

@cart.route("/", methods=["POST"])
@jwt_required()
def create_cart():
    try:
        cart = Cart(**request.json)
        if cart.user_id != get_jwt_identity() and not is_admin():
            return "You can't create this cart!", 403

        product = Product.query.filter_by(id=cart.product_id).first()
        if not product or product.deleted:
            return "You can't add this product to cart!", 400

        existing_cart = Cart.query.filter_by(user_id=cart.user_id, product_id=cart.product_id).first()
        if existing_cart:
            existing_cart.quantity += cart.quantity
        else:
            db.session.add(cart)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    created_cart = Cart.query.filter_by(user_id=cart.user_id, product_id=cart.product_id).first()
    return schema.jsonify(created_cart), 201

@cart.route("/<int:user_id>/<string:product_id>", methods=["PATCH"])
@jwt_required()
def update_cart(user_id, product_id):
    if user_id != get_jwt_identity() and not is_admin():
        return "You can't modify this cart!", 403

    cart = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
    if not cart:
        return "Cart not found!", 404

    product = Product.query.filter_by(id=cart.product_id).first()
    if not product or product.deleted:
        return "You can't add this product to cart!", 400

    new_cart = request.json
    new_cart["product_id"] = product_id 
    if not is_admin():
        new_cart["user_id"] = user_id
    try:
        cart = Cart.query.filter_by(user_id=user_id, product_id=product_id).update(new_cart)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 404
    return schema.jsonify(cart)

@cart.route("/<int:user_id>/<string:product_id>", methods=["DELETE"])
@jwt_required()
def delete_cart(user_id, product_id):
    if user_id != get_jwt_identity() and not is_admin():
        return "You can't modify this cart!", 403

    cart = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
    if not cart:
        return "Cart not found!", 404

    db.session.delete(cart)
    db.session.commit()
    return "", 204

@cart.route("/", methods=["DELETE"])
@jwt_required()
def delete_user_cart():
    if is_admin():
        return "You don't have a cart because you are admin!", 400

    user_id = get_jwt_identity()
    Cart.query.filter_by(user_id=user_id).delete()
    db.session.commit()
    return "", 204