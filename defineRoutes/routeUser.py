from models.CustomerApplication import CustomerApplication
from app import app
from flask import render_template,redirect
import forms

@app.route('/', methods=['POST','GET']) 
@app.route('/login', methods=['POST','GET'])
def login():
    form = forms.Login()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            return redirect("/Dashboard")
        if not user:
            return '<h1>User not found!!</h1>'
    return(render_template('login.html',form=form))