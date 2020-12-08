from models.CustomerApplication import CustomerApplication
from app import app
from flask import render_template
import forms

@app.route('/', methods=['POST','GET']) 
@app.route('/login', methods=['POST','GET'])
def login():
    form = forms.Login()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(EMAIL=form.EMAIL.data).first()
        if user and user.check_password(PASSWORD=form.PASSWORD.data):
            login_user(user)
            return "Logged In"
        if not user:
            return '<h1>User not found!!</h1>'
    return(render_template('login.html',form=form))