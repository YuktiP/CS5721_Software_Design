from models.UserAuthentication import User
from app import db

class UserDBController():
    def __init__(self):
        self = self
    def addUser(self,User):
        db.create_all()
        db.session.add(User)
        db.session.commit()