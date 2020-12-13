from app import app,db
from flask import render_template,redirect,url_for,flash,request
from models.Transactions import Transaction
from models.Card import CreditCard
from datetime import datetime
from helper.randGenerator import Randpass
from dbController.TransactionDBController import TransactionDBController
from models.Transactions import Transaction
from models.TransactionFacade.TransactionRequest import TransactionRequest
from models.TransactionFacade.TransactionAuthorizationService import TransactionAuthorizationService
import forms
r=Randpass()

class TransactionController():

    def authorize(self,form):
       
        #Transaction Request
        transactionRequest = TransactionRequest()
        transactionRequest.cardNumber = form.cardNumber.data
        transactionRequest.transactionType = form.transactionType.data
        transactionRequest.transactionSource = form.transactionSource.data
        transactionRequest.cardPin = form.cardPin.data
        transactionRequest.cardExpiryDate = form.cardExpiryDate.data
        transactionRequest.transactionDate = form.timestamp.data
        transactionRequest.transactionAmount = form.amount.data

        #Transaction Facade Pattern
        transAuthorize = TransactionAuthorizationService()
        result = transAuthorize.authorizeTransaction(transactionRequest)
        return result
        # stat_checker=0
        # func_checker=0
        # date_checker=r.datecheck(form.timestamp.data)
        # stat_checker=db.session.query(CreditCard).filter(CreditCard.cardNumber==form.cardNumber.data).all()
        # if len(stat_checker)==1 and date_checker ==1:
        #     print("verified")
        #     func_checker=1
        #     TxnCtrl=TransactionDBController()
        #     TdbObj=Transaction(cardNumber=form.cardNumber.data,transactionType=form.transactionType.data,transactionSource=form.transactionSource.data,timestamp=form.timestamp.data,amount=form.amount.data)
        #     TxnCtrl.addTransaction(TdbObj)
        #     return func_checker
        # else:
        #     return 0 
            