import abc

class AbstractBuilder(abc.ABC):

    @abc.abstractmethod
    def getUser(self,customerApplication):
        pass

    @abc.abstractmethod
    def getCard(self,customerApplication):
        pass

