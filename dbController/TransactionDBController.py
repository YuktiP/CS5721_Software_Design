from app import db
from models.Transactions import Transaction

class TransactionDBController():
    def __init__(self):
        self = self
    
        
    def addTransaction(self,Transaction):
        db.create_all()
        db.session.add(Transaction)
        db.session.commit()     

    def findtotalAmt(self,cardNo):
        self.result=db.session.query(Transaction).filter(Transaction.cardNumber == cardNo).all()
        return(self.result)