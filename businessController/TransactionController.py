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

        transAuthorize = TransactionAuthorizationService()
        result = transAuthorize.authorizeTransaction(transactionRequest)
        return result
         
            