from models.Decorator.CardDecorator import CardDecorator

class BlackCard(CardDecorator):

    def __init__(self,decoratedCard):
      CardDecorator.__init__(self,decoratedCard)
   
    def getCreditLimit(self):
      return self.decoratedCard.getCreditLimit() + 9000
   
    def getInterest(self):
      return self.decoratedCard.getInterest() + 0.8