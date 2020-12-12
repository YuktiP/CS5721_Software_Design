import abc

class IDashboard(abc.ABC):
    @abc.abstractmethod
    
    def getDashboardData(self,requestedPage):
        pass