from models.DashboardFactory import DashboardFactory 
from models.BlockCard import BlockCard
from models.UnblockCard import UnblockCard
from businessController.BlockCardController import BlockCardController
from businessController.UnblockCardController import UnblockCardController
from businessController.DashboardController import DashboardController
from app import app
from flask import render_template,redirect,url_for,request
import forms

 @app.route("/ShowRequests")
 def Dashboard():
     dc = DashboardController()
     data = dc.createDashboard('registerbatch')

     return(render_template(data.template,data = data))

@app.route("/Block", methods=['POST','GET'])
def blockCard():
    df = BlockCard()
    data2 = df.actionOnCustomerCardList()
    bObj = BlockCardController()
    number = request.form.get('delete')
    
    if request.method == 'POST':
        bObj.initiateBlockCard(number)
        return redirect(url_for('blockCard'))

    return (render_template('BlockCard.html', data2 = data2))
 
@app.route("/Unblock", methods=['POST','GET']) 
def unblockCard():
    df = UnblockCard()
    data3 = df.actionOnCustomerCardList()
    bObj1 = UnblockCardController()
    number = request.form.get('add')
    if request.method == 'POST':
        bObj1.initiateUnblockCard(number)
        return redirect(url_for('unblockCard'))
    
    return (render_template('UnblockCard.html',data3 = data3))
    
    