from app import app
from flask import render_template, request, redirect, flash, url_for
from flask_login import current_user
from businessController.BlockCardRequestController import BlockCardRequest


@app.route('/User', methods=['POST','GET'])
def UserDashboard(): 
    if request.method =='POST':
        if "viewstatement" in request.form:
            return redirect(url_for('.statement'))

        elif "blockcard" in request.form:
            userId = current_user.get_id()
            blockCardRequest = BlockCardRequest(userId)
            currentBlockRequestStatus = blockCardRequest.currentBlockRequest()

            if currentBlockRequestStatus == 1 :
                message = "A block request has already been lodged for this card."
                flash(message)
                return redirect(url_for('UserDashboard'))

            else:
                blockCardRequest.blockRequest()
                message = "A block request has been lodged."
                flash(message) 
                return redirect(url_for('UserDashboard'))
            
        elif "changepin" in request.form: 
            return redirect(url_for('UserDashboard'))

    elif request.method == 'GET':
        return(render_template("CustomerPage.html"))