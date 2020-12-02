from flask_mysqldb import MySQL
from flask import current_app as app
 
mysql = MySQL()
 
class User():
    def __init__(self, name="",phonenumber="",address="",email="",dateofbirth="",occupation="",income="",username="",password=""):
        self.name=name
        self.phonenumber=phonenumber
        self.address=address
        self.email=email
        self.dateofbirth=dateofbirth
        self.occupation=occupation
        self.income=income
        self.username=username
        self.password=password
 
    def register_User(self):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO userdetails(name,phonenumber,address,email,dateofbirth,occupation,income,username,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.name,self.phonenumber,self.address,self.email,self.dateofbirth,self.occupation,self.income,self.username,self.password))
        mysql.connection.commit()
        cur.close()