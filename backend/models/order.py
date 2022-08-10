from config import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    email = db.Column(db.String(255), nullable=False)
    shipping_address_id = db.Column(db.Integer, db.ForeignKey("address.id"), nullable=False)
    billing_address_id = db.Column(db.Integer, db.ForeignKey("address.id"), nullable=False)
    shipping_method_id = db.Column(db.Integer, db.ForeignKey("shipping_method.id"), nullable=False)
    payment_method_id = db.Column(db.Integer, db.ForeignKey("payment_method.id"), nullable=False)
    sent = db.Column(db.Boolean, nullable=False)
    delivered = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Order: {self.id}>'