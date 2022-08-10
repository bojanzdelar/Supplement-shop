from config import ma
from models.address import Address

class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address