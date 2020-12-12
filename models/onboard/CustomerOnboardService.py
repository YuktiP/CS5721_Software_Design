from models.Result import Result
from models.AccountBuilder import AccountBuilder as ab,AccountDirector as ad
from models.Card import CreditCard

class CustomerOnBoardService():

    def __init__(self):
        self = self

    def onBoardCustomer(self,application):
           #Create Account using Builder Pattern
            accountBuilder = ab.AccountBuilder()
            accountDirector = ad.AccountDirector()
            accountDirector.setBuilder(accountBuilder)
            account = accountDirector.getAccount(application)
            
            card = account.card
            card.addCard()
            user = account.user
            user.addUser()
            account.addAccount()

            return Result(isSuccess=true,text="Customer Onboarded Successfully")