from flask_sqlalchemy import SQLAlchemy
from app import db
#from dbController.AccountDBController import AccountDBController
#from dbController.TransactionDBController import TransactionDBController
#from dbController.CardDBController import CardDBController

'''
class Statement():
    def __init__(self, userId):
        self.userId = userId
        
    def getStatement(self):
        AccountDB = AccountDBController()
        accountInfo = AccountDB.getAccountByUserId(self.userId)
        self.cardId = accountInfo.cardId

        CardDB = CardDBController()
        cardInfo = CardDB.getCardById(self.cardId)
        self.cardNumber = cardInfo.cardNumber

        TransactionDB = TransactionDBController()
        self.statement = TransactionDB.getTransactoinsByCardNumber(self.cardNumber)

        return self
        '''