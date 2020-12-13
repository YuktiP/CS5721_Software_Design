from app import app
from flask import redirect
from flask import redirect
from businessController.DashboardController import DashboardController



@app.route("/Dashboard")
def Dashboard():

    dash = DashboardController()
    data = dash.createDashboard(None)
    return redirect(data) 