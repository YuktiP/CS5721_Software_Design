from flask_sqlalchemy import SQLAlchemy
from app import db
from models.UserAuthentication import User
from models.Card import CreditCard
from models.Transactions import Transaction
from dbController.AccountDBController import AccountDBController
from dbController.TransactionDBController import TransactionDBController
from dbController.CardDBController import CardDBController


class Statement():
    def __init__(self,userId):
        self.userId = userId
        
    '''
    def getAccountNumber(self):
        findAccountNumber=User.query.filter_by(userId = self.userId).first()
        self.accountNumber = findAccountNumber.accountNumber
    
    def getCard(self):
        self.getAccountNumber()
        findCard = CreditCard.query.filter_by(accountNumber = self.accountNumber).first()
        self.cardId = findCardId.cardId
        self.cardNumber = findCard.cardNumber
        
    def getStatement(self):
        self.getCard()
        self.statement = Transaction.query.filter_by(cardId = self.cardId).all()
        self.template = "ViewStatement.html"
        
'''
    def getStatement(self,userId):
        total=0
        actObj=AccountDBController()
        cardObj=CardDBController()
        TxnObj=TransactionDBController()
        acctno=actObj.findAccountNumber(userId)
        cardNo=actObj.getCardNumber(acctno)
        self.cardNumber=actObj.convert(cardNo)
        actBal=actObj.getAccountBal(acctno)
        self.actBal=actObj.convert(actBal)
        interest=cardObj.findCardInterest(cardNo)
        print(interest)
        intr=actObj.convertVal(interest)
        exec=TxnObj.findtotalAmt(cardNo)
        for i in exec:
            total=total+i.amount  
        self.statement=exec
        extraIncur=(intr/100)*365
        self.sum=total+extraIncur 
        self.template = "ViewStatement.html"
        return(self)