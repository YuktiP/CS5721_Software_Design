

class AccountDBController():

    def __init__(self):
        self = self
    def addAccount(self,account):
        db.create_all()
        db.session.add(account)
        db.session.commit()