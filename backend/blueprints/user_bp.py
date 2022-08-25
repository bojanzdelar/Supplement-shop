from werkzeug.security import generate_password_hash
from flask import Blueprint, request
from config import db
from utils.security_utils import admin_required
from schemas.user_schema import UserSchema
from models.user import User

user = Blueprint('user', __name__)
schema = UserSchema()

@user.route("/", methods=["GET"])
@admin_required()
def get_all_users():
    users = User.query.all()
    return schema.jsonify(users, many=True)

@user.route("/<int:id>", methods=["GET"])
@admin_required()
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return "User not found!", 404

    return schema.jsonify(user)
    
@user.route("/", methods=["POST"])
@admin_required()
def create_user():
    try:
        user = User(**request.json)
        user.password = generate_password_hash(user.password, "sha256")
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(user), 201

@user.route("/<int:id>", methods=["PATCH"])
@admin_required()
def update_user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return "User not found!", 404
    
    new_user = request.json
    if "password" in new_user:
        new_user["password"] = generate_password_hash(new_user["password"], "sha256")
    try:
        User.query.filter_by(id = id).update(new_user)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(user)

@user.route("/<int:id>", methods=["DELETE"])
@admin_required()
def delete_user(id):
    user = User.query.filter_by(id = id).first()
    if not user:
        return "User not found!", 404

    db.session.delete(user)
    db.session.commit()
    return "", 204