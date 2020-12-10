
from app import app
from flask import render_template,request
from enums import Enums as en
from models.Batch import BatchProcess as bat
import datetime
from models.Batch import BatchCreateHelper as bh

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
        createBatch = bh.batchHelper()
        batch = createBatch.createBatchObject(request.form)

        batch.CreateBatch()
        batchlist = []
        batchlist.append(batch)

        return (render_template("ScheduleBatchProcess.html",BatchTypes=BatchTypes, BatchProcessTypes=BatchProcessTypes,batchlist=batchlist))

    return(render_template("ScheduleBatchProcess.html",BatchTypes=BatchTypes,BatchProcessTypes=BatchProcessTypes))
    