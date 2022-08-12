from config import ma
from models.user_type import UserType

class UserTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserType
        include_fk = True