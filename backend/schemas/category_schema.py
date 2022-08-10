from config import ma
from models.category import Category

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category