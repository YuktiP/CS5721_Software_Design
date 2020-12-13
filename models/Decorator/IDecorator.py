import abc

class IDecorator(abc.ABC):
    @abc.abstractmethod
    
    def getCreditLimit(self):
        pass

    def getInterest(self):
        pass