from app import db
from models.UserAuthentication import User
from models.card import Creditcard
from models.account import Account

class PinChange():
    def __init__(self, userId):
        self.userId = userId

    def setPin(self,password2):

        dbCardNumber = Account.query.filter_by(userId=self.userId).first().cardNumber
        db.session.query(Creditcard).filter(Creditcard.cardNumber == dbCardNumber).update({Creditcard.pin: password2 })
        db.session.commit()
        #db.session.query(Creditcard).filter(Creditcard.cardNumber == dbCardNumber).update({​​​​​Card.block_request:0}​​​​​)

    def checkPin(self, pin):

        dbCardNumber = Account.query.filter_by(userId=self.userId).first().cardNumber
        dbPin = Creditcard.query.filter_by(cardNumber=dbCardNumber).first().pin

        if str(pin) == str(dbPin):
            return True
        else:
            return False