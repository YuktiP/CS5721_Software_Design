from app import db

class CreditCard(db.Model):
    cardId=db.Column(db.BigInteger,primary_key=True)
    cardNumber=db.Column(db.BigInteger)
    currentCreditLimit=db.Column(db.Integer)
    availableCreditLimit=db.Column(db.Integer)
    pin=db.Column(db.Integer)
    cardCode=db.Column(db.Integer)
    expiryDate=db.Column(db.Date)
    cardStatus=db.Column(db.Integer)
    cardType=db.Column(db.String(20))
    creditLimit=db.Column(db.Integer)
    interest=db.Column(db.Integer)
    blockRequest=db.Column(db.Integer)
    
    def __init__(self,cardNumber=None,pin=None,cardCode=None,expiryDate=None,status=None,cardType=None,creditLimit=None,interest=None,blockRequest=None):
        self.cardNumber=cardNumber
        self.pin=pin
        self.cardCode=cardCode
        self.expiryDate=expiryDate
        self.status=status
        self.cardType=cardType
        self.creditLimit = creditLimit
        self.interest = interest
        self.blockRequest = blockRequest   