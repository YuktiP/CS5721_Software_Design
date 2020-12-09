
from app import app
from flask import render_template,request
from enums import Enums as en
from models.Batch import BatchProcess as bat
import datetime

@app.route("/batch",methods=['POST','GET'])
def Batch():
    BatchTypes = en.BatchType.list()
    BatchProcessTypes = en.BatchProcessType.list()

    if request.method == 'POST':

        batchType = request.form.get('batchType')
        for b in BatchTypes:
            if b['Label'] == batchType:
                b['Selected']=True
            else:
                b['Selected']=False

        batchProcessType = request.form.get('batchProcessType')
        for b in BatchProcessTypes:
            if b['Label'] == batchProcessType:
                b['Selected']=True
            else:
                b['Selected']=False
        
        batch = bat.BatchProcess()
        batch.batchType = en.BatchType[batchType].value
        batch.batchTypeName = en.BatchType[batchType].name
        batch.batchProcessType = en.BatchProcessType[batchProcessType].value
        batch.isActive = True
        batch.createdDate = datetime.datetime.now()
        batch.createdBy = 1
        if batch.batchType == en.BatchType.Daily:
            batch.date = request.form.get('torundate')
        elif batch.batchType == en.BatchType.Weekly:
            batch.frequency = request.form.get('dayfrequency')
        elif batch.batchType == en.BatchType.Monthly:
            batch.frequency = request.form.get('monthfrequency')
        elif batch.batchType == en.BatchType.Yearly:
            batch.frequency = request.form.get('yearfrequency')
            
        batch.CreateBatch()
        batchlist = []
        batchlist.append(batch)

        return (render_template("ScheduleBatchProcess.html",BatchTypes=BatchTypes, BatchProcessTypes=BatchProcessTypes,batchlist=batchlist))

    return(render_template("ScheduleBatchProcess.html",BatchTypes=BatchTypes,BatchProcessTypes=BatchProcessTypes))
    