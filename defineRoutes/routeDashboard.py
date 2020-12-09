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
    #data2 = None
    #form = forms.BlockCard()
    #if request.method == 'POST':
     #   if request.form.get('add'):
      #      post_id = request.form.get('add')
       #     data2 = dashObj.unblockCard(post_id)
        #    return redirect(url_for('AdminDashboard'))
        #else:
         #   post_id = request.form.get('delete')
          #  data2 = dashObj.blockCard(post_id)
           # return redirect(url_for('AdminDashboard'))
    
    
    