from flask_sqlalchemy import SQLAlchemy
from app import db
from models.UserAuthentication import User
from models.card import Creditcard
from models.Transactions import Transaction


class Statement():
    def __init__(self, userId):
        self.userId = userId
        
    
    def getAccountNumber(self):
        findAccountNumber=User.query.filter_by(userId = self.userId).first()
        self.accountNumber = findAccountNumber.accountNumber
    
    def getCard(self):
        self.getAccountNumber()
        findCard = Card.query.filter_by(accountNumber = self.accountNumber).first()
        self.cardId = findCardId.cardId
        self.cardNumber = findCard.cardNumber
        
    def getStatement(self):
        self.getCard()
        self.statement = Transaction.query.filter_by(cardId = self.cardId).all()
        self.template = "ViewStatement.html"
        
