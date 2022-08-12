from config import ma
from models.user import User
from schemas.user_type_schema import UserTypeSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

    user_type = ma.Nested(UserTypeSchema)