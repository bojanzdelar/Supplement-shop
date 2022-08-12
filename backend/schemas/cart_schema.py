from config import ma
from models.cart import Cart
from schemas.user_schema import UserSchema
from schemas.product_schema import ProductSchema

class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cart
    
    user_cart = ma.Nested(UserSchema)
    product_cart = ma.Nested(ProductSchema)