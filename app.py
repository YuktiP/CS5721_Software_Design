from flask import Flask,request,render_template, redirect
from flask_sqlalchemy import SQLAlchemy
#from flask_mysqldb import MySQL
#import yaml

app=Flask(__name__)

#config db in yaml file
#dbase = yaml.load(open('db_setup.yaml'))
#Using MySQL
#app.config['MYSQL_HOST'] = dbase['mysql_host']
#app.config['MYSQL_USER'] = dbase['mysql_user']
#app.config['MYSQL_PASSWORD'] = dbase['mysql_password']
#app.config['MYSQL_DB'] = dbase['mysql_db']
#mysql = MySQL(app)
#cur = mysql.connection.cursor()

#Using SQL Alchemy
app.config['SECRET_KEY']='SECURITY_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/qwerty'
#app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:password@server'
db=SQLAlchemy(app)


from routes import *
if __name__ == "__main__":
    app.run(debug=True)