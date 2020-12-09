from app import db, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(25))
    password=db.Column(db.String(25))
    role=db.Column(db.Integer)

    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        

    '''def set_password(self, PASSWORD):
	    self.PASSWORD = generate_password_hash(PASSWORD, method='sha256')'''
    
    def checkPassword(self, password):
        #Check hashed password.
        if self.password == password:
            return True
        #return check_password_hash(self.PASSWORD, PASSWORD)