import abc

class IAuthorization(abc.ABC):
    @abc.abstractmethod
    def Authorize(self):
        pass