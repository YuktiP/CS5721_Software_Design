from app import db
class Customer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    FIRSTNAME=db.Column(db.String(20))
    SURNAME=db.Column(db.String(20))
    ADDRESS=db.Column(db.String(20))

    def __repr__(self):
        return f'{self.FIRSTNAME} AND {self.ADDRESS}'
