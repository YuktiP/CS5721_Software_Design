from Interfaces.IBatch import IBatch


class BatchProcessingService():

    def __init__(self,iBatch):
        self.iBatch = iBatch

    def Register(self,form):
        return self.iBatch.Create(form)

    def Run(self):
        self.iBatch.Run()