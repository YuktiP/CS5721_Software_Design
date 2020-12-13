from Interfaces.IDashboard import IDashboard
from flask import request, redirect, url_for
from flask import render_template,redirect,request,url_for
from werkzeug.utils import secure_filename
import csv
import pandas as pd 
import os
import urllib.request
from models.UserAuthentication import User
from models.CustomerApplication import CustomerApplication
import datetime
from datetime import date
from app import db
import app
import forms

class EmployeeDashboard(IDashboard):

    def __init__(self,template=None):
        self.template = template

    def getDashboardData(self,requestedPage):
        if requestedPage == 'singleupload':
            app_type = 'O'
            result=db.session.query(CustomerApplication).filter(CustomerApplication.application_type ==app_type).all()
            db.session.query(CustomerApplication).filter(CustomerApplication.application_type ==app_type).update({CustomerApplication.application_type:'A'},synchronize_session=False)
            self.dashboardName = "Display a List of Customers to be onboarded"
            self.template = 'upload.html'
            self.applications = result
        elif requestedPage == 'bulkupload':
            self.template = 'OnBoardCustomers.html'
        return self

