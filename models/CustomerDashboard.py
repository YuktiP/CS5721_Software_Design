from Interfaces.IDashboard import IDashboard

class CustomerDashboard(IDashboard):

    def _init_(self):
        self = self

    def getDashboardData(self,requestedPage):
        self.url = '/User'
        self.dashboardName = "Customer Home"
        self.template = "CustomerHome.html"
        return self

        