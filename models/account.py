from app import db
class Account(db.Model):
    accountId=db.Column(db.Integer,primary_key=True)
    accountNumber=db.Column(db.BigInteger,unique=True)
    userId=db.Column(db.Integer)
    cardNumber=db.Column(db.BigInteger)
    createdDate=db.Column(db.Date)
    currentcreditLimit=db.Column(db.Integer)
    availablecreditLimit=db.Column(db.Integer)
    status=db.Column(db.String(10))
       

    def __init__(self,accountNumber,userId,cardNumber,createdDate,currentcreditLimit,availablecreditLimit,status):
        self.accountNumber=accountNumber
        self.userId=userId
        self.cardNumber=cardNumber
        self.createdDate=createdDate
        self.currentcreditLimit=currentcreditLimit
        self.availablecreditLimit=availablecreditLimit
        self.status=status
    def addAccount(self):
            db.create_all()
            db.session.add(self)
            db.session.commit()