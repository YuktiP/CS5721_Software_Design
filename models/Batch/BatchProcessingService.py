from Interfaces.IBatch import IBatch

class BatchProcessingService():

    def Register(self,IBatch):
        return "Register a Batch"

    def Run(self,name):
        return "Write Logic to run a batch process"