from models.account import Account

class AccountDBController():

    def __init__(self):
        self = self
    def addAccount(self,Account):
        db.create_all()
        db.session.add(Account)
        db.session.commit()