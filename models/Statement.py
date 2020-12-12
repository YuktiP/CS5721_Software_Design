from flask_sqlalchemy import SQLAlchemy
from app import db
from models.UserAuthentication import User
from models.Card import CreditCard
from models.Transactions import Transaction
from dbController.AccountDBController import AccountDBController
from dbController.TransactionDBController import TransactionDBController
from dbController.CardDBController import CardDBController


class Statement():
    def __init__(self, userId):
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
        actBal=actObj.getAccountBal(acctno)
        interest=cardObj.findCardInterest(cardNo)
        exec=TxnObj.findtotalAmt(cardNo)
        for i in exec:
            total=total+i.amount  
        self.statement=exec
        total=total*interest
        self.sum=total
        for j in actBal:
            self.avlbal=j    
        self.template = "ViewStatement.html"
        


        '''
        findAccountNumber=db.session.query(User.accountNumber).filter(User.userId==952695 ).all()
        print(findAccountNumber)
        findCardNo=db.session.query(Account.cardNumber).filter(Account.accountNumber ==findAccountNumber).all()
        findCardInterest=db.session.query(CreditCard.interest).filter(CreditCard.cardNumber==findCardNo)
        currentLimit=db.session.query(Account.currentcreditLimit).filter(Account.accountNumber ==findAccountNumber).all()
        print(findCardNo)
        exec = db.session.query(Transaction).filter(Transaction.cardNumber == findCardNo ).all()'''
            
