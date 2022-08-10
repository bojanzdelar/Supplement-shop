from config import ma
from models.payment_method import PaymentMethod

class PaymentMethodSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PaymentMethod