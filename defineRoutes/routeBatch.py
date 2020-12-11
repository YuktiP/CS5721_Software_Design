
from app import app
from flask import render_template,request
from enums import Enums as en
from businessController import BatchController as bc

@app.route("/registerbatch",methods=['POST','GET'])
def Batch():
    bController = bc.BatchController()
    BatchTypes = en.BatchType.list()
    BatchProcessTypes = en.BatchProcessType.list()
    if request.method == 'POST':
        bController.registerBatch(request.form)
        batchlist = bController.getAllbatches()
        return (render_template("ScheduleBatchProcess.html",BatchTypes=BatchTypes, BatchProcessTypes=BatchProcessTypes,batchlist=batchlist))
    
    batchlist = bController.getAllbatches()
    return(render_template("ScheduleBatchProcess.html",BatchTypes=BatchTypes,BatchProcessTypes=BatchProcessTypes,batchlist=batchlist))
    

