from flask_sqlalchemy import SQLAlchemy
from app import db
from models.UserAuthentication import User
from models.Card_Test import Card
from models.Transaction_Test import Transaction


class Statement():
    def __init__(self, userId):
        self.userId = userId
        
    
    def getAccountNumber(self):
        findAccountNumber=User.query.filter_by(userId = self.userId).first()
        self.accountNumber = findAccountNumber.accountNumber
    
    def getCardno(self):
        self.getAccountNumber()
        findCardNumber = Card.query.filter_by(accountNumber = self.accountNumber).first()
        self.cardNumber = findCardNumber.cardNumber

    def getStatement(self):
        self.getCardno()
        self.statement = Transaction.query.filter_by(cardNumber = self.cardNumber).all()
        self.template = "ViewStatement.html"
        
