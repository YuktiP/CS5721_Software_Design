from app import db
from models.Card import Card

class CardDBController():

    def __init__(self):
        self = self

    def getBlockRequests(self):
        self.blockCardList = db.session.query(Card.card_number).filter(Card.block_request == 1 , Card.card_status != 0).all()
        return self.blockCardList
    
    def getUnblockRequests(self):
        self.unblockCardList = db.session.query(Card.card_number).filter(Card.card_status == 0).all()
        return self.unblockCardList

    def setCardBlockStatus(self, cardNumber):
        db.session.query(Card).filter(Card.card_number == cardNumber).update({Card.card_status:0})
        db.session.commit()

    def setCardUnblockStatus(self, cardNumber):
        db.session.query(Card).filter(Card.card_number == cardNumber).update({Card.card_status:1})
        db.session.query(Card).filter(Card.card_number == cardNumber).update({Card.block_request:0})
        db.session.commit()