import datetime
from app import app, db, current_user
from flask import render_template, session
from models.UserAuthentication import User
from models.Statement import Statement
from app import current_user, login_manager
from app import app,db
from app import app, db, current_user, login_manager
from flask import render_template
from businessController.DashboardController import DashboardController
#from businessController.StatementController import Statement


@app.route('/viewstatement', methods = ['POST','GET'])
def statement(): 
#userId=current_user.get_id()
    dash = DashboardController()
    data = dash.createDashboard('viewstatement')
    return(render_template(data.template, statement=data.statementObj))
 #fetchedStatement = statementObj.getStatement()
 #return(render_template("ViewStatement.html", statement=fetchedStatement))
    '''
    #userId=current_user.get_id()
    userId=408106
    statementObj = Statement(userId)
    fetchedStatement = statementObj.getStatement(userId)
    return(render_template("ViewStatement.html", statement=statementObj))
    #fetchedStatement = statementObj.getStatement()
    #return(render_template("ViewStatement.html", statement=fetchedStatement))
'''
    #userId=current_user.get_id()
 
 #userId=408106
 # statementObj = Statement(userId)
 # self.fetchedStatement = statementObj.getStatement(userId)
 # self.url = '/viewstatement'
 # self.dashboardName = "View Statement"
 # self.template = "ViewStatement.html"
 

 #fetchedStatement = statementObj.getStatement()
 #return(render_template("ViewStatement.html", statement=fetchedStatement))

    

        





    
    

