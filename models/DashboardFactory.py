from Interfaces import IDashboard
from models.EmployeeDashboard import EmployeeDashboard
from models.AdminDashboard import AdminDashboard

class DashboardFactory():

    def __init__(self):
        self = self
        
    def getDashboard(self,url):
        if (url=='admin'):
            return AdminDashboard()
        else:    
            return EmployeeDashboard()



    # Customer
    # Authorize
    # GetDashboardData






    