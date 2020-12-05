from flask_wtf import FlaskForm
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
    EMAIL = StringField('EMAIL')
    PASSWORD = PasswordField('PASSWORD')
    SUBMIT = SubmitField('SUBMIT')

class EnterTransactionForm(FlaskForm):
    TRANSACTION_ID=IntegerField('TRANSACTION_ID')
    CARD_NUMBER=IntegerField('CARD_NUMBER')
    TRANSACTION_TYPE=StringField('TRANSACTION_TYPE')
    TIMESTAMP=DateTimeField('TIMESTAMP')
    AMOUNT=IntegerField('AMOUNT')
    SUBMIT=SubmitField('SUBMIT')
