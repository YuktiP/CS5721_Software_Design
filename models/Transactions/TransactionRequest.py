class TransactionRequest(db.Model):
    
    
    def __init__(self,cardNumber,transactionType,transactionDate,amount):
        self.card_number = card_number
        self.transaction_type = transaction_type
        self.transaction_date=transaction_date
        self.amount=amount