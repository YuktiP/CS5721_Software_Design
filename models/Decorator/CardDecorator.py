from models.Decorator.IDecorator import IDecorator

class CardDecorator(IDecorator):

    def __init__(self,decoratedCard):
      self.decoratedCard = decoratedCard
   
    def getCreditLimit(self):
      return self.decoratedCard.getCreditLimit()
   
    def get_ingredients(self):
      return self.decoratedCard.getInterest()
