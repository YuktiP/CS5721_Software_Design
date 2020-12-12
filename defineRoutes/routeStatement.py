from app import app, db, current_user, login_manager
from flask import render_template
from businessController.StatementController import Statement


@app.route('/ViewStatement', methods = ['POST','GET'])
def statement(): 
    userId=current_user.get_id()

    statementObj = Statement(userId)
    fetchedStatement = statementObj.getStatement()
    return(render_template("ViewStatement.html", statement=fetchedStatement))
    

        





    
    

