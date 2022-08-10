from config import ma
from models.product_in_category import ProductInCategory

class ProductInCategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductInCategory