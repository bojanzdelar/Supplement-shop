from flask import Blueprint, request
from config import db
from utils.security_utils import admin_required
from schemas.payment_method_schema import PaymentMethodSchema
from models.payment_method import PaymentMethod

payment_method = Blueprint('payment_method', __name__)
schema = PaymentMethodSchema()

@payment_method.route("/", methods=["GET"])
def get_all_payment_methods():
    payment_methods = PaymentMethod.query.all()
    return schema.jsonify(payment_methods, many=True)

@payment_method.route("/<int:id>", methods=["GET"])
def get_payment_method(id):
    payment_method = PaymentMethod.query.filter_by(id=id).first()
    if not payment_method:
        return "Payment method not found!", 404

    return schema.jsonify(payment_method)
    
@payment_method.route("/", methods=["POST"])
@admin_required()
def create_payment_method():
    try:
        payment_method = PaymentMethod(**request.json)
        db.session.add(payment_method)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(payment_method), 201

@payment_method.route("/<int:id>", methods=["PATCH"])
@admin_required()
def update_payment_method(id):
    payment_method = PaymentMethod.query.filter_by(id=id).first()
    if not payment_method:
        return "Payment method not found!", 404
    
    new_payment_method = request.json
    try:
        PaymentMethod.query.filter_by(id = id).update(new_payment_method)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(payment_method)

@payment_method.route("/<int:id>", methods=["DELETE"])
@admin_required()
def delete_payment_method(id):
    payment_method = PaymentMethod.query.filter_by(id = id).first()
    if not payment_method:
        return "Payment method not found!", 404

    db.session.delete(payment_method)
    db.session.commit()
    return "", 204