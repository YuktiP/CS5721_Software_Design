from app import db
from models.Card import CreditCard


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
        db.session.query(Creditcard).filter(CreditCard.cardNumber == cardNumber).update({CreditCard.cardStatus:0})
        db.session.commit()

    def setCardUnblockStatus(self, cardNumber):
        db.session.query(Creditcard).filter(CreditCard.cardNumber == cardNumber).update({CreditCard.cardStatus:1})
        db.session.query(Creditcard).filter(CreditCard.cardNumber == cardNumber).update({CreditCard.blockRequest:0})
        db.session.commit()

    def addCard(self,CreditCard):
        db.create_all()
        db.session.add(CreditCard)
        db.session.commit()

    def findCardInterest(self,cardNo):
        self.result=db.session.query(CreditCard.interest).filter(CreditCard.cardNumber==cardNo)
        return (self.result)
        
    def getCardById(self, cardId):
        return db.session.query(CreditCard).filter(CreditCard.cardId== cardId).first()

    def getCardByNumber(self, cardNumber):
        return db.session.query(CreditCard).filter(CreditCard.cardNumber== cardNumber).first()
    
    
    def blockCardRequest(self, cardId):
        cardInfo = db.session.query(CreditCard).filter(CreditCard.cardId == cardId).first()
        cardInfo.blockRequest = "1"
        db.session.commit()


    def unblockCardRequest(self, cardId):
        cardInfo = db.session.query(CreditCard).filter(CreditCard.cardId == cardId).first()
        cardInfo.blockRequest = "0"
        db.session.commit()
    





