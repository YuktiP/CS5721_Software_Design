from app import db


class Card(db.Model):
    cardId=db.Column(db.BigInteger,primary_key=True)
    cardNumber=db.Column(db.BigInteger)
    currentCreditLimit=db.Column(db.Integer)
    availableCreditLimit=db.Column(db.Integer)
    pin=db.Column(db.Integer)
    #cardCode=db.Column(db.Integer)
    expiryDate=db.Column(db.Date)
    cardStatus=db.Column(db.Integer)
    cardType=db.Column(db.String(20))
    blockRequest=db.Column(db.Integer)
    
    def __init__(self,cardId,cardNumber,currentCreditLimit,availableCreditLimit,pin,expiryDate,cardStatus,blockRequest,cardType):
        self.cardId = cardId
        self.cardNumber = cardNumber
        self.currentCreditLimit = currentCreditLimit
        self.availableCreditLimit = availableCreditLimit
        self.pin = pin
        self.expiryDate = expiryDate
        self.cardStatus = card_status
        self.blockRequest = block_request
        self.cardType = cardType

    def addCard(self):
            db.create_all()
            db.session.add(self)
            db.session.commit()   