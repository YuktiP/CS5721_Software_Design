from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

class EnrollForm(FlaskForm):
    FIRSTNAME=StringField('FNAME')
    SURNAME=StringField('SNAME')
    EMAIL=StringField('EMAIL')
    ADDRESS=StringField('ADDR')
    SUBMIT=SubmitField('SUBMIT')
