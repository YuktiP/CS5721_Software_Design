from Interfaces.IDashboard import IDashboard

class CustomerDashboard(IDashboard):

    def __init__(self,template=None):
        self.template = template

    def getDashboardData(self,requestedPage):
        self.url = '/customerdashboard'
        self.dashboardName = "Customer Home"
        self.template = "CustomerHome.html"
        return self

        