from app import db
class Transaction(db.Model):
    transactionId=db.Column(db.Integer,primary_key=True)
    cardNumber=db.Column(db.String(30))
    transactionType=db.Column(db.String(30))
    transactionSource=db.Column(db.String(30))
    timestamp=db.Column(db.DateTime)
    amount=db.Column(db.Integer)
    isSettled=db.Column(db.Boolean)
       

    def __init__(self,cardNumber=None,transactionType=None,transactionSource=None,timestamp=None,amount=None):
        self.cardNumber = cardNumber
        self.transactionType = transactionType
        self.transactionSource=transactionSource
        self.timestamp=timestamp
        self.amount=amount
        


   