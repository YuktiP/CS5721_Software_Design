from models.CustomerApplication import CustomerApplication
from app import app,login_required
from flask import render_template
import forms


@app.route("/CustomerApplication",methods=['POST','GET'])
@login_required
def Enroll():
    form=forms.CustomerApplication()
    if form.validate_on_submit():
        cust=CustomerApplication(first_name=form.first_name.data, last_name=form.last_name.data, date_of_birth=form.date_of_birth.data,address=form.address.data, city=form.city.data, pin=form.pin.data, monthly_income =form.monthly_income.data, card_type= form.card_type.data, occupation=form.occupation.data, ppsn=form.ppsn.data, contact_number =form.contact_number.data,application_type='O',  eligibility=1,error_details='passed')
        cust.CollectApplications()
        return '<h1>Application Submitted</h1>'
    return render_template('CustomerApplication.html',form=form)