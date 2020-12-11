from Interfaces import IDashboard

class CustomerDashboard(IDashboard):

    def _init_(self):
        self = self

    def GetDashboardData(self):
        self.dashboardName = "Customer Home"
        self.template = "CustomerHome.html"
        return self

        