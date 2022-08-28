from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity   
from config import db
from utils.security_utils import is_admin
from schemas.address_schema import AddressSchema
from models.address import Address

address = Blueprint('address', __name__)
schema = AddressSchema()

@address.route("/", methods=["GET"])
@jwt_required()
def get_all_addresses():
    if not is_admin():
        user_id = get_jwt_identity()
        addresses = Address.query.filter_by(user_id=user_id).all()
        return schema.jsonify(addresses, many=True)
    
    addresses = Address.query.all()
    return schema.jsonify(addresses, many=True)

@address.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_address(id):
    address = Address.query.filter_by(id=id).first()
    if not address:
        return "Address not found!", 404

    if address.user_id != get_jwt_identity() and not is_admin():
        return "You can't access this address!", 403

    return schema.jsonify(address)

@address.route("/", methods=["POST"])
@jwt_required(optional=True)
def create_address():
    address = request.json
    if not is_admin():
        address["user_id"] = get_jwt_identity()
    if not get_jwt_identity():
        del address["user_id"]

    try:
        address = Address(**address)
        db.session.add(address)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(address), 201

@address.route("/<int:id>", methods=["PATCH"])
@jwt_required()
def update_address(id):
    address = Address.query.filter_by(id = id).first()
    if not address:
        return "Address not found!", 404

    if address.user_id != get_jwt_identity() and not is_admin():
        return "You can't modify this address!", 403

    new_address = request.json
    new_address["id"] = id
    if not is_admin():
        new_address["user_id"] = get_jwt_identity()

    try:
        Address.query.filter_by(id = id).update(new_address)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(address)

@address.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_address(id):
    address = Address.query.filter_by(id = id).first()
    if not address:
        return "Address not found!", 404

    if address.user_id != get_jwt_identity() and not is_admin():
        return "You can't modify this address!", 403

    address.deleted = True
    db.session.commit()
    return "", 204