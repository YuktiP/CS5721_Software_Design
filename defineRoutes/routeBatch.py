
from app import app
from flask import render_template,request,url_for
from enums import Enums as en
from businessController import BatchController as bc
from businessController.DashboardController import DashboardController

@app.route("/registerbatch",methods=['POST','GET'])
def registerBatch():

    bController = bc.BatchController()
    dash = DashboardController()
    data = dash.createDashboard('registerbatch')

    if request.method == 'POST':
        bController.registerBatch(request.form)
        batchlist = bController.getAllbatches()
        return (render_template(data.template,BatchTypes=data.batchTypes, BatchProcessTypes=data.batchProcessTypes,batchlist=batchlist))
    
    batchlist = bController.getAllbatches()
    return(render_template(data.template,BatchTypes=data.batchTypes,BatchProcessTypes=data.batchTypes,batchlist=batchlist))
    

