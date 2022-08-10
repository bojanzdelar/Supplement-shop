from config import ma
from models.order import Order

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order