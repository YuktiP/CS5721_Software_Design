from models.DashboardFactory import DashboardFactory 
from app import app
from flask import render_template

@app.route("/Dashboard")
def Dashboard():
    #df = DashboardFactory()
    #dashObj = df.getDashboard("") #Employee/Customer/Admin
    #data = dashObj.GetDashboardData()
    #return(render_template(data.template,data = data))
    
    df = DashboardFactory()
    dashObj = df.getDashboard("/Dashboard") #Employee/Customer/Admin
    data = dashObj.getAdminDashboardData()

    return(render_template(data.template,data = data))