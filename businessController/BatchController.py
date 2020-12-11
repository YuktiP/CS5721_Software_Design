import models.Batch.BatchProcessingService as bp
from models.Batch import CalculateInterest as c,SettleTransactions as s,GenerateStatement as g, EmailStatement as e, UpdateReportingDB as u
from dbController.BatchDBController import BatchDBController
import enums.Enums as en
from models.Batch.BatchCreateHelper import batchHelper

class BatchController():
    def __init__(self):
        self = self

    def registerBatch(self, form):
        batchProcessType = form.get('batchProcessType')
        batchObj = None
        if batchProcessType == en.BatchType(en.BatchProcessType.CalculateInterest).name:
            batchObj = c.CalculateInterest()
        elif batchProcessType == en.BatchType(en.BatchProcessType.SettleTransactions).name:
            batchObj = s.SettleTransactions()
        elif batchProcessType == en.BatchType(en.BatchProcessType.GenerateStatement).name:
            batchObj = g.GenerateStatement()
        elif batchProcessType == en.BatchType(en.BatchProcessType.EmailStatement).name:
            batchObj = e.EmailStatement()
        elif batchProcessType == en.BatchType(en.BatchProcessType.UpdateReportingDB).name:
            batchObj = u.UpdateReportingBD()

        bProcess = bp.BatchProcessingService(batchObj)
        batch = bProcess.Register(form)
        batchDB = BatchDBController()
        batchDB.createBatch(batch)

    def getAllbatches(self):
        batchDB = BatchDBController()
        batches = batchDB.getAllRegisteredBatches()
        bhelper = batchHelper()
        return bhelper.getBatches(batches)



