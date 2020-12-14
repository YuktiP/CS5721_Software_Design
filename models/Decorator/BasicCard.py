from models.Decorator.CardDecorator import CardDecorator

class BasicCard(CardDecorator):

    def __init__(self,decoratedCard):
      CardDecorator.__init__(self,decoratedCard)
   
    def getCreditLimit(self):
      return self.decoratedCard.getCreditLimit() + 7000
   
    def getInterest(self):
      return self.decoratedCard.getInterest() + 0.2