from dbController.CardDBController import CardDBController


class BlockCardController():

    def __init__(self):
        self = self


    def initiateBlockCard(self, cardNumber):
        self.cardNumber = cardNumber
        dbObj = CardDBController()
        dbObj.setCardBlockStatus(cardNumber)
