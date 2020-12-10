from Interfaces.IBatch import IBatch

class BatchProcessingService():

    def __init__(self,iBatch):
        self.iBatch = iBatch

    def Register(self):
        self.iBatch.Create()

    def Run(self):
        self.iBatch.Run()