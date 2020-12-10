from app import db

class Role(db.model):

    roleId=db.Column(db.Integer,unique=True)
    roleName=db.Column(db.String(50))

    def __init__(self,roleId,roleName):
        self.roleId = roleId
        self.roleName = roleName

    