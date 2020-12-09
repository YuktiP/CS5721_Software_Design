import abc

class IDashboard(abc.ABC):
    @abc.abstractmethod
    def getAdminDashboardData():
        pass
