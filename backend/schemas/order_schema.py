from config import ma
from models.order import Order
from schemas.user_schema import UserSchema
from schemas.address_schema import AddressSchema
from schemas.shipping_method_schema import ShippingMethodSchema
from schemas.payment_method_schema import PaymentMethodSchema

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
    
    user_order = ma.Nested(UserSchema)
    shipping_address = ma.Nested(AddressSchema)
    billing_address = ma.Nested(AddressSchema)
    shipping_method = ma.Nested(ShippingMethodSchema)
    payment_method = ma.Nested(PaymentMethodSchema)
    total_product_price = ma.Method("get_total_product_price")

    def get_total_product_price(self, order):
        products = order.products
        prices = [product.product_order.price * product.quantity for product in products]
        return round(sum(prices), 2)