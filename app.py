from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SECRET_KEY']='SECURITY_KEY'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///collection.db'
db=SQLAlchemy(app)
from routes import *
if __name__ == "__main__":
    app.run(debug=True)