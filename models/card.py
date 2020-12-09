from app import db
class Creditcard(db.Model):
    cardId=db.Column(db.BigInteger,primary_key=True)
    cardNumber=db.Column(db.BigInteger)
    pin=db.Column(db.Integer)
    cardCode=db.Column(db.Integer)
    expiryDate=db.Column(db.Date)
    status=db.Column(db.Integer)
    cardType=db.Column(db.String(20))
    
    def __init__(self,cardNumber,pin,cardCode,expiryDate,status,cardType):
        self.cardNumber=cardNumber
        self.pin=pin
        self.cardCode=cardCode
        self.expiryDate=expiryDate
        self.status=status
        self.cardType=cardType


    def addCard(self):
            db.create_all()
            db.session.add(self)
            db.session.commit()    