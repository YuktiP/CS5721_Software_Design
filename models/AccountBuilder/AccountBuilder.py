from models.AccountBuilder import AbstractBuilder as abs
from models.UserAuthentication import User
from models.Card import CreditCard
from helper.randGenerator import Randpass
from enums.Enums import *
from werkzeug.security import generate_password_hash
from models.Decorator.CardDecoratorService import CardDecoratorService

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
        user.zipcode = customerApplication.zipcode
        user.occupation = customerApplication.occupation
        user.monthly_income = customerApplication.monthly_income
        return user
        
    def getCard(self,customerApplication):
        randomVar=Randpass()

        card = CreditCard()
        card.cardNumber = randomVar.cardGen() 
        card.pin = randomVar.pinGen()
        card.cardCode = randomVar.codeGen()
        card.expiryDate = randomVar.cardExp()
        card.cardStatus = Status(Status.Active).value
        card.cardType = customerApplication.cardType

        #Card Decorator
        cardDecorator = CardDecoratorService()
        decoratedCard = cardDecorator.decorateCard(customerApplication.cardType)
        card.creditLimit = decoratedCard.creditLimit
        card.interest = decoratedCard.interest
        card.availableCreditLimit=card.creditLimit
        card.currentCreditLimit=card.creditLimit
        return card 
    
 
