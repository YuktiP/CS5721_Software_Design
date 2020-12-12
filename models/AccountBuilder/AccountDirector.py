from models.Account import Account
import datetime
from helper.randGenerator import Randpass
from enums.Enums import *

class AccountDirector:
   
   def setBuilder(self, builder,):
        self.builder = builder
   
   def getAccount(self, customerApplication):
        randomVar=Randpass()
        account = Account()
        #User
        user = self.builder.getUser(customerApplication)
        #Card
        card = self.builder.getCard(customerApplication)
        #Account
        account.user = user
        account.userId = user.userId
        account.card = card
        account.cardNumber = card.cardNumber
        account.currentBalance=card.creditLimit
        account.availableBalance=card.creditLimit
        account.createdDate=datetime.datetime.now() 
        account.status=Status(Status.Active).value
        account.accountNumber = randomVar.accGen()
        
        return account