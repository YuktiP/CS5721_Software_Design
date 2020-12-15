from Interfaces.IDashboard import IDashboard
from app import current_user

from models.Statement import Statement
class CustomerDashboard(IDashboard):

    def __init__(self,template=None):
        self.template = template
    def getDashboardData(self,requestedPage):
        if requestedPage == "viewstatement":
            self.statementObj = Statement(current_user.get_id())
            self.fetchedStatement = self.statementObj.getStatement(current_user.get_id())
            self.url = '/viewstatement'
            self.dashboardName = "View Statement"
            self.template = "ViewStatement.html"
        return self    

        