
from flask import render_template,request, redirect, flash, url_for
from app import app,db
from flask_login import current_user
from businessController.BlockCardController import BlockCardController



@app.route('/customerdashboard', methods = ['POST','GET'])
def customerdashboard(): 
    return(render_template("CustomerPage.html"))
'''
def getDashboardData(self,requestedPage):
 if requestedPage == "viewstatement":
 self.statementObj = Statement()
 #self.fetchedStatement = statementObj.getStatement(userId)
 self.url = '/viewstatement'
 self.dashboardName = "View Statement"
 self.template = "ViewStatement.html"
 return self
'''
'''
@app.route('/customerdashboard', methods = ['GET'])
def UserDashboard(): 
    if request.method =='POST':
        if "viewstatement" in request.form:
            return redirect(url_for('.statement'))

        elif "blockcard" in request.form:
            userId = current_user.get_id()
            blockCardRequest = BlockCardRequest(userId)
            currentBlockRequestStatus = blockCardRequest.currentBlockRequest()

            if currentBlockRequestStatus == 1 :
                message = "A block request has already been lodged for this card."
                flash(message)
                return redirect(url_for('UserDashboard'))

            else:
                blockCardRequest.blockRequest()
                message = "A block request has been lodged."
                flash(message) 
                return redirect(url_for('UserDashboard'))
            
#         elif "changepin" in request.form: 
#             return redirect(url_for('UserDashboard'))

    elif request.method == 'GET':
        return(render_template("CustomerPage.html"))
'''
