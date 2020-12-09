import abc
from models.Batch import Batch
from models.Result import Result

class IBatch(abc.ABC):
    @abc.abstractmethod
    def Create(self,batch) -> Result:
        pass

    @abc.abstractmethod
    def Execute(self,name)-> Result:
        pass