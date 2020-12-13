from models.Decorator.CardDecorator import CardDecorator

class StudentCard(CardDecorator):

    def __init__(self,decoratedCard):
      CardDecorator.__init__(self,decoratedCard)
   
    def getCreditLimit(self):
      return self.decoratedCard.getCreditLimit() + 4000
   
    def get_ingredients(self):
      return self.decoratedCard.getInterest() - 0.2