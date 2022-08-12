from config import ma
from models.address import Address
from schemas.user_schema import UserSchema

class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
    
    user_address = ma.Nested(UserSchema)