from Interfaces import IDashboard

class CustomerDashboard(IDashboard):

    def _init_(self):
        self = self

    def GetDashboardData(self):
        self.url = '/User'
        self.dashboardName = "Customer Home"
        self.template = "CustomerHome.html"
        return self

        