from models.DashboardFactory import DashboardFactory 
from app import app,db,current_user
import os
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import csv
import pandas as pd 
from flask import render_template,redirect,request,url_for

from models.UserAuthentication import User
from defineRoutes.onBoard import Onboard
import datetime
from datetime import date
from models.onboard.CustomerOnboardService import CustomerOnboardService 
from models.onboard.CustomerOnboardBatchService import CustomerOnBoardBatchService

UPLOAD_FOLDER='/Users/yuktipatil/MySpace'


@app.route('/EmployeeDashboard', methods=['POST','GET'])
def EmployeeDashboard():   
    if request.method=='POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        docpath=os.path.join(app.config['UPLOAD_FOLDER'],filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        onboard = CustomerOnBoardBatchService()
        data=onboard.onBoardCustomerBatch(docpath)
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
            applicationId = request.args.get('id')
            onboard=CustomerOnBoardService()
            application = db.session.query(CustomerApplication).filter(CustomerApplication.id == applicationId).first()
            
            status=onboard.onBoardCustomer(application)
            if(status.isSuccess):
                flash(status.text)
    return(render_template(data.template,data=data))