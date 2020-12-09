import abc

class IDashboard(abc.ABC):
    @abc.abstractmethod
    #added the abstract method
    def getAdminDashboardData():
        pass
