from app import db
from models.Transactions import Transaction

class TransactionDBController():
    def __init__(self):
        self = self
    
        
    def addTransaction(self,Transaction):
        db.create_all()
        db.session.add(Transaction)
        db.session.commit()                 