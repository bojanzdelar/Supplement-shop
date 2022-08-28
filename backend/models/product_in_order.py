from config import db

class ProductInOrder(db.Model):
    product_id = db.Column(db.String(50), db.ForeignKey("product.id", onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id", onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product in order: {self.product_id} - {self.order_id}>'