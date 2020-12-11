from app import db

class Modules(db.model):
    moduleId=db.Column(db.Integer,unique=True)
    moduleName=db.Column(db.String(50))
    isDefault=db.Column(db.Boolean)

    def __init__(self,moduleId,moduleName,isDefault):
        self.moduleId = moduleId
        self.moduleName = moduleName
        self.isDefault = isDefault