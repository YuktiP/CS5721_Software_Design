from app import db,app
from models.UserAuthentication import User
from passgen import Randpass
test=Randpass()
class Setup():
    def Admin(self):
        userId=test.userGen()
        #userId,acno,"username",haspwd,i.firstName,i.lastName,"customer",i.dob,i.email,i.address,i.city,i.zipcode,i.occupation,i.monthlyIncome
        u=User(userId,111111,'ADMIN','ADMIN','ADMIN','ADMIN','ADMIN','1990-10-12','admin@login.com','NULL','NULL','NULL','NULL','0')
        u.addUser()
    def Employee(self):
        userId=test.userGen()
        #userId,acno,"username",haspwd,i.firstName,i.lastName,"customer",i.dob,i.email,i.address,i.city,i.zipcode,i.occupation,i.monthlyIncome
        u=User(userId,111112,'EMPLOYEE','EMPLOYEE','EMPLOYEE','EMPLOYEE','EMPLOYEE','1990-10-12','employee@login.com','NULL','NULL','NULL','NULL','0')
        u.addUser()    