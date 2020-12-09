from Interfaces import IDashboard
from models.EmployeeDashboard import EmployeeDashboard

class DashboardFactory():

    def __init__(self):
        self = self
        
    def getDashboard(self,url):
        #url - employee
        #return EmployeeDashboard()
        if (url=='admin'):
            return AdminDashboard()
        else:    
            return EmployeeDashboard()



    # Customer
    # Authorize
    # GetDashboardData






    