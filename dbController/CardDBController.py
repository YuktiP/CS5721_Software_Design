from app import db
from models.Card import Card


class CardDBController():
    def __init__(self):
        self = self
    
    def getBlockRequests(self):
        self.blockCardList = db.session.query(Card.cardNumber).filter(Card.blockRequest == 1 , Card.cardStatus != 0).all()
        return self.blockCardList
    
    def getUnblockRequests(self):
        self.unblockCardList = db.session.query(Card.cardNumber).filter(Card.cardStatus == 0).all()
        return self.unblockCardList

    def setCardBlockStatus(self, cardNumber):
        db.session.query(Card).filter(Card.cardNumber == cardNumber).update({Card.cardStatus:0})
        db.session.commit()

    def setCardUnblockStatus(self, cardNumber):
        db.session.query(Card).filter(Card.cardNumber == cardNumber).update({Card.cardStatus:1})
        db.session.query(Card).filter(Card.cardNumber == cardNumber).update({Card.blockRequest:0})
        db.session.commit()

    def addCard(self,Creditcard):
        db.create_all()
        db.session.add(Card)
        db.session.commit()

