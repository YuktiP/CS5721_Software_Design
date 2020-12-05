from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
#from flask_mysqldb import MySQL

class Customer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    FIRSTNAME=db.Column(db.String(20))
    SURNAME=db.Column(db.String(20))
    ADDRESS=db.Column(db.String(20))
    
    def __init__(self, FIRSTNAME, SURNAME, ADDRESS):
        self.FIRSTNAME = FIRSTNAME
        self.SURNAME = SURNAME
        self.ADDRESS = ADDRESS
        
    def register_User(self):
        db.create_all()
        db.session.add(self)
        db.session.commit()

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    EMAIL=db.Column(db.String(25))
    PASSWORD=db.Column(db.String(25))
    ROLE=db.Column(db.String(1))

    def __init__(self, EMAIL, PASSWORD, ROLE):
        self.EMAIL = EMAIL
        self.PASSWORD = PASSWORD
        self.ROLE = 'U'

    def Login(self):
        db.create_all()
        db.session.add(self)
        db.session.commit()

    def set_password(self, PASSWORD):
	    self.PASSWORD = generate_password_hash(PASSWORD, method='sha256')
    
    def check_password(self, PASSWORD):
        #Check hashed password.
        if self.PASSWORD == PASSWORD:
            return True
        #return check_password_hash(self.PASSWORD, PASSWORD)