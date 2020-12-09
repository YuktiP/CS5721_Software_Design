from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer,primary_key=True)
    card_number=db.Column(db.Integer,primary_key=True)
    current_credit_limit=db.Column(db.Integer)
    available_credit_limit=db.Column(db.Integer)
    pin=db.Column(db.Integer)
    expiry_date=db.Column(db.String(255))
    card_status=db.Column(db.Integer)
    block_request=db.Column(db.Integer)
       

    def __init__(self, card_number, current_credit_limit, available_credit_limit,pin,expiry_date,card_status,block_request):
        self.card_id = card_id
        self.card_number = card_number
        self.current_credit_limit = current_credit_limit
        self.available_credit_limit = available_credit_limit
        self.pin=pin
        self.expiry_date=expiry_date
        self.card_status=card_status
        self.block_request=block_request
