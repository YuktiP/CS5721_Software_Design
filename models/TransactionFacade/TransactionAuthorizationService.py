from models.TransactionFacade.CardVerificationService import CardVerificationService
from models.TransactionFacade.AccountService import AccountService
from models.TransactionFacade.LedgerService import LedgerService
from models.Result import Result

class TransactionAuthorizationService():
    def __init__(self):
        self.cardVerificationService = CardVerificationService()
        self.accountService = AccountService()
        self.ledgerService = LedgerService()
    
    def authorizeTransaction(self,transaction):
        resultCard = self.cardVerificationService.verifyCard(transaction.cardNumber)
        resultAccount = self.accountService.verifyAccountBalance(transaction.cardNumber,transaction.transactionAmount)
        if resultCard.isSuccess and resultAccount.isSuccess:
            resultLedger = self.ledgerService.createLedgerTransaction(transaction)
            return resultLedger
        else:
            if not resultCard.isSuccess:
                return resultCard
            elif not resultAccount.isSuccess:
                return resultAccount
            