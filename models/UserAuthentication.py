from app import db, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    userId=db.Column(db.Integer,primary_key=True)
    accountNumber=db.Column(db.BigInteger)
    userName=db.Column(db.String(200))
    password=db.Column(db.String(200))
    firstName=db.Column(db.String(20))
    lastName=db.Column(db.String(20))
    Role=db.Column(db.String(20))
    dob=db.Column(db.Date)
    email=db.Column(db.String(200))
    address=db.Column(db.String(200))
    city=db.Column(db.String(200))
    zipcode=db.Column(db.Integer)
    occupation=db.Column(db.String(200))
    monthlyIncome=db.Column(db.Integer)

    def __init__(self,userId=None,accountNumber=None,userName=None,password=None,firstName=None,lastName=None,Role=None,dob=None,email=None,address=None,city=None,zipcode=None,occupation=None,monthlyIncome=None):
        self.userId =userId
        self.accountNumber = accountNumber
        self.userName = userName
        self.password=password
        self.firstName=firstName
        self.lastName=lastName
        self.Role=Role
        self.dob=dob
        self.email=email
        self.address=address
        self.city=city
        self.zipcode=zipcode
        self.occupation=occupation
        self.monthlyIncome=monthlyIncome
        
    def addUser(self):
        db.create_all()
        db.session.add(self)
        db.session.commit()    

    def get_id(self):
           return (self.userId)

    def getUserRole(self):
           return (self.Role)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)