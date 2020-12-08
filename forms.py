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

class EnrollForm(FlaskForm):
    FIRSTNAME=StringField('FNAME')
    SURNAME=StringField('SNAME')
    EMAIL=StringField('EMAIL')
    ADDRESS=StringField('ADDR')
    SUBMIT=SubmitField('SUBMIT')

class Login(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField('submit')

class EnterTransactionForm(FlaskForm):
    TRANSACTION_ID=IntegerField('TRANSACTION_ID')
    CARD_NUMBER=IntegerField('CARD_NUMBER')
    TRANSACTION_TYPE=StringField('TRANSACTION_TYPE')
    TIMESTAMP=DateTimeField('TIMESTAMP')
    AMOUNT=IntegerField('AMOUNT')
    SUBMIT=SubmitField('SUBMIT')

class CustomerApplication(FlaskForm):
    first_name=StringField('first_name')
    last_name=StringField('last_name')
    date_of_birth=DateField('date_of_birth')
    address=StringField('address')
    city=StringField('city')
    pin=StringField('pin')
    monthly_income=StringField('monthly_income')
    card_type=StringField('card_type')
    occupation=StringField('occupation')
    ppsn=StringField('ppsn')
    contact_number=StringField('contact_number')
    email=StringField('email')
    submit=SubmitField('submit')