from config import db

class PaymentMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    orders = db.relationship("Order", backref="payment_method")
  
    def __repr__(self):
        return f'<Payment method: {self.name}>'