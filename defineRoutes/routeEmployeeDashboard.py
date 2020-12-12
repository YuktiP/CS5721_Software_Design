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
from models.onboard.CustomerOnboardService import CustomerOnBoardService
from models.onboard.CustomerOnboardBatchService import CustomerOnBoardBatchService
from businessController.DashboardController import DashboardController
from models.CustomerApplication import CustomerApplication
from dbController.CustAppDBController import CustAppDBController

UPLOAD_FOLDER='/Users/yuktipatil/MySpace'

@app.route('/singleupload',methods=['POST','GET'])
def singleupload():
    #Get Dashboard Data
    dash = DashboardController()
    data = dash.createDashboard('singleupload')

    if request.method=='POST':
        if request.form.get('onboard'):
            applicationId = request.args.get('id')
            #Instantiate
            onboard=CustomerOnBoardService()
            app = CustAppDBController()
            #Get Application to be onboarded
            application = app.getApplicationById(applicationId)
            #Onboard a customer
            result=onboard.onBoardCustomer(application)
            if(result.isSuccess):
                flash(status.text)
    return(render_template(data.template,data=data))

@app.route('/bulkupload', methods=['POST','GET'])
def bulkupload():   
    #Get Dashboard Data
    dash = DashboardController()
    data = dash.createDashboard('bulkupload')

    if request.method=='POST':
        #read file to upload customers to be onboarded
        file = request.files['file']
        filename = secure_filename(file.filename)
        docpath=os.path.join(app.config['UPLOAD_FOLDER'],filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #Instantiate
        onboard = CustomerOnBoardBatchService()
        #Onboard customer batch
        result=onboard.onBoardCustomerBatch(docpath)
        flash(result.text)
        return(render_template('Display.html',data=result.data))
    return(render_template(data.template))    
