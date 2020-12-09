from Interfaces.IDashboard import IDashboard
from flask import request, redirect, url_for
from flask import render_template,redirect,request,url_for
from werkzeug.utils import secure_filename
import csv
import pandas as pd 
import os
import urllib.request
from models.UserAuthentication import User
from models.card import Creditcard
from models.account import Account
from models.CustomerApplication import CustomerApplication
import datetime
from datetime import date
from passgen import Randpass
from app import db
import app
import forms

class EmployeeDashboard(IDashboard):

    def __init__(self):
        self=self

    def GetDashboardData(self):
        result=db.session.query(CustomerApplication).all()
        self.dashboardName = "Display a List of Customers to be onboarded"
        print(result)
        self.template = "upload.html"
        self.applications = result
        return self

