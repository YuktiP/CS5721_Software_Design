from models.Decorator.ConcreteCard import ConcreteCard
from models.Decorator.BasicCard import BasicCard
from models.Decorator.BlackCard import BlackCard
from models.Decorator.StudentCard import StudentCard

class CardDecoratorService():

    def decorateCard(self, cardType):

        card = ConcreteCard()
        if cardType=='Black':
            card = BlackCard(card)
        elif cardType=='Basic':
            card = BasicCard(card)
        elif cardType=='Student':
            card = StudentCard(card)

        self.creditLimit = card.getCreditLimit()
        self.interest = card.getInterest()
        return self