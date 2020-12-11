from app import db
from models.Batch.BatchProcess import BatchProcess
class BatchDBController():

    def __init__(self):
        self = self

    def createBatch(self,batch):
        db.create_all()
        db.session.add(batch)
        db.session.commit()

    def getAllRegisteredBatches(self):
        return db.session.query(BatchProcess).all()