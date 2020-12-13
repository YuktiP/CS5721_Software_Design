from app import app,db
from flask import render_template,redirect,url_for,flash,request
from models.Transactions import Transaction
from datetime import datetime
from businessController.TransactionController import TransactionController
import forms

@app.route("/EnterTransaction",methods=['POST','GET'])
def EnterTransaction():
    stat_checker=0
    form=forms.EnterTransactionForm()
    if form.validate_on_submit():
        TransacObj=TransactionController()
        sucess_status=TransacObj.Validate(form)
        if sucess_status==1:
            return redirect(url_for('EnterTransaction'))  
        else:
            return render_template('Invalid_Transactions.html',form=form)
            print("invalid card")
            flash("Transaction Rejected !")  
    return(render_template('Enter_Txn.html',form=form))  
            