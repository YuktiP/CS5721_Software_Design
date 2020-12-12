from app import db
from models.card import CreditCard


class CardDBController():
    def __init__(self):
        self = self
    
    def getBlockRequests(self):
        self.blockCardList = db.session.query(CreditCard.cardNumber).filter(CreditCard.blockRequest == 1 , CreditCard.cardStatus != 0).all()
        return self.blockCardList
    
    def getUnblockRequests(self):
        self.unblockCardList = db.session.query(CreditCard.cardNumber).filter(CreditCard.cardStatus == 0).all()
        return self.unblockCardList

    def setCardBlockStatus(self, cardNumber):
        db.session.query(CreditCard).filter(CreditCard.cardNumber == cardNumber).update({CreditCard.cardStatus:0})
        db.session.commit()

    def setCardUnblockStatus(self, cardNumber):
        db.session.query(CreditCard).filter(CreditCard.cardNumber == cardNumber).update({CreditCard.cardStatus:1})
        db.session.query(CreditCard).filter(CreditCard.cardNumber == cardNumber).update({Card.blockRequest:0})
        db.session.commit()

    def addCard(self,CreditCard):
        db.create_all()
        db.session.add(CreditCard)
        db.session.commit()

