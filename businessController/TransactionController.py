from app import app,db
from flask import render_template,redirect,url_for,flash,request
from models.Transactions import Transaction
from models.card import Creditcard
from datetime import datetime
from passgen import Randpass
from dbController.TransactionDBController import TransactionDBController
from models.Transactions import Transaction
import forms
r=Randpass()

class TransactionController():

    def Validate(self,form):
        #TdbObj=TransactionDBController(cardNumber=form.cardNumber.data,transactionType=form.transactionType.data,transactionSource=form.transactionSource.data,timestamp=form.timestamp.data,amount=form.amount.data)
        stat_checker=0
        func_checker=0
        date_checker=r.datecheck(form.timestamp.data)
        stat_checker=db.session.query(Creditcard).filter(Creditcard.cardNumber==form.cardNumber.data).all()
        if len(stat_checker)==1 and date_checker ==1:
            print("verified")
            func_checker=1
            TxnCtrl=TransactionDBController()
            TdbObj=Transaction(cardNumber=form.cardNumber.data,transactionType=form.transactionType.data,transactionSource=form.transactionSource.data,timestamp=form.timestamp.data,amount=form.amount.data)
            TxnCtrl.addTransaction(TdbObj)
            return func_checker
        else:
            return 0 
            