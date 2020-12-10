from Interfaces.IBatch import IBatch
from models.Result import Result

class CalculateInterest(IBatch):

    def __init__(self,batch):
        self.batch=batch

    def Create(self):
        return Result(True,"Batch Created")

    
    def Execute(self):
        return Result(True,"Batch Run SuccessFully")