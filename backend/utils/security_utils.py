from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from models.user import User

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["admin"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admins only!"), 403

        return decorator

    return wrapper

def is_admin():
    jwt = get_jwt()
    return jwt["admin"] if jwt else False

def get_claims(user: User):
    if not user or not isinstance(user, User):
        return None

    return {
        "name": f"{user.first_name} {user.last_name}",
        "email": user.email,
        "admin": (user.user_type_id == 1)
    }