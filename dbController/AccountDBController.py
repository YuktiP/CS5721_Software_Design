from models.UserAuthentication import User
from app import db

class AccountDBController():
    def __init__(self):
        self = self
    def addAccount(self,account):
        db.create_all()
        db.session.add(account)
        db.session.commit()
    def findAccountNumber(self,userId):
        self.result=db.session.query(User.accountNumber).filter(User.userId==userId ).all()  
        return (self.result)  
    def getCardNumber(self,account):
        self.result=db.session.query(Account.cardNumber).filter(Account.accountNumber==account).all()
        return(self.result)
    def getAccountBal(self,account):
        self.result=db.session.query(Account.availableBalance).filter(Account.accountNumber==account).all()


