from config import db

class UserType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    users = db.relationship("UserType", backref="user")
  
    def __repr__(self):
        return f'<User type: {self.name}>'