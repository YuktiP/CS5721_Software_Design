from app import app,db
from flask import render_template,redirect,url_for,flash,request
from models import Customer, User,Transaction
import forms

@app.route('/', methods=['POST','GET']) 
@app.route('/login', methods=['POST','GET'])
def main():
    form = forms.Login()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(EMAIL=form.EMAIL.data).first()  
        if user and user.check_password(PASSWORD=form.PASSWORD.data):
            return "Logged In"
        flash('Invalid username/password combination')
    #return "Login Again"
    return(render_template('login.html',form=form))

@app.route("/Display",methods=['POST','GET'])
def Display():
    lists=User.query.all()
    return(render_template('Display.html',lists=lists))

@app.route("/Enter_Transaction",methods=['POST','GET'])
def Enter_Transaction():
    form=forms.EnterTransactionForm()
    if form.validate_on_submit():
        txn=Transaction(TRANSACTION_ID=form.TRANSACTION_ID.data,CARD_NUMBER=form.CARD_NUMBER.data,TRANSACTION_TYPE=form.TRANSACTION_TYPE.data,TIMESTAMP=form.TIMESTAMP.data,AMOUNT=form.AMOUNT.data,AUTHORIZED='No')
        txn.Add_Transaction()
        return redirect(url_for('Enter_Transaction'))
    return(render_template('Enter_Txn.html',form=form))    

@app.route("/Enroll",methods=['POST','GET'])
def Enroll():
    form=forms.EnrollForm()
    if form.validate_on_submit():
        cust=Customer(FIRSTNAME=form.FIRSTNAME, SURNAME=form.SURNAME, ADDRESS=form.ADDRESS.data)
        cust.register_User()
        return redirect(url_for('Display'))
    return render_template('Enroll.html',form=form)