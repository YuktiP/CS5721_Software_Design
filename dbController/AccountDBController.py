
from models.account import Account
from app import db

class AccountDBController():

    def __init__(self):
        self = self

    
    def getAccountByUserId(self, userId):
        return db.session.query(Account).filter_by(userId = userId).first()

    def addAccount(self,account):
        db.create_all()
        db.session.add(account)
        db.session.commit()
