from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField,SubmitField,IntegerField,PasswordField,validators,DateTimeField
from flask import Flask, request
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Optional
)



class Login(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField('Submit')

class PinChange(FlaskForm):
    password1 = PasswordField('password1')
    password2 = PasswordField('password2')
    submit = SubmitField('submit')

class EnterTransactionForm(FlaskForm):
    cardNumber=IntegerField('cardNumber')
    transactionType=StringField('transactionType')
    transactionSource=StringField('transactionSource')
    timestamp=DateTimeField('timestamp')
    cardExpiryDate = DateTimeField('timestamp')
    cardPin = IntegerField('cardPin')
    amount=IntegerField('amount')
    submit=SubmitField('Submit')

class CustomerApplication(FlaskForm):
    first_name=StringField('first_name')
    last_name=StringField('last_name')
    date_of_birth=DateField('date_of_birth')
    address=StringField('address')
    city=StringField('city')
    zipcode=StringField('zipcode')
    monthly_income=StringField('monthly_income')
    cardType=StringField('cardType')
    occupation=StringField('occupation')
    ppsn=StringField('ppsn')
    contact_number=StringField('contact_number')
    email=StringField('email')
    submit=SubmitField('submit')