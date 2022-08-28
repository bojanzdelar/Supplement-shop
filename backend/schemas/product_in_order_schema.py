from config import ma
from models.product_in_order import ProductInOrder
from schemas.product_schema import ProductSchema

class ProductInOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductInOrder
    
    product_order = ma.Nested(ProductSchema)