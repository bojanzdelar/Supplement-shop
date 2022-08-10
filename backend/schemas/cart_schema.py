from config import ma
from models.cart import Cart

class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cart