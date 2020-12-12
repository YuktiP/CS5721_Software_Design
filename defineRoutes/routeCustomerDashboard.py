from flask import render_template
from app import app,db


@app.route('/customerdashboard', methods = ['POST','GET'])
def customerdashboard(): 
    return(render_template("CustomerPage.html"))