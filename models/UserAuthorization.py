
from Interfaces import IAuthorization as iauth
from app import current_user, db
from models.RolesPermission import RolesPermission

class UserAuthorization(iauth.IAuthorization):

    def __init__(self,requestedUrl):
        self.requestedUrl = requestedUrl
    
    def Authorize(self):

        db.create_all()
        userRole=current_user.getUserRole()
        modules = db.session.query(RolesPermission).all()
        return ""




