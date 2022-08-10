from config import db

class Category(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.Text, nullable=False)
    products = db.relationship('ProductInCategory', backref="category")
  
    def __repr__(self):
        return f'<Category: {self.name}>'