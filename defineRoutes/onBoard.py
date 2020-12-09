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
from models.account import Account
from models.UserAuthentication import User
import datetime
from datetime import date
from passgen import Randpass
from app import db
import app
import forms
from werkzeug.security import generate_password_hash

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
    def singleOnboard(self,list):
        for i in list:
            randomVar=Randpass()
            passwd=randomVar.passGen()
            haspwd=generate_password_hash(passwd, method='sha256')
            pin=randomVar.pinGen() 
            cardNo=randomVar.cardGen()  
            expDate=randomVar.cardExp()
            acno=randomVar.accGen()
            userId=randomVar.userGen()
            opendate=date.today()
            if i.card_type=='PLATINUM':
                credlimit=10000
            elif i.card_type=='BRONZE':
                credlimit=8000
            else:
                credlimit=5000 
            c=Creditcard(cardNo,pin,12,expDate,1,i.cardType)
            c.addCard()
            a=Account(acno,userId,cardNo,opendate,credlimit,credlimit,'open')
            a.addAccount()
            u=User(userId,acno,"username",haspwd,i.firstName,i.lastName,"customer",i.dateOfBirth,i.email,i.address,i.city,i.pin,i.occupation,i.monthly_income)
            u.addUser()