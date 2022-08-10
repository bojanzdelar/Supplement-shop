from config import ma
from models.product_in_order import ProductInOrder

class ProductInOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductInOrder