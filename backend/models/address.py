from config import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    company = db.Column(db.Text)
    address = db.Column(db.Text, nullable=False)
    apartment = db.Column(db.Text)
    city = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)
    state = db.Column(db.Text, nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(45))
    deleted = db.Column(db.Boolean, default=False)
    shipping_orders = db.relationship("Order", backref="shipping_address", foreign_keys="Order.shipping_address_id")
    billing_orders = db.relationship("Order", backref="billing_address", foreign_keys="Order.billing_address_id")
    
    def __repr__(self):
        return f'<Address: {self.address}>'