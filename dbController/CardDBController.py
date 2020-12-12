from models.card import Creditcard
from app import db
class cardDBController():
    def __init__(self):
        self = self

    def addCard(self,Creditcard):
        db.create_all()
        db.session.add(Creditcard)
        db.session.commit()

