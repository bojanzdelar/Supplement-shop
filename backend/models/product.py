from config import db

class Product(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    thumbnail = db.Column(db.Text)
    image = db.Column(db.Text)
    views = db.Column(db.Integer, nullable=False, default=0)
    deleted = db.Column(db.Boolean, default=False)
    categories = db.relationship('ProductInCategory', backref="product_category")
    carts = db.relationship("Cart", backref="product_cart")

    def __repr__(self):
        return f'<Product: {self.name}>'