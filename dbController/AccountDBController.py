from models.UserAuthentication import User
from app import db
from models.Account import Account

class AccountDBController():
    def __init__(self):
        self = self
    def addAccount(self,account):
        db.create_all()
        db.session.add(account)
        db.session.commit()
    def convert(self,integers):
        subval=str(integers).strip('[]')
        subval=subval.replace(',', '')
        subval=subval.replace('(','')
        subval=subval.replace(')','')
        self.val=int(subval)
        return(self.val)  

    def convertVal(self,val):
        subval=str(val).strip('[]')
        subval=subval.replace('(','')
        subval=subval.replace(')','')
        subval=subval.replace(',', '')
        self.val=int(subval)
        return(self.val)  


    def findAccountNumber(self,userId):
        self.result=db.session.query(Account.accountNumber).filter(Account.userId==userId ).all()  
        return (self.result)  
        
    def getCardNumber(self,account):
        self.result=db.session.query(Account.cardNumber).filter(Account.accountNumber==account).all()
        return(self.result)

    def getAccountBal(self,account):
        self.result=db.session.query(Account.availableBalance).filter(Account.accountNumber==account).first()
        return self.result

    def getAccountByCardNumber(self,cardNum):
        self.result = db.session.query(Account).filter(Account.cardNumber==cardNum).first()
        return self.result

    def setAccountBalance(self, balance):
        db.session.query(Account).filter(Account.accountNumber == accountNumber).update({Account.availableBalance:balance})
        db.session.commit()

        

