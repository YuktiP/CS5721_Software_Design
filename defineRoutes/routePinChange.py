from models.UserAuthentication import  User
from models.PinChange import PinChange
from app import app,login_manager,current_user,login_required, login_user,logout_user
from flask import render_template,redirect,url_for,flash,request
import forms


@app.route('/pinChange', methods=['POST','GET'])
def pinChange():
    form = forms.PinChange()
    userId=current_user.get_id()
    pinObj = PinChange(userId)
    if form.validate_on_submit():
        if pinObj.checkPin(form.password1.data):
            pinObj.setPin(password2=form.password2.data)
            return "PIN Changed Successfully"
        else:
            return "Incorrect PIN Entered"
    return(render_template('pinChange.html',form=form))