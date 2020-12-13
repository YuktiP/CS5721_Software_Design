from models.Decorator.IDecorator import IDecorator

class ConcreteCard(IDecorator):

    def getCreditLimit(self):
        return 1000

    def getInterest(self):
        return 1