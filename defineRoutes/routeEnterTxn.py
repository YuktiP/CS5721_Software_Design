from app import app,db
from flask import render_template,redirect,url_for,flash,request
from models.Transactions import Transaction
from datetime import datetime
from businessController.TransactionController import TransactionController
from enums.Enums import *
import forms

@app.route("/EnterTransaction",methods=['POST','GET'])
def EnterTransaction():
    form=forms.EnterTransactionForm()
    transactionTypes = TransactionType.list()
    sourceTypes = SourceType.list()

    if request.method == 'POST':
        transController=TransactionController()
        result=transController.authorize(form)
        if result.isSuccess:
            flash(result.text)
            return redirect(url_for('EnterTransaction'))  
        else:
            flash(result.text)
            return render_template('Invalid_Transactions.html',form=form)
              
    return(render_template('Enter_Txn.html',form=form,TransTypes=transactionTypes, SrcTypes = sourceTypes))  
            