from enums import Enums as en
from models.Batch import BatchProcess as bat
import datetime
from app import db


class batchHelper():

    def __init__(self):
        self=self

    def createBatchObject(self,form) -> bat.BatchProcess:
        batchType = form.get('batchType')
        batchProcessType = form.get('batchProcessType')
        batch = bat.BatchProcess()
        batch.batchType = en.BatchType[batchType].value
        batch.batchTypeName = en.BatchType[batchType].name
        batch.batchProcessType = en.BatchProcessType[batchProcessType].value
        batch.batchProcessTypeName = en.BatchProcessType[batchProcessType].name
        batch.isActive = True
        batch.createdDate = datetime.datetime.now()
        batch.createdBy = 1
        if batch.batchType == en.BatchType(en.BatchType.Daily).name:
            batch.date = request.form.get('torundate')
        elif batch.batchType == en.BatchType(en.BatchType.Weekly).name:
            batch.frequency = form.get('dayfrequency')
        elif batch.batchType == en.BatchType(en.BatchType.Monthly).name:
            batch.frequency = form.get('monthfrequency')
        elif batch.batchType == en.BatchType(en.BatchType.Yearly).name:
            batch.frequency = form.get('yearfrequency')
        return batch

    def getBatches(self,batches):
        for b in batches:
            b.batchTypeName = en.BatchType(b.batchType).name
            b.batchProcessTypeName = en.BatchProcessType(b.batchProcessType).name
        return batches
