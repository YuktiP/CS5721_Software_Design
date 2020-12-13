class TransactionRequest():
    
    def __init__(self,cardNumber=None,cardPin=None,cardExpiryDate=None,transactionDate=None,transactionType=None,transactionSource=None,transactionAmount=None):
        self.cardNumber = cardNumber
        self.cardPin = cardPin
        self.cardExpiryDate = cardExpiryDate
        self.transactionDate = transactionDate
        self.transactionType = transactionType
        self.transactionSource = transactionSource
        self.transactionAmount = transactionAmount