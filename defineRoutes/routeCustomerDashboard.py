from flask import render_template
from app import app

@app.route('/customerdashboard', methods = ['GET'])
def UserDashboard(): 
    return(render_template("CustomerPage.html"))