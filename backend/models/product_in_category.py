from config import db

class ProductInCategory(db.Model):
    product_id = db.Column(db.String(50), db.ForeignKey("product.id", onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    category_id = db.Column(db.String(50), db.ForeignKey("category.id", onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)

    def __repr__(self):
        return f'<Product in category: {self.product_id} - {self.category_id}>'