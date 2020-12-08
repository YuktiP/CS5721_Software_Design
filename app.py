from flask import Flask,request,render_template, redirect
from flask_sqlalchemy import SQLAlchemy
#from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, current_user, login_required,logout_user,login_user
import yaml
app=Flask(__name__)

#config db in yaml file
dbase = yaml.full_load(open('db_setup.yaml'))

#getting values from yaml file
MYSQL_HOST = dbase['mysql_host']
MYSQL_USER = dbase['mysql_user']
MYSQL_PASSWORD = dbase['mysql_password']
MYSQL_DB = dbase['mysql_db']

#Using SQL Alchemy [ORM]
app.config['SECRET_KEY']='SECURITY_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+MYSQL_USER+':'+MYSQL_PASSWORD+'@'+MYSQL_HOST+'/'+MYSQL_DB
#app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:password@localhost/qwerty'
db=SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view

#Import Routes
#from routes import *
from defineRoutes.routeCustomerApplication import *
from defineRoutes.routeUserAuthentication import *

if __name__ == "__main__":
    app.run(debug=True)