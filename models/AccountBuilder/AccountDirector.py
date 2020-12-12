from models.Account import Account
class AccountDirector:
   
   
   def setBuilder(self, builder,):
      self.builder = builder
   
   def getAccount(self, customerApplication):
      account = Account()
     #User
      user = self.builder.getUser(customerApplication)
      account.user = user
      #Card
      card = self.builder.getCard(customerApplication)
      account.card = card
      
      #Account
      return account