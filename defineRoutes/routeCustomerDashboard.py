from flask import render_template


@app.route('/User', methods = ['GET'])
def UserDashboard(): 
    return(render_template("CustomerPage.html"))