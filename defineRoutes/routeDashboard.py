from models.DashboardFactory import DashboardFactory 
from app import app,db
import os
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import csv
import pandas as pd 
from flask import render_template,redirect,request,url_for
from models.card import Creditcard
from models.account import Account
from models.UserAuthentication import User
from defineRoutes.onBoard import Onboard
import datetime
from datetime import date
from passgen import Randpass
UPLOAD_FOLDER='C:/uploads'



app.route("/Dashboard")
def Dashboard():
    df = DashboardFactory()
    dashObj = df.getDashboard("admin") #Employee/Customer/Admin
    data = dashObj.getAdminDashboardData()

    return(render_template(data.template,data = data))





@app.route('/EmployeeDashboard', methods=['POST','GET'])
def EmployeeDashboard():   
    if request.method=='POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        x=os.path.join(app.config['UPLOAD_FOLDER'],filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        add=Onboard()
        data=add.BulkOnboard(x)
        flash('File successfully uploaded')
        return(render_template('Display.html',data=data.result))
    return(render_template('OnBoardCustomers.html'))

@app.route('/singleUpload',methods=['POST','GET'])
def singleUpload():
    f=DashboardFactory()
    fobj=f.getDashboard("employee")
    data=fobj.GetDashboardData()
    if request.method=='POST':
        if request.form.get('onboard'):
            add=Onboard()
            add.singleOnboard(data.applications)
            flash('Onboarded Sucessfully')
    return(render_template(data.template,data=data))