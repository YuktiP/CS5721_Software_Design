from app import db

class Modules(db.Model):
    __tablename__ = 'module'
    moduleId=db.Column(db.Integer,primary_key=True)
    moduleName=db.Column(db.String(50))
    isDefault=db.Column(db.Boolean)

    def __init__(self,moduleId,moduleName,isDefault):
        self.moduleId = moduleId
        self.moduleName = moduleName
        self.isDefault = isDefault