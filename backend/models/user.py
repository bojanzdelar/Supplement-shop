from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    user_type = db.Column(db.Integer, db.ForeignKey("userType.id"), nullable=False)
    carts = db.relationship("Cart", backref="user")
    addresses = db.relationship("Address", backref="user")

    def __repr__(self):
        return f'<User: {self.email}>'