from models.DashboardFactory import DashboardFactory 
from models.BlockCard import BlockCard
from models.UnblockCard import UnblockCard
from businessController.BlockCardController import BlockCardController
from businessController.UnblockCardController import UnblockCardController
from businessController.DashboardController import DashboardController
from app import app
from flask import render_template,redirect,url_for,request
import forms

@app.route("/showrequests")
def showRequests():
     dc = DashboardController()
     data = dc.createDashboard('showrequests')
     return(render_template(data.template, data = data))

@app.route("/block", methods=['POST','GET'])
def blockCard():
    dc = DashboardController()
    data = dc.createDashboard('block')
    
    if request.method == 'POST':
        number = request.form.get('delete')
        blockCard = BlockCardController()
        blockCard.initiateBlockCard(number)
        return redirect(url_for('blockCard'))

    return (render_template(data.template, data = data.blockCardRequests))
 
@app.route("/unblock", methods=['POST','GET']) 
def unblockCard():
    dc = DashboardController()
    data = dc.createDashboard('unblock')
    
    if request.method == 'POST':
        number = request.form.get('add')
        ublockCard = UnblockCardController()
        ublockCard.initiateUnblockCard(number)
        return redirect(url_for('unblockCard'))
    
    return (render_template(data.template,data = data.unblockCardRequests))
    
    