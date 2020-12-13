from app import app,login_required
from flask import render_template
from models.CustomerApplication import CustomerApplication
from businessController.EnrollController import EnrollController
import forms


@app.route("/CustomerApplication",methods=['POST','GET'])
#@login_required
def Enroll():
    form=forms.CustomerApplication()
    if form.validate_on_submit():
        enroll = EnrollController()
        enroll.enrollForCard(form)
        return '<h1>Application Submitted</h1>'
    return render_template('CustomerApplication.html',form=form)