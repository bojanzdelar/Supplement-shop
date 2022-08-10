from config import ma
from models.shipping_method import ShippingMethod

class ShippingMethodSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ShippingMethod