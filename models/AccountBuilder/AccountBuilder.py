from models.AccountBuilder import AbstractBuilder as abs
from models.UserAuthentication import User
from models.Card import CreditCard
from helper.randGenerator import Randpass
from enums.Enums import *
from werkzeug.security import generate_password_hash

class AccountBuilder(abs.AbstractBuilder):
    
    def getUser(self,customerApplication):
        randomVar=Randpass()
        user = User()
        user.userId = randomVar.userGen()
        user.accountNumber = randomVar.accGen()
        user.userName = customerApplication.lastName +','+  customerApplication.firstName 
        user.firstName = customerApplication.firstName 
        user.lastName = customerApplication.lastName
        user.password = generate_password_hash(randomVar.passGen(), method='sha256')
        user.Role = Role(Role.Customer).value
        user.dob = customerApplication.dateOfBirth
        user.email = customerApplication.email
        user.address = customerApplication.address
        user.city = customerApplication.city
        user.pin = customerApplication.pin
        user.occupation = customerApplication.occupation
        user.monthly_income = customerApplication.monthly_income
        return user
        
    def getCard(self,customerApplication):
        randomVar=Randpass()

        if customerApplication.cardType=='PLATINUM':
            credlimit=10000
            interest = 1.2
        elif customerApplication.cardType=='BRONZE':
            credlimit=8000
            interest=2.6
        else:
            credlimit=5000
            interest=1

        card = Creditcard()
        card.cardNo = randomVar.cardGen() 
        card.pin = randomVar.pinGen()
        card.cardCode = randomVar.codeGen()
        card.expDate = randomVar.cardExp()
        card.status = Status(Status.Active).value
        card.cardType = customerApplication.cardType
        card.creditLimit = credlimit
        card.interest = interest
        return card
    
 
