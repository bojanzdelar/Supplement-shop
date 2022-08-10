from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey("user_type.id"), nullable=False)
    carts = db.relationship("Cart", backref="user_cart")
    addresses = db.relationship("Address", backref="user_address")

    def __repr__(self):
        return f'<User: {self.email}>'