from app import db

class CustomerApplication(db.Model):

    Id=db.Column(db.Integer,primary_key=True)
    FirstName=db.Column(db.String(20))
    LastName=db.Column(db.String(20))
    Address=db.Column(db.String(40))

    def __init__(self, Id=0,FirstName="",LastName="",Address=""):
        self.Id = Id
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address