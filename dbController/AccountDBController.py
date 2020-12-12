from models.account import Account
from app import db

class AccountDBController():

    def __init__(self):
        self = self
        
    def addAccount(self,Account):
        db.create_all()
        db.session.add(Account)
        db.session.commit()
    
    def getAccountByUserId(self, userId):
        return db.session.query(Account).filter_by(userId = userId).first()