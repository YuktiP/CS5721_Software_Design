class Transaction(db.Model):
    transaction_id=db.Column(db.Integer,primary_key=True)
    card_number=db.Column(db.Integer)
    transaction_date=db.Column(db.DateTime)
    amount=db.Column(db.Integer)
    transaction_type=db.Column(db.String(30))
    
    def __init__(self, transaction_id,card_number,transaction_type,transaction_date,amount):
        self.transaction_id =transaction_id
        self.card_number = card_number
        self.transaction_type = transaction_type
        self.transaction_date=transaction_date
        self.amount=amount
        


    def Add_Transaction(self):
            db.create_all()
            db.session.add(self)
            db.session.commit() 