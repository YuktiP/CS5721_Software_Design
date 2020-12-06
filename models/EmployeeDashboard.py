from Interfaces.IDashboard import IDashboard
from models.CustomerApplication import *

class EmployeeDashboard(IDashboard):

    def __init__(self):
        self=self

    def GetDashboardData(self):

        self.dashboardName = "Display a List of Customers to be onboarded"
        
        cust = CustomerApplication(1,"John","Doe","Some place on Earth")
        applicationList = []
        applicationList.append(cust)

        self.template = "OnBoardCustomers.html"
        self.applications = applicationList

        return self

        
        
    