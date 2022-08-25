from config import db
from models import *

try:
    db.drop_all()
    db.create_all()
    db.session.commit()
except Exception as e:
    print(e)