from Interfaces.IDashboard import IDashboard
from models.CustomerApplication import *
from flask import request, redirect, url_for
from flask import render_template,redirect,request,url_for,flash
from werkzeug.utils import secure_filename
import csv
import pandas as pd 
import os
import urllib.request
from models.card import Creditcard
from models.Account import Account
from models.UserAuthentication import User
import datetime
from datetime import date
from helper.randGenerator import Randpass
from app import db
import app
import forms
from werkzeug.security import generate_password_hash
from enums.Enums import *

from models.AccountBuilder import AccountBuilder as ab, AccountDirector as ad


class Onboard():

    def BulkOnboard(self,docpath):
        data=pd.read_csv(docpath)
        df =pd.DataFrame(data, columns= ['firstName','lastName','dob','email','address','city','zipcode','occupation','monthlyIncome','cardType'])
        print(df)
        for i in df.itertuples():
            randomVar=Randpass()
            passwd=randomVar.passGen()
            print(passwd)
            haspwd=generate_password_hash(passwd, method='sha256')
            pin=randomVar.pinGen() 
            cardNo=randomVar.cardGen()  
            expDate=randomVar.cardExp()
            acno=randomVar.accGen()
            userId=randomVar.userGen()
            opendate=date.today()
            if i.cardType=='PLATINUM':
                credlimit=10000
            elif i.cardType=='BRONZE':
                credlimit=8000
            else:
                credlimit=5000        
            c=Creditcard(cardNo,pin,12,expDate,1,i.cardType)
            c.addCard()
            a=Account(acno,userId,cardNo,opendate,credlimit,credlimit,'open')
            a.addAccount()
            u=User(userId,acno,"username",haspwd,i.firstName,i.lastName,"customer",i.dob,i.email,i.address,i.city,i.zipcode,i.occupation,i.monthlyIncome)
            u.addUser()
        self.result=db.session.query(User).all()
        return self

    def singleOnboard(self,applicationId):
            application = db.session.query(CustomerApplication).filter(CustomerApplication.id == applicationId).first()
            randomVar=Randpass()
            passwd=randomVar.passGen()
            haspwd=generate_password_hash(passwd, method='sha256')
            pin=randomVar.pinGen() 
            cardNo=randomVar.cardGen()  
            expDate=randomVar.cardExp()
            acno=randomVar.accGen()
            userId=randomVar.userGen()
            opendate=datetime.datetime.now()
            if application.cardType=='PLATINUM':
                credlimit=10000
            elif application.cardType=='BRONZE':
                credlimit=8000
            else:
                credlimit=5000 
            
            accountBuilder = ab.AccountBuilder()
            accountDirector = ad.AccountDirector()
            accountDirector.setBuilder(accountBuilder)
            account = accountDirector.getAccount(application)

            #c=Creditcard(cardNo,pin,12,expDate,1,i.cardType)
            c = account.card
            c.addCard()
            u = account.user
            u.addUser()

            a=Account()
            a.accountNumber = acno
            a.userId=u.userId
            a.cardNumber=c.cardNo
            a.createdDate=opendate 
            a.currentBalance=c.creditLimit
            a.availableBalance=c.creditLimit
            a.status=Status(Status.Active).value
            a.addAccount()