from config import db

class ShippingMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship("Order", backref="shipping_method")
  
    def __repr__(self):
        return f'<Shipping method: {self.name}>'