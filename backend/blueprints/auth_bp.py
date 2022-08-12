from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from config import db
from schemas.user_schema import UserSchema
from models.user import User

auth = Blueprint("auth", __name__)
schema = UserSchema()

@auth.route("/register", methods=["POST"])
def register():
    try:
        user = User(**request.json)
        email_exists = User.query.filter_by(email=user.email).first() is not None
        if email_exists:
            return "Email already exists", 400

        user.user_type_id = 2
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(user), 201

@auth.route("/login", methods=["POST"])
def login():
    credentials = request.json
    user = User.query.filter_by(email = credentials["email"], password = credentials["password"]).first()
    if not user:
        return "User doesn't exist", 401

    additional_claims = {
        "name": f"{user.first_name} {user.last_name}",
        "email": user.email,
        "admin": (user.user_type_id == 1)
    }
    access_token = create_access_token(identity=user.id, additional_claims=additional_claims)
    refresh_token = create_refresh_token(identity=user.id, additional_claims=additional_claims)
    return jsonify(access_token=access_token, refresh_token=refresh_token)

# We are using the `refresh=True` options in jwt_required to only allow
# refresh tokens to access this route.
@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    old_claims = get_jwt()
    additional_claims = {
        "name": old_claims["name"],
        "email": old_claims["email"],
        "admin": old_claims["admin"]
    }
    access_token = create_access_token(identity=identity, additional_claims=additional_claims)
    return jsonify(access_token=access_token)