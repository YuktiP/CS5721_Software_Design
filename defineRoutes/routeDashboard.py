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
from models.Card import CreditCard
from models import UserAuthorization as auth
from defineRoutes.onBoard import Onboard
import datetime
from datetime import date
from Interfaces import IAuthorization as Iauth

from businessController.DashboardController import DashboardController



@app.route("/Dashboard")
def Dashboard():

    dash = DashboardController()
    data = dash.createDashboard(None)
    return redirect(data) 