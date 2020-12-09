from app import app
from flask import render_template,redirect,url_for,flash,request
from models.Transactions import Transaction
import forms
@app.route("/Enter_Transaction",methods=['POST','GET'])
def Enter_Transaction():
    form=forms.EnterTransactionForm()
    if form.validate_on_submit():
        txn=Transaction(cardNumber=form.cardNumber.data,transactionType=form.transactionType.data,transactionSource=form.transactionSource.data,timestamp=form.timestamp.data,amount=form.amount.data)
        txn.addTransaction()
        return redirect(url_for('Enter_Transaction'))
    return(render_template('Enter_Txn.html',form=form))  