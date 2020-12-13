from dbController.AccountDBController import AccountDBController
from models.Result import Result

class AccountService():

    def __init__(self):
        self = self

    def verifyAccountBalance(self,cardNum,amount):
        accountDB = AccountDBController()
        account = accountDB.getAccountByCardNumber(cardNum)

        hasBalance = account.availableBalance > amount
        if hasBalance:
            return Result(hasBalance, "Account Balance Verified")
        else:
            return Result(hasBalance, "Not enough Account Balance")

    def deductAccountAvailableBalance(self,amount,cardNum,transType):
        accountDB = AccountDBController()
        #transType - Depending on transaction type the amount would be added or deducted
        account = accountDB.getAccountByCardNumber(cardNum)
        accBalance = account.availableBalance - amount
        accountDB.setAccountBalance(accBalance)