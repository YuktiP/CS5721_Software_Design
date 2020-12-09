from Interfaces.IBatch import IBatch
from models.Result import Result

class CalculateInterest(IBatch):

    def __init__(self):
        self=self

    def Create(self, batch):
        return Result(True,"Batch Created")

    
    def Execute(self, name):
        return Result(True,"Batch Run SuccessFully")