from app import db

class Card(db.Model):
    cardId = db.Column(db.Integer,primary_key=True)
    cardNumber=db.Column(db.Integer,primary_key=True)
    currentCredit_limit=db.Column(db.Integer)
    availableCredit_limit=db.Column(db.Integer)
    pin=db.Column(db.Integer)
    expiryDate=db.Column(db.String(255))
    cardSatus=db.Column(db.Integer)
    blockRequest=db.Column(db.Integer)
       

    def __init__(self, cardId, cardNumber, currentCreditLimit, availableCreditLimit,pin,expiryDate,cardStatus,blockRequest):
        self.cardId = cardId
        self.cardNumber = card_number
        self.currentCreditLimit = currentCreditLimit
        self.availableCreditLimit = availableCreditLimit
        self.pin=pin
        self.expiryDate=expiryDate
        self.cardStatus=cardStatus
        self.blockRequest=blockRequest
