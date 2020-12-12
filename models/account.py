from app import db
from dbController.AccountDBController import AccountDBController

class Account(db.Model):
    accountId=db.Column(db.Integer,primary_key=True)
    accountNumber=db.Column(db.BigInteger,unique=True)
    userId=db.Column(db.Integer)
    cardNumber=db.Column(db.BigInteger)
    createdDate=db.Column(db.Date)
    currentBalance=db.Column(db.Integer)
    availableBalance=db.Column(db.Integer)
    minPaymentDue = db.Column(db.Integer)
    totalPaymentDue = db.Column(db.Integer)
    status=db.Column(db.String(10))

    def __init__(self,accountNumber = None, userId=None,user=None, cardNumber=None,card=None,createdDate=None,currentBalance=None,availableBalance=None,status=None,minPaymentDue=None,totalPaymentDue=None):
        self.accountNumber=accountNumber
        self.userId=userId
        self.user = user
        self.cardNumber=cardNumber
        self.card = card
        self.createdDate=createdDate
        self.currentBalance=currentBalance
        self.availableBalance=availableBalance
        self.minPaymentDue=minPaymentDue
        self.totalPaymentDue=totalPaymentDue
        self.status=status

    def addAccount(self):
            accountDb = AccountDBController()
            accountDb.addAccount(self)