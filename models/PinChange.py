from app import db
from models.UserAuthentication import User
from models.Card import CreditCard
from models.Account import Account

class PinChange():
    def __init__(self, userId):
        self.userId = userId

    def setPin(self,password2):

        dbCardNumber = Account.query.filter_by(userId=self.userId).first().cardNumber
        db.session.query(CreditCard).filter(CreditCard.cardNumber == dbCardNumber).update({CreditCard.pin: password2 })
        db.session.commit()
        #db.session.query(Creditcard).filter(Creditcard.cardNumber == dbCardNumber).update({​​​​​Card.block_request:0}​​​​​)

    def checkPin(self, pin):

        dbCardNumber = Account.query.filter_by(userId=self.userId).first().cardNumber
        dbPin = CreditCard.query.filter_by(cardNumber=dbCardNumber).first().pin

        if str(pin) == str(dbPin):
            return True
        else:
            return False