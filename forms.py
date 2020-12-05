from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,PasswordField,validators
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