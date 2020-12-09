from models.DashboardFactory import DashboardFactory 
from app import app
from flask import render_template,redirect,url_for,request
#from models import DashboardFactory as D
import forms

@app.route("/Dashboard", methods=['POST','GET'])
def AdminDashboard():
    df = DashboardFactory()
    dashObj = df.getDashboard("/Dashboard") #Employee/Customer/Admin
    data = dashObj.getAdminDashboardData()

    return(render_template(data.template,data = data,form = form))
    
    
    