from models.card import CreditCard
from app import db
class CardDBController():
    def __init__(self):
        self = self

    def addCard(self,Creditcard):
        db.create_all()
        db.session.add(Creditcard)
        db.session.commit()

