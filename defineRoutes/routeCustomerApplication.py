from app import app,login_required
from flask import render_template
from models.CustomerApplication import CustomerApplication
import forms


@app.route("/CustomerApplication",methods=['POST','GET'])
#@login_required
def Enroll():
    form=forms.CustomerApplication()
    if form.validate_on_submit():
        cust=CustomerApplication(firstName=form.first_name.data, lastName=form.last_name.data, dateOfBirth=form.date_of_birth.data,address=form.address.data, city=form.city.data, zipcode=form.zipcode.data, monthly_income =form.monthly_income.data, cardType= form.cardType.data, occupation=form.occupation.data, ppsn=form.ppsn.data, contact_number =form.contact_number.data,email=form.email.data,application_type='O',  eligibility=1,error_details='passed')
        cust.CollectApplications()
        return '<h1>Application Submitted</h1>'
    return render_template('CustomerApplication.html',form=form)