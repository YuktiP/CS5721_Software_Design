from flask import render_template


@app.route('/customerdashboard', methods = ['GET'])
def UserDashboard(): 
    return(render_template("CustomerPage.html"))