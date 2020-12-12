from app import db

from models.card import Creditcard

class CardDBController():
    def __init__(self):
        self = self
    
    def getBlockRequests(self):
        self.blockCardList = db.session.query(Creditcard.cardNumber).filter(Creditcard.blockRequest == 1 , Creditcard.cardStatus != 0).all()
        return self.blockCardList
    
    def getUnblockRequests(self):
        self.unblockCardList = db.session.query(Creditcard.cardNumber).filter(Creditcard.cardStatus == 0).all()
        return self.unblockCardList

    def setCardBlockStatus(self, cardNumber):
        db.session.query(Creditcard).filter(Creditcard.cardNumber == cardNumber).update({Creditcard.cardStatus:0})
        db.session.commit()

    def setCardUnblockStatus(self, cardNumber):
        db.session.query(Creditcard).filter(Creditcard.cardNumber == cardNumber).update({Creditcard.cardStatus:1})
        db.session.query(Creditcard).filter(Creditcard.cardNumber == cardNumber).update({Creditcard.blockRequest:0})
        db.session.commit()

    def addCard(self,CreditCard):
        db.create_all()
        db.session.add(CreditCard)
        db.session.commit()

    def getCardById(self, cardId):
        return db.session.query(Creditcard).filter(Creditcard.cardId== cardId).first()

    def getCardByNumber(self, cardNumber):
        return db.session.query(Creditcard).filter(Creditcard.cardNumber== cardNumber).first()
    
    
    def blockCardRequest(self, cardId):
        cardInfo = db.session.query(Creditcard).filter(Creditcard.cardId == cardId).first()
        cardInfo.blockRequest = "1"
        db.session.commit()


    def unblockCardRequest(self, cardId):
        cardInfo = db.session.query(Creditcard).filter(Creditcard.cardId == cardId).first()
        cardInfo.blockRequest = "0"
        db.session.commit()
    





