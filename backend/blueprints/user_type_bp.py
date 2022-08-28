from flask import Blueprint, request
from config import db
from utils.security_utils import admin_required
from schemas.user_type_schema import UserTypeSchema
from models.user_type import UserType

user_type = Blueprint('user_type', __name__)
schema = UserTypeSchema()

@user_type.route("/", methods=["GET"])
def get_all_user_types():
    user_types = UserType.query.all()
    return schema.jsonify(user_types, many=True)

@user_type.route("/<int:id>", methods=["GET"])
def get_user_type(id):
    user_type = UserType.query.filter_by(id=id).first()
    if not user_type:
        return "User type not found!", 404

    return schema.jsonify(user_type)
    
@user_type.route("/", methods=["POST"])
@admin_required()
def create_user_type():
    try:
        user_type = UserType(**request.json)
        db.session.add(user_type)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(user_type), 201

@user_type.route("/<int:id>", methods=["PATCH"])
@admin_required()
def update_user_type(id):
    user_type = UserType.query.filter_by(id=id).first()
    if not user_type:
        return "User type not found!", 404
    
    new_user_type = request.json
    new_user_type["id"] = id
    try:
        UserType.query.filter_by(id = id).update(new_user_type)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(user_type)

@user_type.route("/<int:id>", methods=["DELETE"])
@admin_required()
def delete_user_type(id):
    user_type = UserType.query.filter_by(id = id).first()
    if not user_type:
        return "User type not found!", 404

    db.session.delete(user_type)
    db.session.commit()
    return "", 204