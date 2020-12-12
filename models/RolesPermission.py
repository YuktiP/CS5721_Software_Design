from app import db

class RolesPermission(db.Model):
    permissionId=db.Column(db.Integer,primary_key=True)
    moduleId=db.Column(db.Integer)
    roleId=db.Column(db.Integer)

    def __init__(self,roleId,moduleId):
        self.roleId = roleId
        self.moduleId = moduleId

    def CreateRolePermission(self):
        db.create_all()
        db.session.add(self)
        db.session.commit()  