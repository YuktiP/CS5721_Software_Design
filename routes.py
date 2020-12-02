from app import app,db
from flask import render_template,redirect,url_for
from models import Customer
import forms

#@app.route("/",methods=['POST','GET'])
#def login():
    
@app.route("/Display",methods=['POST','GET'])
def Display():
    lists=Customer.query.all()
    return(render_template('Display.html',lists=lists))
@app.route("/Enroll",methods=['POST','GET'])
def Enroll():
    form=forms.EnrollForm()
    if form.validate_on_submit():
        cust=Customer(FIRSTNAME=form.FIRSTNAME.data,SURNAME=form.SURNAME.data,ADDRESS=form.ADDRESS.data)
        cust.register_User()
        return redirect(url_for('Display'))
    return render_template('Enroll.html',form=form)