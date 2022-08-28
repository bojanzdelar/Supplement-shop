from config import db

class Cart(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    product_id = db.Column(db.String(50), db.ForeignKey("product.id", onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Cart: {self.user_id} - {self.category_id}>'