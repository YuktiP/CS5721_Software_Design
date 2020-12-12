
from Interfaces import IAuthorization as iauth
from app import current_user, db
from models.RolesPermission import RolesPermission
from models.Modules import Modules
from enums.Enums import *
from models.Result import Result

class UserAuthorization(iauth.IAuthorization):

    def __init__(self,requestedUrl):
        self.requestedUrl = requestedUrl
    
    def Authorize(self):
        userRole = current_user.getUserRole()
        modulesforRole = db.session.query(RolesPermission).filter(RolesPermission.roleId == userRole).all()
        
        moduleUrl = None
        if not self.requestedUrl:
            for m in modulesforRole:
                module = db.session.query(Modules).filter(Modules.moduleId == m.moduleId).first()
                if module.isDefault:
                     moduleUrl = module.moduleName
        else:
            for m in modulesforRole:
                module = db.session.query(Modules).filter(Modules.moduleId == m.moduleId).first()
                if module.moduleName == self.requestedUrl:
                     moduleUrl = module.moduleName
        
        if not moduleUrl:
            return Result(isSuccess=False, text="User not Authorized")
        Url = Role(int(userRole)).name + '/' + moduleUrl
        return Result(isSuccess = True, text = Url)




