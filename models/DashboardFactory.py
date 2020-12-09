from Interfaces import IDashboard
#from models.EmployeeDashboard import EmployeeDashboard
from models.AdminDashboard import AdminDashboard
class DashboardFactory():

    def __init__(self):
        self = self
        
    def getDashboard(self,url):
        #url - employee
        return AdminDashboard()



    # Customer
    # Authorize
    # GetDashboardData






    