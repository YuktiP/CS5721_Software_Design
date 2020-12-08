from models.UserAuthentication import  User
from app import app,login_manager,current_user,login_required, login_user,logout_user
from flask import render_template,redirect,url_for,flash,request
import forms

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['POST','GET']) 
@app.route('/login', methods=['POST','GET'])
def login():
    form = forms.Login()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.checkPassword(password=form.password.data):
            login_user(user)
            return "Logged In"
        if not user:
            return '<h1>User not found!!</h1>'
    return(render_template('login.html',form=form))

@app.route('/logout',methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    return "You are logged out!!!"