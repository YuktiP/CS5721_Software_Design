from dbController.TransactionDBController import TransactionDBController
from models.Result import Result
from models.Transactions import Transaction

class LedgerService():

    def __init__(self):
        self = self

    def createLedgerTransaction(self,transEntry):
        # Use Try and Exception
        transDB=TransactionDBController()
        transaction = Transaction()
        transaction.cardNumber=transEntry.cardNumber
        transaction.transactionType=transEntry.transactionType
        transaction.transactionSource=transEntry.transactionSource
        transaction.timestamp=transEntry.transactionDate
        transaction.amount=transEntry.transactionAmount
        transDB.addTransaction(transaction)
        return Result(True, "Transaction Added")

        
            