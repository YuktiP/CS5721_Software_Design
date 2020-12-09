from app import db,app
from Interfaces.IDashboard import IDashboard
from models.Card import *


class AdminDashboard(IDashboard):

    def __init__(self):
        self = self
    
    def getAdminDashboardData(self):
        self.template = 'AdminPage.html'
        
        return self

    

