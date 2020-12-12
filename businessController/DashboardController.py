from models.UserAuthorization import UserAuthorization
from models.DashboardFactory import DashboardFactory
class DashboardController():
    def __init__(self):
        self = self

    def createDashboard(self,requestedUrl):

        authorize = UserAuthorization(requestedUrl)
        result = authorize.Authorize()
        
        if not result.isSuccess:
            return "" #redirect to no access page
        
        if not requestedUrl:
            return "/" + result.text.split('/')[1]

        df = DashboardFactory()
        dashObj = df.getDashboard(result.text) 
        data = dashObj.getDashboardData(requestedUrl)
        return data
