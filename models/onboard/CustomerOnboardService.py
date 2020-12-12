from models.Result import Result
from models.AccountBuilder import AccountBuilder as ab,AccountDirector as ad
from dbController.CardDBController import CardDBController
from dbController.UserDBController import UserDBController
from dbController.AccountDBController import AccountDBController

class CustomerOnBoardService():

    def __init__(self):
        self = self

    def onBoardCustomer(self,application):
           #Create Account using Builder Pattern
            accountBuilder = ab.AccountBuilder()
            accountDirector = ad.AccountDirector()
            accountDirector.setBuilder(accountBuilder)
            account = accountDirector.getAccount(application)
            
            cardDB = CardDBController()
            cardDB.addCard(account.card)
            
            userDB = UserDBController()
            userDB.addUser(account.user)

            accountDB = AccountDBController()
            accountDB.addAccount(account)

            return Result(isSuccess=True,text="Customer Onboarded Successfully", data = account.user)