from Interfaces.IBatch import IBatch
from models.Result import Result
from app import db

class UpdateReportingBD(IBatch):

    def __init__(self):
        self=self

    def Create(self,batch):
        db.create_all()
        db.session.add(batch)
        db.session.commit()

    
    def Execute(self):
        return Result(True,"Batch Run SuccessFully")