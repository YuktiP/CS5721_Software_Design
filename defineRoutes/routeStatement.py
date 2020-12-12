import datetime
from app import app, db, current_user
from flask import render_template, session
from models.UserAuthentication import User
from models.Statement import Statement
from app import current_user, login_manager
from app import app,db
from app import app, db, current_user, login_manager
from flask import render_template
from businessController.StatementController import Statement


@app.route('/ViewStatement', methods = ['POST','GET'])
def statement(): 
    userId=current_user.get_id()

    statementObj = Statement(userId)
    fetchedStatement = statementObj.getStatement(userId)
    return(render_template("ViewStatement.html", statement=statementObj))
    fetchedStatement = statementObj.getStatement()
    return(render_template("ViewStatement.html", statement=fetchedStatement))
    

        





    
    

