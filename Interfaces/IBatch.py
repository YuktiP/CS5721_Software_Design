import abc
from models.Result import Result

class IBatch(abc.ABC):

    @abc.abstractmethod
    def Create(self,form) -> Result:
        pass

    @abc.abstractmethod
    def Execute(self,name)-> Result:
        pass