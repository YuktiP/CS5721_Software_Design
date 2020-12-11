from app import db

class RolesPermission(db.model):
    moduleId=db.Column(db.Integer)
    roleId=db.Column(db.Integer)

    def __init__(self,roleId,moduleId):
        self.roleId = roleId
        self.moduleId = moduleId