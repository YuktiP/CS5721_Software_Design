from Interfaces import IDashboard
from models.AdminDashboard import AdminDashboard
from models.CustomerDashboard import CustomerDashboard
from models.EmployeeDashboard import EmployeeDashboard
from enums.Enums import *

class DashboardFactory():

    def __init__(self):
        self = self
        
    def getDashboard(self,url):

        request = url.split('/')
        if request[0]== Role(Role.Admin).name:
            return AdminDashboard()
        elif request[0]== Role(Role.Employee).name:   
            return EmployeeDashboard()
        elif request[0]== Role(Role.Customer).name:
            return CustomerDashboard()



    # Customer
    # Authorize
    # GetDashboardData






    